🚗 Cars24 Used Cars Data Analysis

An end-to-end Exploratory Data Analysis (EDA) project analyzing used car listings from Cars24 using Python, Pandas, and Matplotlib."

📌 Project Overview
1.The goal of this project is to clean raw, unformatted used-car market data and extract actionable insights regarding pricing trends across different fuel types, transmission modes, ownership histories, and individual car models.

Dataset: CARS24.CSV (1,084 listings spanning models from 2009 to 2021)

Tools & Libraries: Python 3, Jupyter Notebook, Pandas, Matplotlib

🛠️ Workflow & Methodology

Data Loading & Inspection: Loaded the raw CSV file into a Pandas DataFrame and inspected column data types, structure, and missing values (NaN).

Data Cleaning & Preprocessing:

1.Removed currency symbols (₹), commas (,), and non-breaking spaces (\xa0) from price columns (SELLING_PRICE, TOTAL_PRICE)

2.Converted cleaned text fields into numerical float formats for mathematical aggregation

3.Handled missing values using .dropna() before visualization

Exploratory Data Analysis (EDA) 
 Performed group-based aggregations (groupby) to compare average selling prices across categories.

Data Visualization 
Built clean, publication-ready bar charts using Matplotlib to visualize category-wise and car-wise price distributions.

📊 Key Insights & Summary
Fuel Type Impact
 Diesel vehicles command the highest average selling price at approximately ₹7,08,592, outperforming Petrol and CNG variants.

Transmission Premium 
Automatic cars average around ₹11.75 Lakh, which is more than double the average price of Manual cars (~₹5.25 Lakh).

Ownership & Outliers 
While 1st, 2nd, and 3rd owner vehicles maintain steady average prices between ₹5.5 Lakh and ₹6.2 Lakh, the 4th Owner category spikes above ₹26 Lakh due to high-end luxury car outliers in the dataset.

Car-Wise Comparison: Across individual listings, luxury sedans like the 2015 BMW 3 Series (~₹18+ Lakh) sit at the top end, while budget hatchbacks like the 2018 Renault Kwid (<₹3 Lakh) represent the entry-level segment.



🚀 How to Run This Project
1.Clone or download this repository.
2.Ensure Python and the required libraries are installed:
3.pip install pandas matplotlib notebook
4.Place CARS24.CSV in the same directory as the Jupyter Notebook (.ipynb).
5.Launch Jupyter Notebook and run all cells:
jupyter notebook


👨‍💻Author: UZER Khan  
Goal: Data Science & Machine Learning Journey 
