import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
df=pd.read_csv("data.csv")
print(df.head())
print(df.describe())
print(df.info())
print(df["Region"].value_counts())
plt.figure(figsize=(10,6))
sns.barplot(x="Region", y="Value", data=df)
plt.title("Bar Plot of Region vs Value")
plt.xlabel("Region")
plt.ylabel("Value")
plt.show()