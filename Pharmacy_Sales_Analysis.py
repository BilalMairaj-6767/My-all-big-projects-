import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = {
    "Bill_ID": range(7001, 7031),

    "Customer_Name": [
        "Ali","Sara","Ahmed","Fatima","Bilal",
        "Ayesha","Usman","Hira","Hamza","Noor",
        "Zain","Maryam","Abdullah","Sana","Daniyal",
        "Iqra","Farhan","Laiba","Kashif","Mahnoor",
        "Ali","Sara","Ahmed","Fatima","Bilal",
        "Ayesha","Usman","Hira","Hamza","Noor"
    ],

    "City": [
        "Karachi","Lahore","Islamabad","Karachi","Multan",
        "Lahore","Peshawar","Quetta","Karachi","Islamabad",
        "Multan","Lahore","Peshawar","Karachi","Quetta",
        "Islamabad","Karachi","Lahore","Multan","Peshawar",
        "Karachi","Lahore","Islamabad","Karachi","Multan",
        "Lahore","Peshawar","Quetta","Karachi","Islamabad"
    ],

    "Medicine": [
        "Panadol","Augmentin","Brufen","Paracetamol","Vitamin C",
        "Panadol","Cough Syrup","Brufen","Insulin","Vitamin D",
        "Panadol","Augmentin","Paracetamol","Insulin","Vitamin C",
        "Cough Syrup","Panadol","Vitamin D","Brufen","Paracetamol",
        "Insulin","Vitamin C","Panadol","Augmentin","Brufen",
        "Paracetamol","Vitamin D","Panadol","Cough Syrup","Insulin"
    ],

    "Category": [
        "Pain Relief","Antibiotic","Pain Relief","Pain Relief","Supplements",
        "Pain Relief","Cold & Flu","Pain Relief","Diabetes","Supplements",
        "Pain Relief","Antibiotic","Pain Relief","Diabetes","Supplements",
        "Cold & Flu","Pain Relief","Supplements","Pain Relief","Pain Relief",
        "Diabetes","Supplements","Pain Relief","Antibiotic","Pain Relief",
        "Pain Relief","Supplements","Pain Relief","Cold & Flu","Diabetes"
    ],

    "Unit_Price": [
        120,850,180,90,450,
        130,320,190,2500,600,
        125,870,95,2550,470,
        330,135,620,185,100,
        2600,480,140,890,195,
        110,640,145,340,2650
    ],

    "Quantity": [
        5,2,6,10,3,
        4,2,5,1,2,
        6,2,8,1,4,
        3,5,2,7,9,
        1,3,6,2,4,
        8,2,5,3,1
    ],

    "Payment_Method": [
        "Cash","Card","Online","Cash","Card",
        "Online","Cash","Card","Online","Cash",
        "Card","Online","Cash","Card","Online",
        "Cash","Card","Online","Cash","Card",
        "Online","Cash","Card","Online","Cash",
        "Card","Online","Cash","Card","Online"
    ],

    "Pharmacist": [
        "Ahmed","Sara","Bilal","Usman","Ahmed",
        "Sara","Bilal","Usman","Ahmed","Sara",
        "Bilal","Usman","Ahmed","Sara","Bilal",
        "Usman","Ahmed","Sara","Bilal","Usman",
        "Ahmed","Sara","Bilal","Usman","Ahmed",
        "Sara","Bilal","Usman","Ahmed","Sara"
    ]
}

df = pd.DataFrame(data)

df

# 1.EDA

df.head()

df.tail()

df.shape

df.columns

df.info()

df.describe()

df.duplicated().sum()

df.isnull().sum()

# 2.Create New Column : Total_Bill = Unit_Price × Quantity
df['Total_Bill'] = df['Unit_Price'] * df['Quantity']
df

# 3.Analysis

# Highest Total Bill, Lowest Total Bill, Highest Unit Price, Lowest Unit Price, Highest Quantity, Lowest Quantity
highest_total_bill = df['Total_Bill'].max()
lowest_total_bill = df['Total_Bill'].min()
highest_unit_price = df['Unit_Price'].max()
lowest_unit_price = df['Unit_Price'].min()
highest_quantity = df['Quantity'].max()
lowest_quantity = df['Quantity'].min()

print("Highest Total Bill:", highest_total_bill)
print("Lowest Total Bill:", lowest_total_bill)
print("Highest Unit Price:", highest_unit_price)
print("Lowest Unit Price:", lowest_unit_price)
print("Highest Quantity:", highest_quantity)
print("Lowest Quantity:", lowest_quantity)

