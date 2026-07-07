import pandas as pd

data = {
    "Product_ID": range(9001, 9026),

    "Product": [
        "Laptop","Mouse","Keyboard","Monitor","Printer",
        "Tablet","Phone","Speaker","Camera","Router",
        "Laptop","Mouse","Keyboard","Monitor","Printer",
        "Tablet","Phone","Speaker","Camera","Router",
        "Laptop","Mouse","Keyboard","Monitor","Printer"
    ],

    "Category": [
        "Electronics","Accessories","Accessories","Electronics","Electronics",
        "Electronics","Electronics","Accessories","Electronics","Networking",
        "Electronics","Accessories","Accessories","Electronics","Electronics",
        "Electronics","Electronics","Accessories","Electronics","Networking",
        "Electronics","Accessories","Accessories","Electronics","Electronics"
    ],

    "Warehouse": [
        "A","A","B","B","C",
        "A","B","C","A","C",
        "B","C","A","A","B",
        "C","B","A","C","A",
        "B","A","C","B","A"
    ],

    "Supplier": [
        "TechCorp","TechCorp","PrimeIT","PrimeIT","GlobalTech",
        "TechCorp","GlobalTech","PrimeIT","TechCorp","NetLink",
        "PrimeIT","GlobalTech","TechCorp","PrimeIT","GlobalTech",
        "NetLink","TechCorp","PrimeIT","GlobalTech","NetLink",
        "TechCorp","PrimeIT","GlobalTech","TechCorp","PrimeIT"
    ],

    "Unit_Price": [
        120000,2500,5000,45000,35000,
        60000,85000,7000,95000,12000,
        118000,2600,5200,46000,34000,
        61000,84000,7200,97000,12500,
        121000,2550,5100,45500,34500
    ],

    "Stock": [
        10,80,60,20,15,
        18,25,40,12,35,
        9,75,55,18,16,
        20,24,38,11,32,
        8,82,58,19,14
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

df.isnull().sum()

df.duplicated().sum()

# 2.Create Inventory_Value = Unit_Price × Stock
Inventory_Value = df['Unit_Price'] * df['Stock']
df['Inventory_Value'] = Inventory_Value
df

# 3.Analysis

# Highest inventory value, Lowest inventory value, Highest unit price, Lowest unit price, Highest stock, Lowest stock
Highest_Inventory_Value = df['Inventory_Value'].max()
Lowest_Inventory_Value = df['Inventory_Value'].min()
Highest_Unit_Price = df['Unit_Price'].max()
Lowest_Unit_Price = df['Unit_Price'].min()
Highest_Stock = df['Stock'].max()
Lowest_Stock = df['Stock'].min()

print("Highest inventory value : ", Highest_Inventory_Value)
print("Lowest inventory value : ", Lowest_Inventory_Value)
print("Highest unit price : ", Highest_Unit_Price)
print("Lowest unit price : ", Lowest_Unit_Price)
print("Highest stock  :", Highest_Stock)
print("Lowest stock : ", Lowest_Stock)

# Total inventory value, Average inventory value, Average unit price, Average stock
Total_Inventory_Value = df['Inventory_Value'].sum()
Average_Inventory_Value = df['Inventory_Value'].mean()
Average_Unit_Price = df['Unit_Price'].mean()
Average_Stock = df['Stock'].mean()

print("Total Inventory Value:", Total_Inventory_Value)
print("Average Inventory Value:", Average_Inventory_Value)
print("Average Unit Price:", Average_Unit_Price)
print("Average Stock:", Average_Stock)

# 4. GroupBy Analysis

# Inventory value by Category, Inventory value by Warehouse, Inventory value by Supplier, Average Unit Price by Category, Average Stock by Warehouse, Total Stock by Category, Total Stock by Supplier, Product count by Warehouse
Inventory_Value_By_Category = df.groupby('Category')['Inventory_Value'].sum()
Inventory_Value_By_Warehouse = df.groupby('Warehouse')['Inventory_Value'].sum()
Inventory_Value_By_Supplier = df.groupby('Supplier')['Inventory_Value'].sum()
Average_Unit_Price_By_Category = df.groupby('Category')['Unit_Price'].mean
Average_Stock_By_Warehouse = df.groupby('Warehouse')['Stock'].mean()
Total_Stock_By_Category = df.groupby('Category')['Stock'].sum()
Total_Stock_By_Supplier = df.groupby('Supplier')['Stock']
Product_Count_By_Warehouse = df.groupby('Warehouse')['Product_ID'].count

print("Inventory Value by Category:")
print(Inventory_Value_By_Category)
print("\nInventory Value by Warehouse:")
print(Inventory_Value_By_Warehouse)
print("\nInventory Value by Supplier:")
print(Inventory_Value_By_Supplier)
print("\nAverage Unit Price by Category:")
print(Average_Unit_Price_By_Category)
print("\nAverage Stock by Warehouse:")
print(Average_Stock_By_Warehouse)
print("\nTotal Stock by Category:")
print(Total_Stock_By_Category)
print("\nTotal Stock by Supplier:")
print(Total_Stock_By_Supplier)
print("\nProduct Count by Warehouse:")
print(Product_Count_By_Warehouse)

# 5.Charts

# Bar Chart
import matplotlib.pyplot as plt

plt.bar(df['Category'], df['Inventory_Value'])
plt.xlabel('Category')
plt.ylabel('Inventory Value')
plt.title('Inventory Value by Category')
plt.show()

# Pie Chart
plt.pie(df['Inventory_Value'], labels=df['Category'], autopct='%1.1f%%')
plt.title('Inventory Value by Category')
plt.show()

# Line Chart
plt.plot(df['Warehouse'], df['Inventory_Value'])
plt.xlabel('Warehouse')
plt.ylabel('Inventory Value')
plt.title('Inventory Value by Warehouse')
plt.show()

# Scatter Plot
plt.scatter(df['Unit_Price'], df['Stock'])
plt.xlabel('Unit Price')
plt.ylabel('Stock')
plt.title('Unit Price vs Stock')
plt.show()

# Histogram
plt.hist(df['Inventory_Value'], bins=10)
plt.xlabel('Inventory Value')
plt.ylabel('Frequency')
plt.title('Inventory Value Distribution')
plt.show()

# Box Plot
plt.boxplot(df['Inventory_Value'])
plt.ylabel('Inventory Value')
plt.title('Inventory Value Distribution')
plt.show()

# Area Chart
plt.stackplot(df['Category'], df['Inventory_Value'])
plt.xlabel('Category')
plt.ylabel('Inventory Value')
plt.title('Inventory Value by Category')
plt.show()

# Bubble Chart
plt.scatter(df['Unit_Price'], df['Stock'], s=df['Inventory_Value'])
plt.xlabel('Unit Price')
plt.ylabel('Stock')
plt.title('Unit Price vs Stock')
plt.show()

# Which warehouse has the highest inventory value?, Which category has the highest inventory value?, Which supplier provides the highest inventory value?, Which product has the highest inventory value?, Which product has the highest stock?, Which product has the highest unit price?, Which warehouse stores the most stock?, Which category contains the most stock?
warehouse_highest_inventory = df.groupby('Warehouse')['Inventory_Value'].sum().idxmax()
category_highest_inventory = df.groupby('Category')['Inventory_Value'].sum().idxmax()
supplier_highest_inventory = df.groupby('Supplier')['Inventory_Value'].sum().idxmax()
product_highest_inventory = df.loc[df['Inventory_Value'].idxmax()]['Product']
product_highest_stock = df.loc[df['Stock'].idxmax()]['Product']
product_highest_unit_price = df.loc[df['Unit_Price'].idxmax()]['Product']
warehouse_most_stock = df.groupby('Warehouse')['Stock'].sum().idxmax()
category_most_stock = df.groupby('Category')['Stock'].sum().idxmax()

print("Warehouse with the highest inventory value:", warehouse_highest_inventory)
print("Category with the highest inventory value:", category_highest_inventory)
print("Supplier with the highest inventory value:", supplier_highest_inventory)
print("Product with the highest inventory value:", product_highest_inventory)
print("Product with the highest stock:", product_highest_stock)
print("Product with the highest unit price:", product_highest_unit_price)
print("Warehouse with the most stock:", warehouse_most_stock)
print("Category with the most stock:", category_most_stock)

df.to_csv("Warehouse-Inventory-Analysis.csv", index=False)
