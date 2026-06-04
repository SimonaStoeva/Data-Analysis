import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

df = pd.read_csv("sales_data_sample.csv", encoding="cp1252")
quarter_df = df.groupby("QTR_ID")["SALES"].sum()
quarter_df = quarter_df.astype(int)
print(quarter_df)
print(type(quarter_df))

print(quarter_df.index) #x
print(quarter_df.values) #y

max_pos = np.argmax(quarter_df)
strongest_qtr = quarter_df.index[max_pos]
biggest_sales = np.max(quarter_df)

print(f"Strongest quarter: Q{strongest_qtr}")
print(f"Biggest sales: {biggest_sales}")

plt.figure(figsize=(8,5))
bars = plt.bar(quarter_df.index, quarter_df.values, color="lightblue")
plt.bar_label(bars, fmt='%d')
plt.title("Quarter with most sales")
plt.xlabel("Quarter")
plt.ylabel("Sales")
plt.xticks([1,2,3,4], ha='right')
plt.ticklabel_format(style="plain", axis="y")
plt.show()


#print(max_pos)


