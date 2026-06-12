import pandas as pd
import numpy as np

df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

print("="*50)
print("BUSINESS KPI SUMMARY")
print("="*50)

print(f"Total Revenue: ${df['Sales'].sum():,.2f}")
print(f"Total Profit: ${df['Profit'].sum():,.2f}")
print(f"Total Orders: {df['Order ID'].nunique()}")
print(f"Total Customers: {df['Customer ID'].nunique()}")
customer_sales = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .reset_index()
)

customer_sales["Customer Segment"] = np.where(
    customer_sales["Sales"] > 10000,
    "VIP",
    np.where(
        customer_sales["Sales"] > 5000,
        "Premium",
        "Regular"
    )
)

print("\nTOP CUSTOMERS")
print(customer_sales.sort_values(
    by="Sales",
    ascending=False
).head(20))