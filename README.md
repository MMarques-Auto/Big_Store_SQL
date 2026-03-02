# Big Store SQL – Data Analysis with Python and SQLite

## Project Overview
This project simulates a simple Business Intelligence (BI) solution for a retail store. It creates a SQLite database from scratch, populates it with sample sales data, and runs SQL queries to extract business insights using Python.

The goal is to demonstrate how Python can be used to automate database creation, data insertion, and report generation.

## Files
- `CreateDB.py` – Creates the SQLite database (`ecommerce.db`), defines tables (products, customers, sales), and inserts sample data.
- `Relatorios.py` – Queries the database and prints business reports: total sales, top products, customer purchase history.

## Example Reports Generated
- Total revenue by product
- Top 5 best-selling items
- Customer purchase summary

## Tech Stack
- Python 3
- SQLite3
- Pandas (optional for future enhancements)

## How to Run
1. Clone the repository
2. Run `python CreateDB.py` to build and populate the database
3. Run `python Relatorios.py` to see the reports

## Next Steps (Ideas)
- Add data visualization with Matplotlib or Streamlit
- Connect to a real PostgreSQL database
- Turn into a web dashboard
