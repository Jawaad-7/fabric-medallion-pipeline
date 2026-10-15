import pandas as pd

# GOLD LAYER: Create business ready aggregations
print("Starting Gold Layer: Aggregating data for business...")
df = pd.read_csv('data/silver_sales.csv')

# Aggregate data for reporting
gold_summary = df.groupby('Region').agg(
    TotalRevenue=('Total', 'sum'),
    TotalUnitsSold=('Quantity', 'sum')
).reset_index()

# Save to Gold layer
gold_summary.to_csv('data/gold_summary.csv', index=False)
print("Gold Layer complete. Business summary generated:")
print(gold_summary)