# Total Revenue, Average Revenue, Average Unit Price, Average Quantity
total_revenue = df['Total_Bill'].sum()
average_revenue = df['Total_Bill'].mean()
average_unit_price = df['Unit_Price'].mean()
average_quantity = df['Quantity'].mean()

print("Total Revenue:", total_revenue)
print("Average Revenue:", average_revenue)
print("Average Unit Price:", average_unit_price)
print("Average Quantity:", average_quantity)

# Revenue by City
revenue_by_city = df.groupby('City')['Total_Bill'].sum()
print("Revenue by City:")
print(revenue_by_city)

# Revenue by Medicine
revenue_by_medicine = df.groupby('Medicine')['Total_Bill'].sum()
print("Revenue by Medicine:")
print(revenue_by_medicine)

# Revenue by Category
revenue_by_category = df.groupby('Category')['Total_Bill'].sum()
print("Revenue by Category:")
print(revenue_by_category)

# Revenue by Pharmacist
revenue_by_pharmacist = df.groupby('Pharmacist')['Total_Bill'].sum()
print("Revenue by Pharmacist:")
print(revenue_by_pharmacist)

# Average Unit Price by Category
average_unit_price_by_category = df.groupby('Category')['Unit_Price'].mean()
print("Average Unit Price by Category:")
print(average_unit_price_by_category)

# Average Quantity by Category
average_quantity_by_category = df.groupby('Category')['Quantity'].mean()
print("Average Quantity by Category:")
print(average_quantity_by_category)

# Total Quantity by Medicine
total_quantity_by_medicine = df.groupby('Medicine')['Quantity'].sum()
print("Total Quantity by Medicine:")
print(total_quantity_by_medicine)

# Sales Count by Payment Method
sales_count_by_payment_method = df['Payment_Method'].value_counts()
print("Sales Count by Payment Method:")
print(sales_count_by_payment_method)

# 5.Charts

# Bar Chart
df.groupby('Category')['Total_Bill'].sum().plot(kind='bar')
plt.title('Total Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Total Revenue')
plt.show()

# Pie Chart
df.groupby('City')['Total_Bill'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title('Total Revenue by City')
plt.ylabel('')
plt.show()

# Line Chart
df.groupby('Medicine')['Total_Bill'].sum().plot(kind='line')
plt.title('Total Revenue by Medicine')
plt.xlabel('Medicine')
plt.ylabel('Total Revenue')
plt.show()

# Area Chart
df.groupby('Medicine')['Total_Bill'].sum().plot(kind='area')
plt.title('Total Revenue by Medicine')
plt.xlabel('Medicine')
plt.ylabel('Total Revenue')
plt.show()

# Scatter Plot
df.plot(kind='scatter', x='Unit_Price', y='Quantity')
plt.title('Unit Price vs Quantity')
plt.xlabel('Unit Price')
plt.ylabel('Quantity')
plt.show()

# Histogram
df['Total_Bill'].plot(kind='hist')
plt.title('Distribution of Total Revenue')
plt.xlabel('Total Revenue')
plt.ylabel('Frequency')
plt.show()

# Box Plot
df.groupby('Category')['Total_Bill'].sum().plot(kind='box')
plt.title('Box Plot of Total Revenue by Category')
plt.ylabel('Total Revenue')
plt.show()

# Hexbin Plot
df.plot(kind='hexbin', x='Unit_Price', y='Quantity', gridsize=20)
plt.title('Hexbin Plot of Unit Price vs Quantity')
plt.xlabel('Unit Price')
plt.ylabel('Quantity')
plt.show()

# Which city generated the highest revenue?
print("City with Highest Revenue:",
      df.groupby('City')['Total_Bill'].sum().idxmax())

# Which medicine generated the highest revenue?
print("Medicine with Highest Revenue:",
      df.groupby('Medicine')['Total_Bill'].sum().idxmax())

# Which category earned the highest revenue?
print("Category with Highest Revenue:",
      df.groupby('Category')['Total_Bill'].sum().idxmax())

# Which pharmacist handled the highest sales?
print("Top Pharmacist:",
      df.groupby('Pharmacist')['Total_Bill'].sum().idxmax())

# Which payment method was used the most?
print("Most Used Payment Method:",
      df['Payment_Method'].value_counts().idxmax())

# Which customer spent the most?
print("Customer Who Spent the Most:",
      df.groupby('Customer_Name')['Total_Bill'].sum().idxmax())

# Which medicine sold the highest quantity?
print("Medicine with Highest Quantity Sold:",
      df.groupby('Medicine')['Quantity'].sum().idxmax())

# What is the average bill per customer?
print("Average Bill per Customer:",
      df.groupby('Customer_Name')['Total_Bill'].sum().mean())

# 7.Export
df.to_csv('Pharmacy-Sales-Analysis.csv', index=False)

