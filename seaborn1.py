import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Load the example tips dataset
tips = sns.load_dataset("tips")
df=pd.DataFrame(tips)
print(df.head())
print(df.describe())
print(df.info())
print(df["day"].value_counts())
# Create a scatter plot of total bill vs. tip
sns.scatterplot(x="total_bill", y="tip", data=tips)
# Show the plotplt.show()
plt.show()
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()
sns.histplot(tips["total_bill"], kde=True)
plt.show()
sns.pairplot(tips)
plt.show()
sns.kdeplot(tips["total_bill"], shade=True)
plt.show()
corr=tips[["total_bill","tip","size"]].corr()
print(corr)
sns.heatmap(corr, annot=True, cmap="coolwarm")  
plt.show()

