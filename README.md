# Nigerian Energy Billing Analysis

## Overview
This project is an exploratory data analysis (EDA) of Nigerian electricity billing and payment data. The analysis focuses on understanding billing patterns, payment behaviour, tariff band performance, and arrears distribution across electricity distribution companies (DisCos). The project combines data cleaning, exploratory analysis, visualization, and an **interactive Streamlit dashboard** to demonstrate practical real-world data analysis workflows.

## Objectives
- Explore electricity billing and payment patterns
- Identify trends across different distribution companies (DisCos)
- Analyze tariff band performance and risk
- Examine arrears and billing efficiency
- Demonstrate practical data cleaning and EDA techniques
- Provide an interactive dashboard for real-time data exploration

## Features
- Data loading and preprocessing
- Data type inspection and validation
- Data cleaning and transformation
- Grouping and aggregation using Pandas
- Statistical summaries
- Visualization using Matplotlib, Seaborn, and Plotly
- **Interactive Streamlit dashboard with filters and dynamic visualizations**
- Insight generation through charts and analysis
- Included analysis report (PDF)

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

## Installation
1. Clone or download the repository.
2. Install dependencies:
```bash
   pip install -r requirements.txt
```

## Running the Project

### Jupyter Notebook Analysis
Open and run the notebook:
```bash
jupyter notebook nigerian_energy_analysis_code.ipynb
```
Run the cells sequentially to reproduce the analysis.

### Interactive Dashboard
Launch the Streamlit dashboard:
```bash
streamlit run dashboard.py
```
The dashboard will open in your browser, allowing you to:
- Filter data by distribution company and tariff band
- Select custom date ranges
- View real-time KPIs (customers, energy consumption, billing, arrears)
- Explore interactive charts across four tabs:
  - ⚡ **Consumption Pattern**: Consumption distribution and monthly trends
  - 💳 **Billing & Payments**: Billing vs payment comparisons by DisCo
  - 🚨 **Tariff Risk Analysis**: Arrears breakdown by tariff band
  - 📊 **Insights**: Key findings and recommendations

## Files Included
- `nigerian_energy_analysis_code.ipynb` - Main analysis notebook
- `dashboard.py` - Interactive Streamlit dashboard
- `Nigeria_Energy_analysis.pdf` - Detailed analysis and insights report
- `dataset.csv` - Energy billing dataset
- `requirements.txt` - Dependencies
- `README.md` - Project documentation

## Dataset
The project uses a Nigerian electricity billing and payments dataset containing:
- Distribution company (DisCo) data
- Customer IDs and billing months
- Electricity consumption (kWh)
- Amount billed and amount paid
- Tariff bands
- Arrears and financial indicators

## Analysis Included
- Data inspection and validation
- Billing trend analysis
- Average billing comparisons
- Tariff band risk analysis
- Arrears distribution analysis
- Payment ratio calculations
- Visualization of key metrics
- Interactive filtering and exploration

## Key Insights
- Electricity consumption is right-skewed—few customers consume significantly more power
- Billing amounts are relatively consistent across distribution companies
- Tariff Band C contributes the largest share of total arrears
- Payment behaviour varies more strongly by tariff band than by consumption level
- Energy usage alone does not explain outstanding arrears risk

## Author
Mayomi Tsolaye Latasha

