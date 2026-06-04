import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

df = pd.read_csv('sales_data_sample.csv', encoding='cp1252')
#print(df.columns)
#df.info() - sales: float, country: object

#print(df.isna().sum())

sales_per_country = df.groupby('COUNTRY')['SALES'].sum()
#print(sales_per_country)

top_5_sales = sales_per_country.sort_values(ascending=False).head(5)
#print(top_5_sales)

countries = top_5_sales.index
sales = top_5_sales.values.astype(int)

plt.pie(sales, labels=countries, autopct='%1.1f%%')
plt.title("Top 5 countries with most sales")
plt.tight_layout()
plt.show()
