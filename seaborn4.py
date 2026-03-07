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