# E-Commerce Customer Orders Analysis

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Dataset (30 rows)
data = {
    "Order_ID": range(5001,5031),

    "Customer_Name":[
        "Ali","Sara","Ahmed","Fatima","Bilal","Ayesha",
        "Usman","Hira","Hamza","Noor","Zain","Maryam",
        "Abdullah","Sana","Daniyal","Iqra","Farhan",
        "Laiba","Kashif","Mahnoor","Ali","Sara",
        "Ahmed","Fatima","Bilal","Ayesha","Usman",
        "Hira","Hamza","Noor"
    ],

    "City":[
        "Karachi","Lahore","Islamabad","Karachi","Multan",
        "Lahore","Peshawar","Quetta","Karachi","Islamabad",
        "Multan","Lahore","Peshawar","Karachi","Quetta",
        "Islamabad","Karachi","Lahore","Multan","Peshawar",
        "Karachi","Lahore","Islamabad","Karachi","Multan",
        "Lahore","Peshawar","Quetta","Karachi","Islamabad"
    ],

    "Product":[
        "Laptop","Phone","Tablet","Headphones","Mouse",
        "Keyboard","Monitor","Printer","Laptop","Phone",
        "Tablet","Mouse","Keyboard","Laptop","Printer",
        "Monitor","Phone","Laptop","Tablet","Mouse",
        "Keyboard","Laptop","Phone","Tablet","Printer",
        "Laptop","Monitor","Mouse","Phone","Keyboard"
    ],

    "Category":[
        "Electronics","Electronics","Electronics","Accessories","Accessories",
        "Accessories","Electronics","Electronics","Electronics","Electronics",
        "Electronics","Accessories","Accessories","Electronics","Electronics",
        "Electronics","Electronics","Electronics","Electronics","Accessories",
        "Accessories","Electronics","Electronics","Electronics","Electronics",
        "Electronics","Electronics","Accessories","Electronics","Accessories"
    ],

    "Price":[
        120000,80000,60000,8000,3000,
        5000,45000,35000,118000,82000,
        62000,3200,5200,121000,34000,
        46000,81000,119000,61000,3500,
        5400,122000,83000,60500,34500,
        123000,45500,3300,84000,5600
    ],

    "Quantity":[
        1,2,1,3,5,
        2,1,1,1,2,
        2,4,2,1,1,
        2,1,1,2,3,
        2,1,1,2,1,
        1,3,2,1,4
    ],

    "Payment_Method":[
        "Card","Cash","Online","Card","Cash",
        "Online","Card","Cash","Online","Card",
        "Cash","Online","Card","Cash","Online",
        "Card","Cash","Online","Card","Cash",
        "Online","Card","Cash","Online","Card",
        "Cash","Online","Card","Cash","Online"
    ],

    "Order_Status":[
        "Delivered","Delivered","Cancelled","Delivered","Delivered",
        "Pending","Delivered","Delivered","Cancelled","Delivered",
        "Delivered","Pending","Delivered","Delivered","Cancelled",
        "Delivered","Delivered","Pending","Delivered","Delivered",
        "Cancelled","Delivered","Delivered","Pending","Delivered",
        "Delivered","Cancelled","Delivered","Pending","Delivered"
    ],

    "Customer_Rating":[
        5,4,4,5,4,
        3,5,4,5,4,
        5,3,4,5,4,
        5,4,5,4,3,
        4,5,4,5,4,
        5,4,3,5,4
    ]
}

df = pd.DataFrame(data)

df

# 1.EDA

df.head()

df.tail()

df.info()

df.shape

df.columns

df.describe()

df.isnull().sum()

df.duplicated().sum()

# 2.Create a new column: Total_Amount = Price × Quantity
Total_Amount = df['Price'] * df['Quantity']
df['Total_Amount'] = Total_Amount
df

# 3.Analysis

# Highest order and lowest order
highest_order = df[df['Total_Amount'] == df['Total_Amount'].max()]
lowest_order = df[df['Total_Amount'] == df['Total_Amount'].min()]

print("Highest Order:")
print(highest_order)
print("\nLowest Order:")
print(lowest_order)

# Total Revenue
Total_revenue = df['Total_Amount'].sum()
print("Total Revenue:", Total_revenue)

# Average Revenue
Average_revenue = df['Total_Amount'].mean()
print("Average Revenue:", Average_revenue) 

# Average Rating
Average_Rating = df['Customer_Rating'].mean()
print("Average Rating:", Average_Rating)

# Total Quantity Sold
Total_Quantity_Sold = df['Quantity'].sum()
print("Total Quantity Sold:", Total_Quantity_Sold)

# Average Price
Average_Price = df['Price'].mean()
print("Average Price:", Average_Price)

