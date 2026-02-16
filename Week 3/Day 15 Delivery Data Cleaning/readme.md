📦 Day 15 – Delivery Data Cleaning (Python & Pandas)
📌 Project Overview

This project focuses on cleaning and preparing real-world delivery order data using Python and Pandas.
The goal is to transform raw, messy CSV data into a clean, analysis-ready dataset that can later be used for EDA, Power BI, or Tableau dashboards.

This mirrors real industry scenarios, including encoding issues, delimiter mismatches, and missing values.

🗂️ Dataset Description

File: delivery_data_raw.csv

Columns:

order_id

order_date

city

restaurant

customer_id

order_value

delivery_time

delivery_status

payment_method

Common Data Issues Present:

Tab-separated values instead of commas

Missing values (NaN)

Encoding problems from Excel

Mixed data types

Inconsistent delivery times

🛠️ What This Project Does
✅ Data Loading (Robust)

Handles TAB-separated CSV

Fixes Excel encoding issues

Cleans column names

✅ Data Cleaning

Converts numeric columns safely

Handles missing values using:

Median (numeric)

Default labels (categorical)

✅ Feature Engineering

Adds delivery_speed:

Fast (≤ 30 mins)

Normal (31–45 mins)

Late (> 45 mins)

Adds high_value_order flag (₹500+)

✅ Output

Saves cleaned dataset as:

delivery_data_cleaned.csv

🧠 Key Learning Outcomes

Handling real-world CSV errors

Fixing delimiter and encoding issues

Defensive data loading techniques

Feature engineering for analytics

Industry-level Pandas workflow

▶️ How to Run the Project
1️⃣ Requirements
pip install pandas

2️⃣ Run the Script
python data_clean.py

3️⃣ Output

Cleaned CSV file generated

Ready for:

Power BI

Tableau

EDA (Python)

📁 Project Structure
Day 15 Delivery Data Cleaning/
│
├── data_clean.py
├── delivery_data_raw.csv
├── delivery_data_cleaned.csv
└── README.md