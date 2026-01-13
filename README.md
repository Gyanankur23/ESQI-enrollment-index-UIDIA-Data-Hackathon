# Enrollment Stress & Quality Index (ESQI)

[![Streamlit App](https://img.shields.io/badge/Live-Demo-00c853?style=for-the-badge&logo=streamlit)](https://esqi-enrollment-index-uidia-data-hackathon.streamlit.app)
[![GitHub License](https://img.shields.io/github/license/Gyanankur23/ESQI-enrollment-index-UIDIA-Data-Hackathon?style=for-the-badge)](https://github.com/Gyanankur23/ESQI-enrollment-index-UIDIA-Data-Hackathon/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Gyanankur23/ESQI-enrollment-index-UIDIA-Data-Hackathon?style=for-the-badge)](https://github.com/Gyanankur23/ESQI-enrollment-index-UIDIA-Data-Hackathon/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/Gyanankur23/ESQI-enrollment-index-UIDIA-Data-Hackathon?style=for-the-badge)](https://github.com/Gyanankur23/ESQI-enrollment-index-UIDIA-Data-Hackathon)

---

A composite early-warning metric for Aadhaar enrollment systems, developed during the UIDIA Data Hackathon by **Gyanankur Baruah** and **Vishakha Gupta**.  
ESQI combines enrollment stress, volume, and biometric activity into a single score (0–100 scale) to track system resilience under load.

---

## 🔗 Live Demo
Explore the interactive dashboard:  
👉 [Streamlit App](https://esqi-enrollment-index-uidia-data-hackathon.streamlit.app)

---

## 📁 Repository Structure
- `app_streamlit.py` — Streamlit dashboard interface  
- `core_esqi.py` — ESQI computation logic  
- `charts_plotly.py` — Plotly visualizations  
- `enrollment_*.xlsx` — Enrollment data by age group  
- `biometric_*.xlsx` — Biometric transaction data  
- `final_esqi_monthly.csv` — Aggregated ESQI scores  
- `requirements.txt` — Python dependencies  

---

## 📊 ESQI Formula
```python
ESQI = 0.5 * enrollment_stress + 0.3 * enrollment_volume + 0.2 * biometric_activity


```
## License
This project is licensed under the MIT License (github.com in Bing).

## 📚 Presentation
Full analysis and visuals available in the ESQI Presentation (PPTX) 

Made with ❤️ by Gyanankur23


ESQI = 0.5 * enrollment_stress + 0.3 * enrollment_volume + 0.2 * biometric_activity

