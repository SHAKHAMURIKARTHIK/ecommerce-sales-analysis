# E-commerce Sales Analysis — Developer Arena Week 4

## 1. Project overview
This beginner-friendly Python project analyzes an e-commerce practice dataset to summarize sales by product, month, and region. It uses Pandas for data handling and Matplotlib for visualizations.

## 2. Objectives
- Load and validate the sales CSV.
- Clean incomplete, duplicate, or invalid records.
- Calculate total and average sales.
- Identify the highest-sales product, region, and month.
- Create charts and export summary CSV files.
- Communicate findings in a concise report.

## 3. Dataset
File: `data/sales_data.csv`  
Fields: `Date`, `Product`, `Quantity`, `Price`, `Customer_ID`, `Region`, `Total_Sales`.  
The supplied practice dataset produced 100 valid records. Results are descriptive of this dataset and do not represent a real business.

## 4. Setup and installation
Prerequisites: Python 3.10+ (regular/non-freethreaded build recommended).

From the project folder in VS Code terminal:
```bash
python -m pip install -r requirements.txt
python main.py
```
If your VS Code is using a particular interpreter, install packages through that interpreter, e.g. `py -3.13 -m pip install -r requirements.txt`, then run `py -3.13 main.py`.

## 5. Code structure
- `main.py`: data loading, validation/cleaning, grouped summaries, chart creation, CSV exports, and printed insights.
- `analysis.ipynb`: notebook version for stepwise exploration.
- `data/`: input CSV and original copy.
- `visualizations/`: generated PNG charts.
- `outputs/`: product/month/region summary CSVs.
- `reports/project_report.pdf`: project report with insights and chart evidence.
- `reference_images/`: reference images supplied with the task prompt (not needed to execute).
- `screenshots/`: documentation evidence directory.

## 6. Analysis workflow
CSV input → validate required fields → parse dates/numbers → remove incomplete/duplicate and invalid rows → group sales by product/month/region → visualize → export summaries → interpret results.

## 7. Findings
- Valid records analyzed: **100**
- Total sales: **12,365,048.00**
- Average sales per record: **123,650.48**
- Top-selling product: **Laptop (3,889,210.00)**
- Highest-sales region: **North (3,983,635.00)**
- Strongest month: **2024-03 (4,485,006.00)**

## 8. Technical requirements met
- Python used for scripting and reproducible execution.
- Pandas used to read CSV, clean values, group, aggregate, and export tables.
- Matplotlib used to create product, monthly trend, and region charts.
- `pathlib` resolves project-relative paths so execution is not dependent on the current terminal directory.
- Outputs are generated in organized folders (`visualizations/`, `outputs/`).

## 9. Screenshots of working application
The generated chart PNGs in `visualizations/` are the project’s visual output evidence. Open them in VS Code Explorer by expanding `visualizations` and double-clicking each PNG. Add a screenshot of your VS Code terminal showing the summary after running `main.py` to `screenshots/` before submission if your evaluator specifically requires a literal application screenshot.

## 10. Limitations
The dataset does not include cost, profit, discount, refund, or return data. Therefore, the project analyzes sales value, not profitability.
