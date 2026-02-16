import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# LOAD CLEANED DATA
# ==============================
df = pd.read_csv("delivery_data_cleaned.csv")

print("\n✅ Data Loaded Successfully\n")
print(df.head())
print("\nData Info:")
print(df.info())



total_revenue = df["order_value"].sum()
avg_order_value = df["order_value"].mean()

print("\n📊 BASIC METRICS")
print("Total Revenue:", round(total_revenue, 2))
print("Average Order Value:", round(avg_order_value, 2))

# ==============================
# REVENUE ANALYSIS
# ==============================
city_revenue = df.groupby("city")["order_value"].sum().sort_values(ascending=False)
city_revenue_pct = (city_revenue / total_revenue) * 100

print("\n🏙️ Revenue by City")
print(city_revenue)

print("\n📈 Revenue Contribution (%)")
print(city_revenue_pct.round(2))

# ==============================
# DELIVERY PERFORMANCE
# ==============================
avg_delivery_city = df.groupby("city")["delivery_time"].mean().sort_values()
print("\n⏱️ Average Delivery Time by City")
print(avg_delivery_city.round(2))

late_rate_city = (
    df[df["delivery_speed"] == "Late"]
    .groupby("city")
    .size()
    / df.groupby("city").size()
) * 100

print("\n🚨 Late Delivery Rate (%) by City")
print(late_rate_city.round(2))

# ==============================
# RESTAURANT EFFICIENCY
# ==============================
restaurant_perf = df.groupby("restaurant").agg(
    total_revenue=("order_value", "sum"),
    avg_delivery_time=("delivery_time", "mean"),
    late_orders=("delivery_speed", lambda x: (x == "Late").sum())
).sort_values("total_revenue", ascending=False)

print("\n🍽️ Restaurant Performance")
print(restaurant_perf.round(2))

# ==============================
# HIGH VALUE ORDER ANALYSIS
# ==============================
high_value_revenue = df[df["high_value_order"] == "Yes"]["order_value"].sum()
high_value_pct = (high_value_revenue / total_revenue) * 100

print("\n💰 High Value Orders Contribution")
print("Revenue % from High Value Orders:", round(high_value_pct, 2))

print("\n⏱️ Delivery Time vs Order Value")
print(df.groupby("high_value_order")["delivery_time"].mean().round(2))

# ==============================
# PAYMENT METHOD INSIGHTS
# ==============================
payment_counts = df["payment_method"].value_counts()
payment_delay = df.groupby("payment_method")["delivery_time"].mean()

print("\n💳 Payment Method Usage")
print(payment_counts)

print("\n⏱️ Avg Delivery Time by Payment Method")
print(payment_delay.round(2))

# ==============================
# VISUALIZATIONS
# ==============================
sns.set(style="whitegrid")

# Revenue by City
plt.figure(figsize=(8,5))
sns.barplot(x=city_revenue.index, y=city_revenue.values)
plt.title("Total Revenue by City")
plt.ylabel("Revenue")
plt.xlabel("City")
plt.show()

# Late Delivery Rate by City
plt.figure(figsize=(8,5))
sns.barplot(x=late_rate_city.index, y=late_rate_city.values)
plt.title("Late Delivery Rate (%) by City")
plt.ylabel("Percentage")
plt.xlabel("City")
plt.show()

# Restaurant Revenue vs Delivery Time
plt.figure(figsize=(8,5))
sns.scatterplot(
    data=restaurant_perf,
    x="avg_delivery_time",
    y="total_revenue",
    size="late_orders",
    legend=False
)
plt.title("Restaurant Revenue vs Delivery Time")
plt.xlabel("Avg Delivery Time")
plt.ylabel("Total Revenue")
plt.show()

# Payment Method Distribution
plt.figure(figsize=(6,6))
payment_counts.plot.pie(autopct="%1.1f%%")
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.show()

print("\n✅ Day 16 EDA Completed Successfully")
