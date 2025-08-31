import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

quali = pd.read_csv('qualifying.csv')
races = pd.read_csv('races.csv')

merged = pd.merge(quali, races, on='raceId')
pole_positions = merged[merged['position'] == 1]

driver_id = 1
driver_number = pole_positions[pole_positions['driverId'] == driver_id]['number'].mode()[0]
driver_poles = pole_positions[pole_positions['driverId'] == driver_id]
poles_per_year = driver_poles.groupby('year').size()

plt.figure(figsize=(10,6))
plt.plot(poles_per_year.index, poles_per_year.values, marker='o', color='orange')
plt.title(f'Pole Positions per Year for Driver # {driver_number}')
plt.xlabel('Year')
plt.ylabel('Number Pole Positions')
plt.grid(True)
plt.tight_layout()
plt.show()
