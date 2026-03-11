import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
df = pd.DataFrame({"sales": [200, 220, 250, 270, 300], "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                    "profit": [50, 60, 70, 80, 90], "expenses": [150, 160, 180, 190, 210]})
print(df.head())
print(df.describe())
print(df.info())
print(df["day"].value_counts())