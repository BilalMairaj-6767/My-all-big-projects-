import pandas as pd

data = {
    "Order_ID": [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115],

    "Food_Item": [
        "Burger","Pizza","Pasta","Biryani","Sandwich",
        "Pizza","Burger","Fries","Biryani","Pasta",
        "Pizza","Burger","Fries","Sandwich","Biryani"
    ],

    "Category": [
        "Fast Food","Fast Food","Italian","Rice","Fast Food",
        "Fast Food","Fast Food","Sides","Rice","Italian",
        "Fast Food","Fast Food","Sides","Fast Food","Rice"
    ],

    "Price": [
        450,900,700,600,350,
        950,500,250,650,750,
        1000,550,300,400,700
    ],

    "Quantity": [
        2,1,3,2,4,
        2,3,5,1,2,
        1,2,6,3,2
    ],

    "Rating": [
        4.5,4.8,4.2,4.6,4.1,
        4.9,4.4,4.0,4.7,4.3,
        5.0,4.5,4.2,4.0,4.8
    ],

    "City": [
        "Karachi","Lahore","Islamabad","Karachi","Multan",
        "Lahore","Karachi","Islamabad","Peshawar","Multan",
        "Karachi","Lahore","Islamabad","Peshawar","Karachi"
    ],

    "Payment_Method": [
        "Cash","Card","Cash","Online","Card",
        "Online","Cash","Card","Cash","Online",
        "Card","Cash","Online","Card","Cash"
    ]
}

df = pd.DataFrame(data)

df

# 1. Data Exploration (EDA)

df.head()

df.tail()

df.describe()

df.shape

df.columns

# 2. Analysis

# highest & lowest priced food
highest_price_of_food = df['Price'].max()
lowest_price_of_food = df['Price'].min()

print("Highest Priced Food:", highest_price_of_food)
print("Lowest Priced Food:", lowest_price_of_food)

# highest & lowest rated food
highest_rated_food = df.loc[df['Rating'].idxmax(), 'Food_Item']
lowest_rated_food = df.loc[df['Rating'].idxmin(), 'Food_Item']

print("Highest Rated Food:", highest_rated_food)
print("Lowest Rated Food:", lowest_rated_food)

# Total sales amount (Price × Quantity)
df['Total_Sales'] = df['Price'] * df['Quantity']
total_sales_amount = df['Total_Sales'].sum()

print("Total Sales Amount:", total_sales_amount)

# Average rating
average_rating = df['Rating'].mean()

print("Average Rating:", average_rating)

# Average price
average_price = df['Price'].mean()

print("Average Price:", average_price)

# Total quantity sold
total_quantity_sold = df['Quantity'].sum()

print("Total Quantity Sold:", total_quantity_sold)

# 3. GroupBy Analysis

# Average price by category
average_price_by_category = df.groupby('Category')['Price'].mean()

print("Average Price by Category:")
print(average_price_by_category)

# Average rating by category
average_rating_by_category = df.groupby('Category')['Rating'].mean()

print("Average Rating by Category:")
print(average_rating_by_category)

# Total quantity by food item
total_quantity_by_food_item = df.groupby('Food_Item')['Quantity'].sum()

print("Total Quantity by Food Item:")
print(total_quantity_by_food_item)

# Total sales by city
total_sales_by_city = df.groupby('City')['Total_Sales'].sum()

print("Total Sales by City:")
print(total_sales_by_city)

# Average rating by city
average_rating_by_city = df.groupby('City')['Rating'].mean()

print("Average Rating by City:")
print(average_rating_by_city)

# Total orders by payment method
total_orders_by_payment_method = df['Payment_Method'].value_counts()

print("Total Orders by Payment Method:")
print(total_orders_by_payment_method)

# 4. Charts

# Bar Chart
import matplotlib.pyplot as plt

plt.bar(average_price_by_category.index, average_price_by_category.values)
plt.xlabel('Category')
plt.ylabel('Average Price')
plt.title('Average Price by Category')
plt.show()

# Pie Chart
plt.pie(average_rating_by_category.values, labels=average_rating_by_category.index, autopct='%1.1f%%')
plt.title('Average Rating by Category')
plt.show()

# Scatter Plot
plt.scatter(df['Price'], df['Quantity'])
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.title('Price vs Quantity')
plt.show()

# Line Chart
plt.plot(total_sales_by_city.index, total_sales_by_city.values, marker='o')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.title('Total Sales by City')
plt.xticks(rotation=45)
plt.show()

# Box Plot
plt.boxplot(df['Rating'])
plt.ylabel('Rating')
plt.title('Rating Distribution')
plt.show()

# 5. Business Insights

# Which city generated the highest sales?
city_with_highest_sales = total_sales_by_city.idxmax()
print("City with Highest Sales:", city_with_highest_sales)

# Which food item sold the most?
food_item_with_most_sales = total_quantity_by_food_item.idxmax()
print("Food Item with Most Sales:", food_item_with_most_sales)

# Which category has the highest average rating?
category_with_highest_rating = average_rating_by_category.idxmax()
print("Category with Highest Average Rating:", category_with_highest_rating)

# Which payment method is used the most?
payment_method_used_most = total_orders_by_payment_method.idxmax()
print("Payment Method Used the Most:", payment_method_used_most)

# Which food item is the most expensive?
most_expensive_food_item = df.loc[df['Price'].idxmax(), 'Food_Item']
print("Most Expensive Food Item:", most_expensive_food_item)

# 6.Export

df.to_csv("Restaurant-Sales-Analysis.csv", index=False)

