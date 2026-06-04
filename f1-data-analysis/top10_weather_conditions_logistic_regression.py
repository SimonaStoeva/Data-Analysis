import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns

weather = pd.read_csv('f1 weather 2018-2023.csv')  # time, AirTemp, Humidity, Pressure, Rain, TrackTemp, WindDirection, WindSpeed, Round Number, Year
results = pd.read_csv('f1 2021 results.csv')  # Track, Position, No, Driver, Team, Starting Grid, Laps, Time/Retired, Points, +1 Pt, Fastest Lap


def top10_flag(pos):
    try:
        position = int(pos)
        return 1 if position <= 10 else 0
    except:
        return 0


results['Top 10'] = results['Position'].apply(top10_flag)

weather_avg = weather.groupby('Round Number').agg({
    'AirTemp': 'mean',
    'TrackTemp': 'mean',
    'Humidity': 'mean',
    'Pressure': 'mean'
}).reset_index()

results['Round Number'] = 4

data = results.merge(weather_avg, on='Round Number', how='left')

features = ['AirTemp', 'TrackTemp', 'Humidity', 'Pressure', 'Starting Grid']
X = data[features]
y = data['Top 10']

X = X.fillna(X.mean())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

plt.figure(figsize=(8,4))
plt.scatter(range(len(y_prob)), y_prob, c=y_test, cmap='bwr', alpha=0.7)
plt.scatter([], [], c='red', label='Actual: In top 10')
plt.scatter([], [], c='blue', label='Actual: Not in top 10')
plt.xlabel("Sample")
plt.ylabel("Probability of Top 10")
plt.title("Predicted Probability vs Actual Top 10")
plt.legend()
plt.show()

plt.figure(figsize=(6,5))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8,6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC крива (AUC = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC / AUC крива')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()
