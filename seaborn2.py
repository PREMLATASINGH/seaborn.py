import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
df=pd.read_csv("data.csv")
print(df.head())
plt.figure(figsize=(10,6))
sns.barplot(x="Category", y="Value", data=df)
plt.title("Bar Plot of Category vs Value")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()