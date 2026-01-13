import pandas as pd
import plotly.express as px

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("final_esqi_monthly.csv", parse_dates=["month"])

# -----------------------------
# CHART 1: Enrollment Volume vs Stress
# -----------------------------
fig1 = px.line(
    df,
    x="month",
    y=["total_enrollments", "enrollment_stress"],
    title="Enrollment Load vs System Stress",
    labels={"value": "Metric Value", "month": "Month"}
)
fig1.show()

# -----------------------------
# CHART 2: Biometric Transactions
# -----------------------------
fig2 = px.line(
    df,
    x="month",
    y="biometric_transactions",
    title="Biometric Activity Over Time",
    labels={
        "biometric_transactions": "Biometric Transactions",
        "month": "Month"
    }
)
fig2.show()

# -----------------------------
# CHART 3: ESQI Trend (Before / After)
# -----------------------------
fig3 = px.line(
    df,
    x="month",
    y="ESQI",
    title="Enrollment Stress & Quality Index (ESQI)",
    labels={"ESQI": "ESQI Score", "month": "Month"}
)
fig3.add_hline(
    y=df["ESQI"].mean(),
    line_dash="dash",
    annotation_text="Average ESQI",
    annotation_position="bottom right"
)

fig3.show()
