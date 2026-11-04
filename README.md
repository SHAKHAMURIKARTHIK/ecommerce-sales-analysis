# E-commerce Sales Analysis (Developer Arena Week 4)

A simple and professional beginner-friendly Data Analysis project using Python, Pandas, and Matplotlib.

## Project goal
Explore sales records to identify top products, monthly sales trends, and high-performing regions.

## Included files
- `main.py` — documented analysis script
- `data/sales_data.csv` — dataset used by the project
- `data/sales_data_original.csv` — original dataset copy
- `visualizations/` — three generated charts
- `outputs/` — product, monthly, and region summary CSV tables
- `analysis.ipynb` — Jupyter notebook version
- `reports/project_report.pdf` — summary report
- `reference_images/` — screenshots supplied with the project prompt

## Dataset fields
`Date`, `Product`, `Quantity`, `Price`, `Customer_ID`, `Region`, `Total_Sales`

## Run the project
1. Install Python 3.10+.
2. Open a terminal in this project folder.
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python main.py
   ```
Charts and summary CSV files are written to their respective folders.

## Analysis workflow
Load CSV → validate columns → clean missing/duplicate/invalid rows → group sales → create charts → read insights.

## Key findings from this dataset
- Valid records: 100
- Total sales: 12,365,048
- Top product by sales: Laptop
- Highest-sales region: North

These are descriptive results from the provided practice dataset. The data does not include costs, profit, discounts, or returns.
