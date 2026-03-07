import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'sales': [100, 150, 200, 250, 300, 350],
    'profit': [20, 30, 50, 70, 90, 110]
})
print(df.head())
print(df.describe())
print(df.info())