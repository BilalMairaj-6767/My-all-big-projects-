from google.colab import files

uploaded = files.upload()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

df

print(df.duplicated().sum())

df.columns

df.shape

df.describe()

df.info()

df.isnull().sum()

df.head()

df.tail()

highest_Sales = df.loc[df["Sales"].idxmax()]
Lowest_Sales = df.loc[df["Sales"].idxmin()]
highest_Quantity = df.loc[df["Quantity"].idxmax()]
lowest_Quantity = df.loc[df["Quantity"].idxmin()]

print("Highest Sales: ", highest_Sales)
print("\nLowest Sales: ", Lowest_Sales)
print("\nHighest Quantity: ", highest_Quantity)
print("\nLowest Quantity: ", lowest_Quantity)

df.groupby('Sub-Category')['Sales'].sum().plot(kind='bar', figsize=(12, 6))
plt.title("Total Sales by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

df.groupby('Discount')['Sales'].sum().plot(kind='bar', figsize=(12, 6))
plt.title("Total Discount by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Discount")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

  df.dtypes

df.value_counts('Row ID')

df.value_counts('Order Date')

df.value_counts('Order ID')

df.value_counts('Customer ID')

df.value_counts('Customer Name')

df.value_counts('Segment')

df.value_counts('Country')

df.value_counts('City')

df.value_counts('State')

df.value_counts('Postal Code')

df.value_counts('Region')

df.value_counts('Product ID')

df.value_counts('Sub-Category')

df.value_counts('Product Name')

df.value_counts('Sales')

df.value_counts('Quantity')

df.value_counts('Discount')

df.value_counts('Profit')

df.value_counts('Ship Mode')

df.value_counts('Ship Date')

df.value_counts('Category')
