import streamlit as st
import pandas as pd

# Load the cleaned data you saved from the first project
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_coffee_shop_data.csv')
    return df

df = load_data()

# --- Dashboard Components ---

st.title('Coffee Shop Sales Dashboard')
st.markdown('A simple interactive dashboard to analyze sales data from our coffee shops.')

st.divider()

# Display the total sales amount
total_sales_amount = df['total_sales'].sum()
st.metric(label="Total Revenue", value=f"${total_sales_amount:,.2f}")

st.divider()

# Interactive element: Filter data by store location
st.header('Sales Analysis by Location')
store_location_list = df['store_location'].unique()
selected_location = st.selectbox('Select a Store Location', store_location_list)

# Filter the dataframe based on the selected location
filtered_df = df[df['store_location'] == selected_location]

# Display a chart for the filtered data
st.subheader(f'Daily Sales for {selected_location}')
daily_sales = filtered_df.groupby('transaction_day')['total_sales'].sum()
st.line_chart(daily_sales)

st.divider()

# Display charts for all locations (from your original analysis)
st.header('Overall Sales Trends')

st.subheader('Total Sales by Hour of Day')
sales_by_hour = df.groupby('transaction_hour')['total_sales'].sum()
st.bar_chart(sales_by_hour)

st.subheader('Total Sales by Day of the Month')
sales_by_day = df.groupby('transaction_day')['total_sales'].sum()
st.line_chart(sales_by_day)


