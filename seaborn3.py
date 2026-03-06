import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=pd.DataFrame({
    "Category": ["A", "B", "C", "D", "E"],
    "Value": [10, 15, 7, 12, 20],
    "Region": ["North", "South", "East", "West", "Central"] 
})
print(df.head())
print(df.describe())
print(df.info())
print(df["Region"].value_counts())
plt.figure(figsize=(10,6))
sns.barplot(x="Category", y="Value", data=df)
plt.title("Bar Plot of Category vs Value")
plt.xlabel("Category")
plt.ylabel("Value")
plt.savefig('barplot.png')
plt.close()