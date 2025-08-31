import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

quali = pd.read_csv('qualifying.csv')
print(quali.columns)

pole_laps = quali[quali['position'] == 1]
pole_count = pole_laps['number'].value_counts().head(10)

top10 = pole_count.reset_index()
top10.columns = ['driver_number', 'pole_positions']

plt.figure(figsize=(10, 6))
plt.bar(top10['driver_number'].astype(str), top10['pole_positions'], color='red')
plt.xlabel('Driver Number')
plt.ylabel('Number of poles')
plt.title('Top 10 drivers with most poles')

plt.tight_layout()
plt.show()
