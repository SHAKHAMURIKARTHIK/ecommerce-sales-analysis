"""E-commerce Sales Analysis | Beginner-friendly, professional project."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Keep paths relative to this project, so it runs from any working directory.
PROJECT_FOLDER = Path(__file__).resolve().parent
DATA_FILE = PROJECT_FOLDER / "data" / "sales_data.csv"
CHART_FOLDER = PROJECT_FOLDER / "visualizations"
OUTPUT_FOLDER = PROJECT_FOLDER / "outputs"
CHART_FOLDER.mkdir(exist_ok=True)
OUTPUT_FOLDER.mkdir(exist_ok=True)


def load_and_clean_data(file_path):
    """Read the CSV, validate columns, and remove invalid/duplicate records."""
    df = pd.read_csv(file_path)

    required_columns = [
        "Date", "Product", "Quantity", "Price",
        "Customer_ID", "Region", "Total_Sales"
    ]
    missing_columns = [column for column in required_columns if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Dataset is missing columns: {missing_columns}")

    # Convert values into useful data types.
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for column in ["Quantity", "Price", "Total_Sales"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    for column in ["Product", "Customer_ID", "Region"]:
        df[column] = df[column].astype("string").str.strip()

    # Remove incomplete rows and duplicates; exclude impossible values.
    df = df.dropna(subset=required_columns).drop_duplicates()
    df = df[(df["Quantity"] > 0) & (df["Price"] >= 0) & (df["Total_Sales"] >= 0)]
    if df.empty:
        raise ValueError("No valid records were found after cleaning.")

    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    return df


def analyze_sales(df):
    """Create summary tables, charts, and a few descriptive business insights."""
    product_sales = (df.groupby("Product", as_index=False)["Total_Sales"].sum()
                     .sort_values("Total_Sales", ascending=False))
    monthly_sales = (df.groupby("Month", as_index=False)["Total_Sales"].sum()
                     .sort_values("Month"))
    region_sales = (df.groupby("Region", as_index=False)["Total_Sales"].sum()
                    .sort_values("Total_Sales", ascending=False))

    # Chart 1: Compare total sales across products.
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(product_sales["Product"], product_sales["Total_Sales"])
    ax.set_title("Total Sales by Product")
    ax.set_xlabel("Product")
    ax.set_ylabel("Total Sales")
    ax.tick_params(axis="x", rotation=20)
    fig.tight_layout()
    fig.savefig(CHART_FOLDER / "sales_by_product.png", dpi=160)
    plt.close(fig)

    # Chart 2: View sales movement month by month.
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(monthly_sales["Month"], monthly_sales["Total_Sales"], marker="o")
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Sales")
    ax.grid(True, alpha=0.25)
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(CHART_FOLDER / "monthly_sales_trend.png", dpi=160)
    plt.close(fig)

    # Chart 3: Show each region's share of total sales.
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.pie(region_sales["Total_Sales"], labels=region_sales["Region"],
           autopct="%1.1f%%", startangle=90)
    ax.set_title("Sales Distribution by Region")
    fig.tight_layout()
    fig.savefig(CHART_FOLDER / "sales_by_region.png", dpi=160)
    plt.close(fig)

    # Save tables as CSV files for further review.
    product_sales.to_csv(OUTPUT_FOLDER / "sales_by_product.csv", index=False)
    monthly_sales.to_csv(OUTPUT_FOLDER / "monthly_sales.csv", index=False)
    region_sales.to_csv(OUTPUT_FOLDER / "sales_by_region.csv", index=False)

    total_sales = df["Total_Sales"].sum()
    best_product = product_sales.iloc[0]
    best_region = region_sales.iloc[0]
    best_month = monthly_sales.loc[monthly_sales["Total_Sales"].idxmax()]

    print("\n========== E-COMMERCE SALES SUMMARY ==========")
    print(f"Valid records analyzed : {len(df):,}")
    print(f"Total sales            : {total_sales:,.2f}")
    print(f"Average sales / record : {df['Total_Sales'].mean():,.2f}")
    print(f"Top-selling product    : {best_product['Product']} ({best_product['Total_Sales']:,.2f})")
    print(f"Highest-sales region   : {best_region['Region']} ({best_region['Total_Sales']:,.2f})")
    print(f"Strongest month        : {best_month['Month']} ({best_month['Total_Sales']:,.2f})")
    print("\nCharts saved in: visualizations/")
    print("Summary CSVs saved in: outputs/")

    return product_sales, monthly_sales, region_sales


if __name__ == "__main__":
    sales_data = load_and_clean_data(DATA_FILE)
    analyze_sales(sales_data)
