import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
df=pd.DataFrame({
   "hours": [1, 2, 3, 4, 5],
   "score": [10, 20, 30, 40, 50]
})
print(df.head())
print(df.describe())
print(df.info())
print(df["hours"].value_counts())
print(df.columns)
plt.figure(figsize=(10,6))
sns.barplot(x="hours", y="score", data=df)  
plt.title("Bar Plot of Hours vs Score")
plt.xlabel("Hours")
plt.ylabel("Score")
plt.savefig('barplot.png')
plt.close()