# 4.GroupBy

# Revenue by City
revenue_by_city = df.groupby('City')['Total_Amount'].sum()
print("Revenue by City:")
print(revenue_by_city)

# Revenue by Product
revenue_by_product = df.groupby('Product')['Total_Amount'].sum()
print("\nRevenue by Product:")
print(revenue_by_product)

# Revenue by Category
revenue_by_category = df.groupby('Category')['Total_Amount'].sum()
print("\nRevenue by Category:")
print(revenue_by_category)

# Average Rating by Product
average_rating_by_product = df.groupby('Product')['Customer_Rating'].mean()
print("\nAverage Rating by Product:")
print(average_rating_by_product)

# Average Rating by City
average_rating_by_city = df.groupby('City')['Customer_Rating'].mean()
print("\nAverage Rating by City:")
print(average_rating_by_city)

# Quantity by Product
quantity_by_product = df.groupby('Product')['Quantity'].sum()
print("\nQuantity by Product:")
print(quantity_by_product)

# Orders by Payment Method
orders_by_payment_method = df['Payment_Method'].value_counts()
print("\nOrders by Payment Method:")
print(orders_by_payment_method)

# Orders by Order Status
orders_by_order_status = df['Order_Status'].value_counts()
print("\nOrders by Order Status:")
print(orders_by_order_status)

# 5.Charts

# Bar Chart
df.groupby('City')['Total_Amount'].sum().plot(kind='bar', figsize=(10, 6))
plt.xlabel('City')
plt.ylabel('Total Amount')
plt.title('Total Amount by City')
plt.show()

# Pie Chart
df['Order_Status'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
plt.title('Order Status Distribution')
plt.ylabel('')
plt.show()

# Histogram
df['Total_Amount'].plot(kind='hist', bins=20, figsize=(10, 6))
plt.xlabel('Total Amount')
plt.ylabel('Frequency')
plt.title('Distribution of Total Amount')
plt.show()

# Scatter Plot
df.plot(kind='scatter', x='Price', y='Quantity', figsize=(10, 6))
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.title('Price vs Quantity')
plt.show()

# Line Chart
df.plot(kind='line', x='Order_ID', y='Total_Amount', figsize=(10, 6))
plt.xlabel('Order ID')
plt.ylabel('Total Amount')
plt.title('Total Amount Over Order ID')
plt.show()

# Box Plot
df.boxplot(column='Total_Amount', by='City', figsize=(10, 6))
plt.xlabel('City')
plt.ylabel('Total Amount')
plt.title('Distribution of Total Amount by City')
plt.xticks(rotation=45)
plt.show()

# Pair Plot
sns.pairplot(df, hue='City')
plt.suptitle('Pair Plot of Numerical Variables', y=1.02)
plt.show()

# hexbin plot
df.plot(kind='hexbin', x='Price', y='Quantity', gridsize=20, figsize=(10, 6))
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.title('Hexbin Plot of Price vs Quantity')

# 6️.Business Questions

# Which city generated the highest revenue?
highest_revenue_city = df.groupby('City')['Total_Amount'].sum().idxmax()
print("City with the Highest Revenue:", highest_revenue_city)

# Which product earned the highest revenue?
highest_revenue_product = df.groupby('Product')['Total_Amount'].sum().idxmax()
print("Product with the Highest Revenue:", highest_revenue_product)

# Which category earned the most money?
highest_revenue_category = df.groupby('Category')['Total_Amount'].sum().idxmax()
print("Category with the Highest Revenue:", highest_revenue_category)

# Which payment method is most popular?
most_popular_payment_method = df['Payment_Method'].value_counts().idxmax()
print("Most Popular Payment Method:", most_popular_payment_method)

# How many orders were cancelled?
cancelled_orders = (df['Order_Status'] == 'Cancelled').sum()
print("Number of Cancelled Orders:", cancelled_orders)

# Which customer spent the most?
most_spent_customer = df.groupby('Customer_Name')['Total_Amount'].sum().idxmax()
print("Customer who Spent the Most:", most_spent_customer)

# Which product sold the highest quantity?
highest_quantity_product = df.groupby('Product')['Quantity'].sum().idxmax()
print("Product with the Highest Quantity Sold:", highest_quantity_product)

# Which product has the highest average rating?
highest_rated_product = df.groupby('Product')['Customer_Rating'].mean().idxmax()
print("Product with the Highest Average Rating:", highest_rated_product)

# Manager's Report
* Laptop sales generated the highest revenue.
* Karachi contributed the largest share of sales.
* Card payments were the most common payment method.
* highest revenue city is Karachi
* cancelled orders were 5

# 8.Export
df.to_csv("Ecommerce-Customer-Orders-Analysis.csv", index=False)
