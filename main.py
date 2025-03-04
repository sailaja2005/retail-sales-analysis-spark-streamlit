#!/usr/bin/env python
# coding: utf-8

from pyspark.sql import SparkSession
import streamlit as st
from pyspark.sql import functions as F  # Unified import

# Initialize Spark session
spark = SparkSession.builder.appName('Retail').getOrCreate()

# Load dataset
df = spark.read.csv('superstore.csv', header=True, inferSchema=True)
df.show(5)

# 1. Total Customers
total_customers = df.select(F.countDistinct('Customer_id').alias('Total Customers')).collect()[0][0]

# 2. Total Orders
total_orders = df.select(F.countDistinct('Order_id').alias('Total Orders')).collect()[0][0]

# 3. Total Sales
total_sales = df.agg(F.sum('Sales').alias('Total Sales')).collect()[0][0]

# 4. Total Profit
total_profit = df.agg(F.sum('Profit').alias('Total Profit')).collect()[0][0]

# 5. Top Sales by Country
top_sales_by_country = df.groupBy('Country').agg(F.sum('Sales').alias('Total Sales')).orderBy(F.desc('Total Sales'))

# 6. Most Profitable Region
region = df.groupby('Region').agg(F.sum('Profit').alias('Profits_region_wise'))
most_profitable_region = region.orderBy(F.desc('Profits_region_wise')).limit(1).collect()[0][0]

# 7. Most Profitable Country
country_profit = df.groupby('Country').agg(F.sum('Profit').alias('Profits_country_wise'))
most_profitable_country = country_profit.orderBy(F.desc('Profits_country_wise')).limit(1).collect()[0][0]

# 8. Top Sales Category Products
top_sales_category_products = df.groupBy("Category").agg(F.sum("Sales").alias("Total Sales")).orderBy(F.desc("Total Sales")).limit(1).collect()[0][0]

# 9. Top 10 Sales Sub-Category Products
top10_sales_products = df.groupBy('Sub_Category').agg(F.sum('Sales').alias('Total Sales')).orderBy(F.desc('Total Sales')).limit(10)

# 10. Most Ordered Quantity Product
most_ordered_products = df.groupby("Product_Name").agg(F.sum("Quantity").alias("Total Quantity")).orderBy(F.desc("Total Quantity")).limit(10)

# 11. Top Customer Based on Sales
top_customer = df.groupby('Customer_Name', 'City').agg(F.sum('Sales').alias('Total Sales')).orderBy(F.desc('Total Sales')).limit(10)

# Streamlit Dashboard
st.title('Retail Sales Dashboard')

# Display key metrics
st.subheader('Key Metrics')
st.write(f'Total Customers: {total_customers}')
st.write(f'Total Orders: {total_orders}')
st.write(f'Total Sales: ${total_sales:,.2f}')
st.write(f'Total Profit: ${total_profit:,.2f}')

# Display top sales by country
st.subheader('Top Sales by Country')
st.dataframe(top_sales_by_country.toPandas())

# Display most ordered products
st.subheader('Top 10 Most Ordered Products')
st.dataframe(most_ordered_products.toPandas())

# Display top customers
st.subheader('Top Customers Based on Sales')
st.dataframe(top_customer.toPandas())

# Display top sales sub-category
st.subheader('Top 10 Sales Sub-Category Products')
st.dataframe(top10_sales_products.toPandas())
import matplotlib.pyplot as plt

# Top Sales by Category Bar Chart
st.subheader("Top Sales by Category")

category_sales = df.groupBy("Category").agg(F.sum("Sales").alias("Total Sales")).toPandas()
st.bar_chart(category_sales.set_index("Category"))


