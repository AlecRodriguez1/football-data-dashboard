#  Football Data Dashboard (2024/25)

An interactive Streamlit dashboard that analyzes attacking performance across Europe’s top five football leagues during the 2024/25 season.  
The project focuses on goal scoring, assists, and per-90 metrics to allow fair comparison between players with different playing time.

---

##  Project Overview

This dashboard provides:
- A league-wide view of top goal scorers
- League-specific breakdowns (Premier League, La Liga, Bundesliga, Serie A, Ligue 1)
- Per-90 analysis to evaluate efficiency and consistency
- Interactive visualizations to explore trends and patterns in attacking output

The goal of the project is to combine **data analysis, visualization, and UI clarity** into a single, easy-to-explore application.

---

##  Features

- **Top 25 scorers across Europe’s top 5 leagues**
- **Top 10 scorers visualized with bar charts**
- **League selector** for league-specific analysis
- **Per-90 statistics**:
  - Goals per 90
  - Assists per 90
  - Goals + Assists per 90
- **Minimum minutes filter** to reduce small-sample bias
- **Scatter plot visualization** to compare efficiency vs playing time
- Clear captions explaining each table and chart

---

##  Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly Express**

---

##  Screenshots

### Dashboard Overview
<img width="1470" height="836" alt="Screenshot 2025-12-22 at 9 51 32 PM" src="https://github.com/user-attachments/assets/57ac3f56-3281-4c20-9a0b-bee94d43da09" />


### Top Scorers Across Top 5 Leagues
<img width="1470" height="836" alt="Screenshot 2025-12-22 at 9 51 32 PM" src="https://github.com/user-attachments/assets/2fb88649-4db2-4cc9-9b5f-619843b8b3f7" />
<img width="1470" height="836" alt="Screenshot 2025-12-22 at 9 51 46 PM" src="https://github.com/user-attachments/assets/170baae3-0321-4d89-a928-33ed3d53105d" />


### League-Specific Analysis
<img width="1470" height="836" alt="Screenshot 2025-12-22 at 9 52 20 PM" src="https://github.com/user-attachments/assets/bdeeb1f4-bccf-489d-a59e-5d9d9bb81e14" />
<img width="1470" height="836" alt="Screenshot 2025-12-22 at 9 52 27 PM" src="https://github.com/user-attachments/assets/9a2e9885-657e-4ac5-b5f1-bfa732a96002" />


### Per-90 Performance Analysis
<img width="1470" height="836" alt="Screenshot 2025-12-22 at 9 52 56 PM" src="https://github.com/user-attachments/assets/9934aba8-8630-4d62-96ee-4df7cc9d6340" />
<img width="1470" height="836" alt="Screenshot 2025-12-22 at 9 53 07 PM" src="https://github.com/user-attachments/assets/5e00d20e-9da4-4071-8f9c-6e37d465c244" />


---

##  Data Source

- **Platform:** Kaggle  
- **Dataset:** Football Players Stats (2024–2025)  
- **Author:** Hubert Sidorowicz  
- **License:** MIT  

Data is originally sourced from **FBref** and updated weekly.

 [View dataset on Kaggle](https://www.kaggle.com/datasets/hubertsidorowicz/football-players-stats-2024-2025)

---

##  How to Run Locally

```bash
pip install streamlit pandas plotly
streamlit run app.py
