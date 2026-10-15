import pandas as pd

# BRONZE LAYER: Ingest raw data
print("Starting Bronze Layer: Ingesting raw data...")
df = pd.read_csv('data/raw_sales.csv')
print(f"Successfully loaded {len(df)} rows of raw data.")
print(df.head())
