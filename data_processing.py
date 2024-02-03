#!/usr/bin/env python
# coding: utf-8

# In[2]:


# data_processing.ipynb

import pandas as pd

def read_and_clean_data(file_path):
    # Read data from CSV file
    data = pd.read_csv(file_path, encoding='ISO-8859-1')

    # Convert 'Order Date' and 'Ship Date' to datetime format
    data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
    data['Ship Date'] = pd.to_datetime(data['Ship Date'], errors='coerce')

    # Fill missing values in the 'Order Priority' column with 'Not Specified'
    data['Order Priority'].fillna('Not Specified', inplace=True)

    return data

def compute_profit_by_category(data):
    # Compute profit by product category
    profit_by_category = data.groupby('Product Category')['Profit'].sum()

    return profit_by_category

def calculate_total_sales(data):
    # Calculate total sales
    total_sales = data['Sales'].sum()

    return total_sales

def identify_high_priority_orders(data):
    # Identify high-priority orders
    high_priority_orders = data[data['Order Priority'] == 'High']

    return high_priority_orders

# Additional tasks:

def compute_total_revenue_by_month(data):
    # Extract month and year from 'Order Date'
    data['order_month'] = data['Order Date'].dt.to_period('M')

    # Compute total revenue by month
    total_revenue_by_month = data.groupby('order_month')['Unit Price'].sum()

    return total_revenue_by_month

def compute_total_revenue_by_product(data):
    # Compute total revenue by product
    total_revenue_by_product = data.groupby('Product Name')['Unit Price'].sum()

    return total_revenue_by_product

def compute_total_revenue_by_customer(data):
    # Compute total revenue by customer
    total_revenue_by_customer = data.groupby('Customer ID')['Unit Price'].sum()

    return total_revenue_by_customer

def identify_top_10_customers(data):
    # Identify top 10 customers by revenue
    top_10_customers = data.groupby('Customer ID')['Unit Price'].sum().nlargest(10)

    return top_10_customers

if __name__ == "__main__":
    # Read and clean data
    orders_data = read_and_clean_data(r'D:\\Users\\Keerthana\\Downloads\\Orders.csv')

    # Compute profit by product category
    profit_by_category = compute_profit_by_category(orders_data)
    print("Profit by Product Category:\n", profit_by_category)

    # Calculate total sales
    total_sales = calculate_total_sales(orders_data)
    print("\nTotal Sales:", total_sales)

    # Identify high-priority orders
    high_priority_orders = identify_high_priority_orders(orders_data)
    print("\nHigh Priority Orders:\n", high_priority_orders)

    # Additional tasks:
    # Compute total revenue by month
    total_revenue_by_month = compute_total_revenue_by_month(orders_data)
    print("\nTotal Revenue by Month:\n", total_revenue_by_month)

    # Compute total revenue by product
    total_revenue_by_product = compute_total_revenue_by_product(orders_data)
    print("\nTotal Revenue by Product:\n", total_revenue_by_product)

    # Compute total revenue by customer
    total_revenue_by_customer = compute_total_revenue_by_customer(orders_data)
    print("\nTotal Revenue by Customer:\n", total_revenue_by_customer)

    # Identify top 10 customers by revenue
    top_10_customers = identify_top_10_customers(orders_data)
    print("\nTop 10 Customers by Revenue:\n", top_10_customers)


# In[ ]:




