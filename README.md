Coffee Shop Sales Data Analysis with Python
Overview
This project analyzes sales data from a coffee shop to gain insights into customer behavior, popular products, and sales trends across different times and locations. The analysis was performed using the pandas library for data manipulation and the matplotlib library for data visualization in Python.

Business Problem
The goal of this analysis is to answer key business questions such as:

What are the peak sales hours of the day?

Are there any noticeable sales trends throughout the month?

How does sales performance compare across different store locations?

Which product categories are the most popular?

What is the best-selling item at each store location?

What is the total revenue generated?

Data Source
The data for this analysis is contained in the Coffee Shop Sales.xlsx file. This file includes information about individual transactions, such as the transaction ID, date, time, quantity, store details, product details, and unit price.

Analysis Steps
The following steps were taken to analyze the data:

Data Loading and Cleaning:

The Coffee Shop Sales.xlsx file was loaded into a pandas DataFrame.

The transaction_date and transaction_time columns were combined and converted to a datetime format.

New columns for transaction_month, transaction_day, and transaction_hour were extracted from the datetime column.

A total_sales column was calculated by multiplying the transaction_qty by the unit_price.

Exploratory Data Analysis (EDA):

The initial structure and information of the DataFrame were examined using head() and info().

Sales Analysis:

Sales by Hour: Total sales were aggregated by the hour of the day to identify peak hours. A bar chart (sales_by_hour.png) was generated to visualize these results.

Sales by Day of the Month: Total sales were aggregated by the day of the month to identify any monthly trends. A line plot (sales_by_day.png) was generated.

Sales by Store Location: Total sales were aggregated by each store location to compare their performance. A bar chart (sales_by_location.png) was generated.

Sales by Product Category: Total sales were aggregated by product category to determine the most popular categories. A bar chart (sales_by_category.png) was generated.

Best Selling Item by Location: The product with the highest total sales was identified for each store location. The results are printed in the console.

Total Sales Calculation:

The total revenue generated from all transactions was calculated.

Key Findings
The peak sales hours are between 9 AM and 10 AM.

Sales tend to fluctuate throughout the month, with a noticeable dip towards the end of the month.

Sales performance is relatively similar across all three store locations (Astoria, Hell's Kitchen, Lower Manhattan).

The most popular product categories are Coffee and Tea.

The best-selling item at each store location is Barista Espresso.

The total revenue generated from all transactions is **698,812.33**.

Code
The Python code used for this analysis is available in the analysis.py file.

How to Run the Code
Make sure you have Python installed.

Clone this repository to your local machine.

Navigate to the project directory in your terminal.

Create and activate a virtual environment (if you haven't already):
```bash
python -m venv my_venv
source my_venv/bin/activate  # On macOS and Linux

my_venv\Scripts\activate # On Windows
```

Install the required libraries:
```bash
pip install pandas matplotlib openpyxl
```

Ensure the cleaned_coffee_shop_data.csv file is in the same directory as analysis.py. If not, run the previous steps of our interactive session to generate this file from the original Coffee Shop Sales.xlsx.

Run the analysis script:
```bash
python analysis.py
```

The script will print the best-selling item by location and the total sales in the console, and it will save the generated charts as .png files in the project directory.

Next Steps (Optional)
Further analysis could explore sales trends by specific product types within categories.

Time series analysis could be performed to forecast future sales.

Customer segmentation could provide deeper insights into purchasing patterns.