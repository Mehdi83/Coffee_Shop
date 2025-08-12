import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_excel('Coffee Shop Sales.xlsx')
    print("Data loaded successfully.")

    # Data cleaning and feature engineering
    df['transaction_datetime'] = pd.to_datetime(df['transaction_date'].astype(str) + ' ' + df['transaction_time'].astype(str))
    df['transaction_month'] = df['transaction_datetime'].dt.month
    df['transaction_day'] = df['transaction_datetime'].dt.day
    df['transaction_hour'] = df['transaction_datetime'].dt.hour
    df['total_sales'] = df['transaction_qty'] * df['unit_price']
    print("Data has been cleaned and new features added.")
    print(df.head())

    # Data analysis and visualization
    sales_by_hour = df.groupby('transaction_hour')['total_sales'].sum()
    plt.figure(figsize=(10, 6))
    sales_by_hour.plot.bar()
    plt.title('Total Sales by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Total Sales')
    plt.savefig('sales_by_hour.png')
    plt.close()
    print("Chart 'sales_by_hour.png' saved.")

    sales_by_day = df.groupby('transaction_day')['total_sales'].sum()
    plt.figure(figsize=(12, 6))
    sales_by_day.plot(kind='line')
    plt.title('Total Sales by Day of the Month')
    plt.xlabel('Day of the Month')
    plt.ylabel('Total Sales')
    plt.savefig('sales_by_day.png')
    plt.close()
    print("Chart 'sales_by_day.png' saved.")

    sales_by_location = df.groupby('store_location')['total_sales'].sum()
    plt.figure(figsize=(8, 6))
    sales_by_location.plot.bar()
    plt.title('Total Sales by Store Location')
    plt.xlabel('Store Location')
    plt.ylabel('Total Sales')
    plt.savefig('sales_by_location.png')
    plt.close()
    print("Chart 'sales_by_location.png' saved.")

    # Save the cleaned dataframe for future use
    df.to_csv('cleaned_coffee_shop_data.csv', index=False)
    print("Cleaned data saved to 'cleaned_coffee_shop_data.csv'.")

except FileNotFoundError:
    print("Error: The file 'Coffee Shop Sales.xlsx' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


    