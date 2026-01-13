import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Aadhaar ESQI Dashboard",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("final_esqi_monthly.csv", parse_dates=["month"])

latest = df.iloc[-1]

# -----------------------------
# HEADER
# -----------------------------
st.title("Aadhaar Enrollment Stress & Quality Intelligence (ESQI)")
st.markdown(
    """
    **Purpose:**  
    Early detection of enrollment system stress and biometric quality degradation  
    using aggregated Aadhaar enrollment and biometric activity data.
    """
)

# -----------------------------
# KPI ROW
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric(
    "Latest ESQI",
    f"{latest['ESQI']:.1f}"
)

col2.metric(
    "Monthly Enrollments",
    f"{int(latest['total_enrollments']):,}"
)

col3.metric(
    "Biometric Transactions",
    f"{int(latest['biometric_transactions']):,}"
)

st.divider()

# -----------------------------
# ESQI TREND
# -----------------------------
st.subheader("System Health Over Time")

fig_esqi = px.line(
    df,
    x="month",
    y="ESQI",
    labels={"ESQI": "ESQI Score", "month": "Month"}
)
fig_esqi.add_hline(
    y=df["ESQI"].mean(),
    line_dash="dash",
    annotation_text="Average ESQI",
    annotation_position="bottom right"
)

st.plotly_chart(fig_esqi, use_container_width=True)

# -----------------------------
# ENROLLMENT STRESS
# -----------------------------
st.subheader("Enrollment Load & Stress")

fig_enroll = px.line(
    df,
    x="month",
    y=["total_enrollments", "enrollment_stress"],
    labels={"value": "Metric Value", "month": "Month"}
)

st.plotly_chart(fig_enroll, use_container_width=True)

# -----------------------------
# BIOMETRIC QUALITY
# -----------------------------
st.subheader("Biometric Activity Trend")

fig_bio = px.line(
    df,
    x="month",
    y="biometric_transactions",
    labels={
        "biometric_transactions": "Biometric Transactions",
        "month": "Month"
    }
)

st.plotly_chart(fig_bio, use_container_width=True)

# -----------------------------
# INTERPRETATION (CRITICAL)
# -----------------------------
st.divider()

st.markdown(
    """
    ### How to interpret ESQI
    - **Higher ESQI** → Increased enrollment pressure and quality stress  
    - **Spikes** → Periods requiring operational or policy intervention  
    - **Stabilization** → Post-intervention normalization

    **Why this matters:**  
    Early identification of enrollment stress helps prevent downstream
    authentication failures and service disruption.
    """
)
