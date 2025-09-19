import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

constructor_df = pd.read_csv('constructor_standings.csv')
print(constructor_df.columns)
#print(constructor_df.info)
#print(constructor_df.isna().sum())

team_points = constructor_df["PTS"].to_numpy()
min_team_points = np.min(team_points)
max_team_points = np.max(team_points)
dev_team_points = np.std(team_points)
print(f"Minimum points scored by a team: {min_team_points:.2f}\nMaximum points scored by a team: {max_team_points:.2f}\nStandard deviation in points: {dev_team_points:.2f}")

most_points = constructor_df.groupby("Team")["PTS"].sum()
top_5 = most_points.sort_values(ascending=False).head(5)

x = top_5.index
y = top_5.values
plt.figure(figsize=(5,4))
plt.bar(x, y, color="blue", width=0.5)
plt.title("Top 5 constructors with most points")
plt.xlabel("Constructor")
plt.ylabel("Points")
plt.xticks(rotation=40)
plt.show()
