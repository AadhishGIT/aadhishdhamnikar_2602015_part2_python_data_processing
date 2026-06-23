# aadhishdhamnikar_2602015_part2_python_data_processing

# Python Data Processing Without Pandas

## Student Information

Name: Aadhish Dhamnikar

Student ID: 2602015

Repository Name:
aadhish_dhamnikar_2602015_part2_python_data_processing

---

## Project Overview

This project implements a Python-based data processing pipeline for a business order dataset without using Pandas.

The solution performs:

- CSV data loading
- Data cleaning
- Data validation
- Rejection handling
- Clean dataset generation
- Business summary report generation

---

## Dataset Description

### raw_orders.csv

Contains 60 order records.

Columns:

- order_id
- customer_id
- customer_name
- city
- product_id
- quantity
- unit_price
- order_status
- payment_method
- order_date

### product_master.csv

Contains product master information.

Columns:

- product_id
- product_name
- category
- standard_price

## Intentionally Added Data Quality Issues

1. Duplicate Order ID
2. Missing Customer Name
3. Missing City
4. Inconsistent City Spelling (Mumbi)
5. Incorrect City Casing (mumbai)
6. Extra Spaces in Customer Names
7. Incorrect Order Status Casing
8. Quantity = 0
9. Negative Quantity
10. Invalid Product ID
11. Invalid Payment Method
12. Invalid Order Status
13. Invalid Date Format
14. Unit Price Mismatch

## Assumptions

1. Product IDs must exist in product_master.csv.
2. Quantity must be greater than zero.
3. Order dates must follow YYYY-MM-DD format.
4. Only UPI, Card, Cash and NetBanking are accepted payment methods.
5. Only Completed, Pending and Cancelled are valid order statuses.
6. Unit price must exactly match the standard price in product_master.csv.
7. Duplicate order IDs are rejected.

## Screenshots

Screenshots are available in:

outputs/screenshots/

1. Program execution
2. cleaned_orders.csv
3. rejected_records.csv
4. summary_report.txt

## How To Run

1. Clone repository

2. Navigate to project folder

3. Run:

```bash
python main.py
```
