import pandas as pd

# SILVER LAYER: Clean and transform data
print("Starting Silver Layer: Cleaning data...")
df = pd.read_csv('data/raw_sales.csv')

# Clean the data
df = df.dropna()
df['SaleDate'] = pd.to_datetime(df['SaleDate'])
df['Total'] = df['Quantity'] * df['UnitPrice']

# Save to Silver layer
df.to_csv('data/silver_sales.csv', index=False)
print(f"Silver Layer complete. {len(df)} clean rows saved.")
