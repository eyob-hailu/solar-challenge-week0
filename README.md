## ☀️ Solar Data Discovery: KAIM Week 0 Challenge

[cite\_start]This repository contains the solution for the **10 Academy: Artificial Intelligence Mastery (KAIM) Week 0 Challenge**, focusing on the **Solar Data Discovery** project[cite: 2, 1]. [cite\_start]The goal is to analyze solar farm data from **Benin, Sierra Leone, and Togo** to provide strategic recommendations for **MoonLight Energy Solutions**[cite: 23, 37].

### 🎯 Business Objective

[cite\_start]The objective is to act as an Analytics Engineer for MoonLight Energy Solutions and perform a quick analysis of environmental measurements to identify **high-potential regions for solar installation**[cite: 38, 40].

---

## 📂 Repository Contents and Progress

This repository is structured to manage the project environment, conduct Exploratory Data Analysis (EDA), and document the findings. [cite\_start]**Tasks 1 and 2 are complete**[cite: 12, 13].

| Directory/File                      | Task             | Status          | Description                                                                                                                                                                                               |
| :---------------------------------- | :--------------- | :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`requirements.txt`**              | Task 1: Setup    | **Complete**    | [cite\_start]Lists all necessary Python dependencies (e.g., pandas, matplotlib, etc.)[cite: 96].                                                                                                          |
| **`.github/workflows/ci.yml`**      | Task 1: Setup    | **Complete**    | [cite\_start]GitHub Actions workflow to run `pip install -r requirements.txt` for Continuous Integration[cite: 97, 99].                                                                                   |
| **`.gitignore`**                    | Task 1: Setup    | **Complete**    | [cite\_start]Configured to ignore the **`data/`** folder and CSV files to prevent raw/cleaned data from being committed[cite: 95, 200].                                                                   |
| **`notebooks/`**                    | Task 2: EDA      | **In Progress** | [cite\_start]Contains Jupyter Notebooks for Data Profiling, Cleaning, and EDA for each country[cite: 126, 127].                                                                                           |
| **`notebooks/<country>_eda.ipynb`** | Task 2: EDA      | **Complete**    | [cite\_start]Each notebook performs **Summary Statistics**, **Outlier Detection** (using Z-scores for GHI, DNI, DHI, etc.), and **Time Series Analysis** on GHI, DNI, DHI, and Tamb[cite: 129, 132, 136]. |
| **`data/`**                         | Task 2: Cleaning | **Output**      | [cite\_start]This folder, although ignored, contains the **cleaned CSVs** (e.g., `data/benin_clean.csv`) ready for comparison[cite: 134].                                                                 |

---

## 📈 Key Data Variables Used in Analysis

[cite\_start]The analysis focuses on time-series data extracted from Solar Radiation Measurement Data[cite: 43]. The primary variables used in EDA (Task 2) include:

| Variable     | Unit              | Description                                                                                                       |
| :----------- | :---------------- | :---------------------------------------------------------------------------------------------------------------- |
| **GHI**      | $\text{W/m}^2$    | [cite\_start]**Global Horizontal Irradiance** (Total solar radiation received on a horizontal surface)[cite: 47]. |
| **DNI**      | $\text{W/m}^2$    | [cite\_start]**Direct Normal Irradiance** (Solar radiation perpendicular to the sun's rays)[cite: 48].            |
| **DHI**      | $\text{W/m}^2$    | [cite\_start]**Diffuse Horizontal Irradiance** (Scattered solar radiation)[cite: 49].                             |
| **Tamb**     | $^\circ \text{C}$ | [cite\_start]Ambient Temperature[cite: 52].                                                                       |
| **WS**       | $\text{m/s}$      | [cite\_start]Wind Speed[cite: 54].                                                                                |
| **Cleaning** | `1 or 0`          | [cite\_start]Flag signifying if a cleaning event occurred[cite: 60].                                              |

---

## ⚙️ Environment Setup

To reproduce the environment for Tasks 1 and 2:

1.  **Clone the Repository:**
    ```bash
    git clone [Your-Repo-Link]/solar-challenge-week0.git
    cd solar-challenge-week0
    ```
2.  **Set up Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate # or appropriate command for your OS/conda
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
