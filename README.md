# First_Project
# NYC Street Construction Permit Analysis (Live API)

## 📊 Overview
This Python-based data pipeline automates the retrieval and analysis of real-time street construction permits from the **NYC Open Data (DOT)** database. By shifting from static CSV files to a live API integration, this tool provides an up-to-the-minute snapshot of city-wide infrastructure activity.

## 🛠️ Tech Stack
* **Python 3**
* **Pandas:** For high-performance data manipulation and cleaning.
* **Matplotlib:** For generating visual data distributions.
* **Requests:** For handling Socrata Open Data API (REST) calls.
* **IO:** For memory-efficient data stream handling.

## 🚀 Key Engineering Features
* **Dynamic Data Ingestion:** Utilizes query parameters (`$limit`) to fetch large datasets directly from the source.
* **Data Integrity:** Implements specific `dtype` declarations to prevent data corruption (e.g., maintaining Zip Code leading zeros and Permit ID consistency).
* **Robust Cleaning:** Normalizes borough naming conventions and handles missing geographic data (NaN values) to ensure visualization accuracy.
* **Automated Reporting:** Generates and exports a distribution chart (`nyc_permit_chart.png`) automatically upon execution.

## 📈 Sample Results
Based on a sample of 10,000 live records, the analysis identifies the "Construction King"—the borough currently seeing the highest volume of infrastructure permits.
