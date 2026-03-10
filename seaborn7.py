import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
    "subject": ["Math", "Science", "English", "History", "Art"],
    "score": [85, 90, 78, 92, 88]
})
print(df.head())
print(df.describe())
print(df.info())
print(df["subject"].value_counts())
print(df.columns)
plt.figure(figsize=(10, 6))
sns.barplot(x="subject", y="score", data=df)
plt.title("Bar Plot of Subject vs Score")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.savefig('barplot.png')
plt.close()
plt.figure(figsize=(10, 6))
sns.histplot(df["score"], kde=True) 
plt.title("Histogram of Score")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig('histogram.png')
plt.close()
plt.figure(figsize=(10, 6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig('heatmap.png')
plt.close()
df1=pd.DataFrame({
    "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "sales": [200, 220, 250, 270, 300]
})
print(df1.head())
print(df1.describe())