import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
import fastf1

fastf1.Cache.enable_cache('D:\\Me\\idk\\python\\F1 data analysis')
session = fastf1.get_session(2024, 12, "R")
session.load()


laps = session.laps
ham_laps = laps.pick_drivers(['HAM'])
ham_laps['LapTimeSeconds'] = ham_laps['LapTime'].dt.total_seconds()

plt.plot(ham_laps['LapNumber'], ham_laps['LapTimeSeconds'], marker='o')
plt.title("Hamilton Lap Times")
plt.xlabel("Lap Number")
plt.ylabel("Time (s)")
plt.show()
