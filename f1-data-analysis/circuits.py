import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')


races_df = pd.read_csv('races.csv')
circuits_df = pd.read_csv('circuits.csv')

print(races_df.columns)
print(circuits_df.columns)


left = races_df
right = circuits_df
on = 'circuitId'
suffixes = ('_race', '_circuit')
merged_df = pd.merge(left, right, on=on, suffixes=suffixes)

print(merged_df.head())
print(merged_df.columns)

num_circuits = merged_df.groupby('name_circuit')
print(num_circuits.size())

races_per_circuit = num_circuits.size().sort_values(ascending=False)
print(races_per_circuit.head(10))

top10 = races_per_circuit.head(10)

labels = top10.index
num_races = top10.values
plt.pie(num_races, labels=labels, autopct='%1.1f%%')
plt.title("Top 10 circuits with most races")
plt.tight_layout()
plt.show()
