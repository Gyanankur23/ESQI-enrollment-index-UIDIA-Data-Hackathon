import pandas as pd
from pathlib import Path

ENROLL_FILES = ["enrollment_1.xlsx", "enrollment_2.xlsx", "enrollment_3.xlsx"]
BIO_FILES = ["biometric_1.xlsx", "biometric_2.xlsx", "biometric_3.xlsx", "biometric_4.xlsx"]

def normalize(series):
    if series.empty or (series.max() == series.min()):
        return series
    return (series - series.min()) / (series.max() - series.min())

def fast_read_and_process(file_list, cols, sum_col_name, sum_cols):
    aggregated_data = []
    
    for file in file_list:
        p = Path(file)
        cache_file = p.with_suffix('.parquet')
        
        if not cache_file.exists():
            print(f"Optimizing {file}...")
            temp_df = pd.read_excel(file, engine='calamine', usecols=cols)
            
            # FIX: Force date conversion before saving to Parquet
            if 'date' in temp_df.columns:
                temp_df['date'] = pd.to_datetime(temp_df['date'], dayfirst=True, errors='coerce')
            
            temp_df.to_parquet(cache_file, index=False)
            del temp_df
        
        df = pd.read_parquet(cache_file)
        
        # Ensure month period exists for grouping
        df["month"] = df["date"].dt.to_period("M")
        df[sum_col_name] = df[sum_cols].apply(pd.to_numeric, errors='coerce').fillna(0).sum(axis=1)

        monthly = df.groupby("month", as_index=False).agg({sum_col_name: "sum"})
        aggregated_data.append(monthly)
        del df

    return pd.concat(aggregated_data).groupby("month", as_index=False).sum()

# --- EXECUTION ---

# 1. Process Enrollments
enrollment_monthly = fast_read_and_process(
    ENROLL_FILES, 
    ['date', 'age_0_5', 'age_5_17', 'age_18_greater'],
    'total_enrollments',
    ['age_0_5', 'age_5_17', 'age_18_greater']
)

# 2. Rolling Statistics
enrollment_monthly["roll_mean"] = enrollment_monthly["total_enrollments"].rolling(3).mean()
enrollment_monthly["roll_std"] = enrollment_monthly["total_enrollments"].rolling(3).std()
enrollment_monthly["enrollment_stress"] = (
    (enrollment_monthly["total_enrollments"] - enrollment_monthly["roll_mean"]) / 
    enrollment_monthly["roll_std"]
).fillna(0)

# 3. Process Biometrics
biometric_monthly = fast_read_and_process(
    BIO_FILES,
    ["date", "bio_age_5_17", "bio_age_17_"],
    "biometric_transactions",
    ["bio_age_5_17", "bio_age_17_"]
)

# 4. Final Merge & Scoring
final = enrollment_monthly.merge(biometric_monthly, on="month", how="left").dropna()

final["n_stress"] = normalize(final["enrollment_stress"])
final["n_enroll"] = normalize(final["total_enrollments"])
final["n_bio"] = normalize(final["biometric_transactions"])

final["ESQI"] = 100 * (0.5 * final["n_stress"] + 0.3 * final["n_enroll"] + 0.2 * final["n_bio"])
final["month"] = final["month"].dt.to_timestamp()

final.to_csv("final_esqi_monthly.csv", index=False)
print(f"DONE ✅ | Saved to final_esqi_monthly.csv")
