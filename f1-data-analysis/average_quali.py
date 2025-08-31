import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

quali_df = pd.read_csv('qualifying.csv')
results_df = pd.read_csv('results.csv')
drivers_df = pd.read_csv('drivers.csv')

quali_df.dropna(subset=['position'], inplace=True)
results_df.dropna(subset=['positionOrder'], inplace=True)

avg_quali = quali_df.groupby('driverId')[['position', 'number']].agg({
    'position': 'mean',
    'number' : 'first'
}).reset_index()

avg_results = results_df.groupby('driverId')[['positionOrder', 'number']].agg({
    'positionOrder': 'mean',
    'number' : 'first'
}).reset_index()

avg_merged = pd.merge(avg_quali, avg_results, on='driverId', suffixes=('_quali', '_race'))

avg_merged['diff'] = avg_merged['positionOrder'] - avg_merged['position']

avg_merged['status'] = np.where(avg_merged['diff'] > 0, 'Loss', 'Gain')

print(avg_merged[['driverId', 'number_quali', 'position', 'positionOrder', 'diff', 'status']]
      .assign(
    position = lambda x: x['position'].round(2),
    positionOrder = lambda x: x['positionOrder'].round(2),
    diff = lambda x: x['diff'].round(2),
)
      .head(10))

