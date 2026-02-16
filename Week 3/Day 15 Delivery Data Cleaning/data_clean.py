import pandas as pd

# ==============================
# LOAD TAB-SEPARATED CSV (FIX)
# ==============================
df = pd.read_csv(
    "delivery_data_raw.csv",
    sep="\t",          # 🔑 THIS IS THE FIX
    encoding="latin1"
)

# Clean column names
df.columns = df.columns.str.strip()

print("✅ CSV loaded successfully")
print(df.head())
print("\nColumns:", list(df.columns))

# ==============================
# DATA CLEANING
# ==============================

# Convert numeric columns
numeric_cols = ["order_value", "delivery_time"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill missing numeric values
df["order_value"].fillna(df["order_value"].median(), inplace=True)
df["delivery_time"].fillna(df["delivery_time"].median(), inplace=True)

# Fill missing categorical values
df["payment_method"].fillna("Unknown", inplace=True)
df["delivery_status"].fillna("Unknown", inplace=True)

# ==============================
# FEATURE ENGINEERING
# ==============================

def delivery_speed(minutes):
    if minutes <= 30:
        return "Fast"
    elif minutes <= 45:
        return "Normal"
    else:
        return "Late"

df["delivery_speed"] = df["delivery_time"].apply(delivery_speed)

df["high_value_order"] = df["order_value"].apply(
    lambda x: "Yes" if x >= 500 else "No"
)

# ==============================
# SAVE CLEAN DATA
# ==============================
df.to_csv("delivery_data_cleaned.csv", index=False)

print("\n✅ Cleaned data saved as delivery_data_cleaned.csv")
