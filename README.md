That's fantastic\! Based on the comprehensive project structure and tasks you completed for the **10 Academy: Artificial Intelligence Mastery (KAIM) Week 0 Challenge**, here is a professional and detailed `README.md` file.

This document covers all the requirements, including setup, running instructions, and a summary of your key findings for MoonLight Energy Solutions.

```markdown
# ☀️ solar-challenge-week0: Cross-Country Solar Farm Analysis

## Project Overview

This repository contains the solution for the **10 Academy: Artificial Intelligence Mastery (KAIM) Week 0 Challenge**. The core objective was to perform a quick analysis of solar farm environmental measurement data from **Benin, Sierra Leone, and Togo** to inform a strategic recommendation for **MoonLight Energy Solutions** on high-potential regions for solar installation.

The project demonstrates proficiency in Git & GitHub , environment setup , Exploratory Data Analysis (EDA), data cleaning, statistical comparison and dashboard creation using Streamlit.

---

## 🚀 Business Objective (MoonLight Energy Solutions)

As an Analytics Engineer, the task was to analyze environmental data—including Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and various temperature/wind metrics to identify key trends and translate observations into a data-driven strategy report. The final recommendation focuses on identifying high-potential regions for solar installation that align with the company's long-term sustainability goals.

## 💻 Deployment and Access

The interactive dashboard for this project was built using **Streamlit** and deployed to the Streamlit Community Cloud.

**Access the Live Dashboard Here:**

👉 [**https://eyobhailu-solar-challenge-week0.streamlit.app/**](https://eyobhailu-solar-challenge-week0.streamlit.app/)

---

## 🛠️ Project Structure and Technologies

The repository structure follows the recommended pattern, ensuring separation of notebooks, source code, and configuration files:
```

├── .github/
│ └── workflows/
│ └── ci.yml \# Basic CI check for dependency installation
├── app/
├── main.py \# Main Streamlit application script
└── utils.py \# Utility functions for data processing/viz
├── notebooks/
├── \<country\>\_eda.ipynb \# Notebooks for Task 2: Data Cleaning & EDA and task 4 for comparing countries
requirements.txt \# List of all project dependencies
├── README.md
.gitignore \# Excludes sensitive data/ and temporary files

````

### Technology Stack

*Language:** Python 3.x
* **Core Libraries:** Pandas, NumPy (for data manipulation)
* **Visualization:** Matplotlib, Seaborn (for EDA)
* **Web App:** Streamlit (for the interactive dashboard)
* **Version Control:** Git & GitHub
***Automation:** GitHub Actions (for CI/CD)

---

## ⚙️ Setup and Environment Reproduction

The project uses a Python virtual environment to manage dependencies. The following steps reproduce the environment locally:

### 1. Clone the Repository

```bash
git clone [https://github.com/](https://github.com/)<eyob-hailu>/solar-challenge-week0.git
cd solar-challenge-week0
````

### 2\. Set up the Python Virtual Environment

Use either `venv` or `conda` to create and activate a virtual environment.

**Using `venv`:**

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
# .\venv\Scripts\activate.ps1 # On Windows PowerShell
```

### 3\. Install Dependencies

Install all required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4\. Data Preparation

**Note:** The raw data files are not included in the repository and are tracked by the `.gitignore` file.

- Place the raw data files (e.g., `togo-dapaong_qc.csv`) into a local `data/` folder.
- Run the notebooks in `notebooks/` (Task 2 & 3) to perform cleaning and generate the required clean CSVs (`data/*_clean.csv`) which are used by the Streamlit application.

---

## ▶️ How to Run the Interactive Dashboard

The project includes an optional, interactive Streamlit dashboard (Task 4).

1.  Ensure the environment is set up and activated (as per the section above).
2.  Ensure the necessary **cleaned** data files (`data/*_clean.csv`) exist locally, as the Streamlit app reads these files.
3.  Run the main application script:

<!-- end list -->

```bash
streamlit run app/main.py
```

This will launch the application in your default web browser, allowing you to interactively visualize key insights (e.g., boxplots of GHI, DNI, DHI, and the top regions table).

---

## 📊 Key Findings Summary

The analysis focused on comparing solar potential metrics across Benin, Sierra Leone, and Togo.

### Data Cleaning and Profiling (Task 2)

- **Outlier Management:** Outliers were proactively identified using the **Z-score method** (|Z|>3) on key columns (GHI, DNI, DHI, ModA, ModB, WS, WSgust) and removed to ensure the final statistics are robust.
- **Missing Data:** Missing values in key columns were imputed using the **median** before outlier removal.
- **Thermal Correlation:** A strong positive correlation was confirmed between solar irradiance metrics (GHI, DNI, DHI) and module temperatures (TModA, TModB), highlighting the importance of thermal management in the final installation.

### Cross-Country Comparison (Task 3)

| Metric                       | Visualization                 | Insight                                                                                                                                                           |
| :--------------------------- | :---------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GHI/DNI/DHI Distribution** | Boxplots (Colored by Country) | Visualized the mean, median, and variability of solar potential, showing which country offers the highest _average_ irradiance vs. the highest _peak_ irradiance. |
| **Statistical Significance** | One-way ANOVA (on GHI)        | Statistically tested whether the observed differences in mean GHI across the three countries were significant (p-values were noted).                              |
| **Ranking**                  | Summary Table/Bar Chart       | Provided a clear ranking based on metrics like median GHI, which serves as the core evidence for the final strategic recommendation.                              |

🖼️ Dashboard Screenshots and Visual Assets

To meet the submission guidelines, a folder has been created to house visual documentation of the deployed dashboard.File PathDescriptiondashboard_screenshots/Folder containing all visual documentation of the Streamlit application17.

dashboard_screenshots/dashboard_preview.pngA key screenshot demonstrating the usability and visual appeal of the interactive dashboard (e.g., GHI boxplot with country selection widgets)181818181818181818.

