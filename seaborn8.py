import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
df = pd.DataFrame({"sales": [200, 220, 250, 270, 300], "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                    "profit": [50, 60, 70, 80, 90], "expenses": [150, 160, 180, 190, 210]})
print(df.head())
print(df.describe())
print(df.info())
print(df["day"].value_counts())
print(df.columns)
plt.figure(figsize=(10, 6))
sns.barplot(x="day", y="sales", data=df)    
plt.title("Bar Plot of Day vs Sales")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.savefig('barplot.png')
plt.close()
plt.figure(figsize=(10, 6))
sns.histplot(df["profit"], kde=True)
plt.title("Histogram of Profit")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.savefig('histogram.png')
plt.close()