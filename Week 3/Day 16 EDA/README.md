# 📊 Day 16 – Delivery App Exploratory Data Analysis (EDA)

## 📌 Project Overview
This project performs Exploratory Data Analysis (EDA) on a food delivery dataset to understand delivery performance, customer behavior, payment trends, and data quality issues.

The analysis simulates real-world delivery app analytics similar to platforms like Swiggy, Zomato, and Uber Eats.

---

## 📂 Dataset
**File:** `delivery_data_cleaned.csv`

### Columns:
- `order_id` – Unique order identifier  
- `order_date` – Date of order  
- `city` – Delivery city  
- `restaurant` – Restaurant name  
- `customer_id` – Customer ID  
- `order_value` – Total order amount  
- `delivery_time` – Delivery time in minutes  
- `delivery_status` – Delivered / Late  
- `payment_method` – UPI / Card / Cash  
- `delivery_speed` – Fast / Normal / Late  
- `high_value_order` – Yes / No  

---

## 🎯 Objectives
- Inspect dataset structure and quality  
- Identify missing values and inconsistencies  
- Analyze delivery performance  
- Detect high-value orders  
- Prepare data for visualization tools  

---

## 🛠️ Tools & Libraries
- Python  
- Pandas  
- Matplotlib  
- VS Code  

---

## 🔍 EDA Steps Performed

### 1. Data Loading
- Loaded cleaned CSV file
- Displayed sample rows
- Verified column names and data types

### 2. Data Quality Checks
- Checked null values
- Verified dataset size
- Reviewed memory usage

### 3. Missing Value Handling
- Numerical columns filled using **median**
- Categorical columns filled using **mode**
- Ensured dataset consistency after cleaning

### 4. Feature Analysis
- Delivery speed classification
- High-value order identification
- Payment method distribution
- City-wise delivery trends

---

## ⚠️ Key Insight
Real-world datasets always contain missing values.  
Instead of stopping execution, missing data was:
- Detected
- Reported
- Cleaned using analytical best practices

This reflects industry-standard EDA workflows.

---

## ▶️ How to Run

### Install dependencies
```bash
pip install pandas matplotlib
