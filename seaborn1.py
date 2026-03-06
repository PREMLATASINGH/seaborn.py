import seaborn as sns
import matplotlib.pyplot as plt
# Load the example tips dataset
tips = sns.load_dataset("tips")
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