# Microsoft Fabric Medallion Architecture Pipeline

## Project Overview
This project simulates a modern Data Engineering pipeline using the Medallion Architecture (Bronze, Silver, Gold), a core design pattern used in Microsoft Fabric. It demonstrates how to ingest raw data, clean and transform it, and aggregate it for business intelligence reporting.

## Architecture
*   **Bronze Layer (`bronze_ingest.py`):** Ingests raw sales data from a CSV file.
*   **Silver Layer (`silver_transform.py`):** Cleans the data, handles missing values, formats dates, and calculates new metrics (e.g., Total Sales).
*   **Gold Layer (`gold_aggregate.py`):** Aggregates the clean data to generate business ready summaries (e.g., Total Revenue by Region).

## Tech Stack
*   **Language:** Python
*   **Libraries:** Pandas
*   **Concepts:** ETL, Medallion Architecture, Data Modeling

## How to Run
Run the scripts in order:
1. `python bronze_ingest.py`
2. `python silver_transform.py`
3. `python gold_aggregate.py`
