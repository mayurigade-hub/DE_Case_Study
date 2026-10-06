# Sales OLAP Case Study

A small data engineering project that creates a sample sales dataset in Parquet format and uses DuckDB to demonstrate common OLAP operations.

## Project contents

- `create_data.py` — builds the sample sales data with pandas and writes `sales.parquet` to the current directory.
- `sales.parquet` — generated dataset containing eight sample sales records.
- `olap.py` — queries the Parquet file with DuckDB and prints several OLAP analyses.

## Dataset

The dataset contains the following columns:

| Column | Description |
| --- | --- |
| `date` | Sale date (`YYYY-MM-DD`) |
| `city` | City where the sale occurred |
| `category` | Product category |
| `product` | Product sold |
| `quantity` | Number of units sold |
| `sales` | Sales amount |

The sample data covers Mumbai, Pune, and Nashik from January through April 2025.

## Requirements

- Python 3
- pandas
- pyarrow (Parquet support for pandas)
- DuckDB

Install the dependencies with:

```bash
python -m pip install pandas pyarrow duckdb
```

## Run the project

From the project directory, generate or refresh the Parquet dataset, then run the OLAP queries:

```bash
python create_data.py
python olap.py
```

`olap.py` reads `sales.parquet` from the current working directory, so run it from the project directory. The script displays:

- The original records
- Roll-up: total sales by category
- Drill-down: total sales by category and product
- Slice: Electronics records
- Dice: Mumbai Electronics records
- Overall sales and quantity aggregates
- Total sales by city

## Notes

The sample data is defined directly in `create_data.py`. Running that script overwrites `sales.parquet` with the sample records.
