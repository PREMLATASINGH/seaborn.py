import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=pd.DataFrame({
    "Category": ["A", "B", "C", "D", "E"],
    "Value": [10, 15, 7, 12, 20],
    "Region": ["North", "South", "East", "West", "Central"] 
})
print(df.head())