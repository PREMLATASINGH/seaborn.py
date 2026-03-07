import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
df=pd.DataFrame({
    "Region": ["North", "South", "East", "West", "Central"],
    "Value": [10, 15, 7, 12, 20]
})
print(df.head())
print(df.describe())
print(df.info())
print(df["Region"].value_counts())
print(df.columns)
plt.figure(figsize=(10,6))
sns.barplot(x="Region", y="Value", data=df)
plt.title("Bar Plot of Region vs Value")
plt.xlabel("Region")
plt.ylabel("Value")
plt.savefig('barplot.png')
plt.close()