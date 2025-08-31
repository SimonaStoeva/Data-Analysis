import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

retail_data = pd.read_csv('retail_price.csv')
retail_data.isna().sum()
dates = pd.to_datetime(retail_data["month_year"])

#print(retail_data.describe().round(2))

#Deviation of the cheapest sale and the most expensive
sales_arr = retail_data["total_price"].to_numpy()
min_sale = np.min(sales_arr)
max_sale = np.max(sales_arr)
std_sale = np.std(sales_arr)

print(f"Minimum sale price: {min_sale}")
print(f"Maximum sale price: {max_sale}")
print(f"Standard deviation of the prices: {std_sale}")

#Top 5 most sold cateogries
sales_sum = retail_data.groupby("product_category_name")["total_price"].sum().sort_values(ascending=False).head(5)
plt.pie(sales_sum, labels=sales_sum.index, autopct='%1.1f%%')
plt.title("5 most sold categories")
plt.show()

#Top 5 least sold cateogries
sales_sum = retail_data.groupby("product_category_name")["total_price"].sum().sort_values(ascending=True).head(5)
plt.figure(figsize=(8,5))
plt.bar(sales_sum.index, sales_sum.values, color='orange')
plt.title("5 least sold categories")
plt.xlabel("Category")
plt.ylabel("Total sales")
plt.xticks(rotation=45, ha='right')
plt.show()