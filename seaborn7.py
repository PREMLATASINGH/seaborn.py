import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
    "subject": ["Math", "Science", "English", "History", "Art"],
    "score": [85, 90, 78, 92, 88]
})
print(df.head())
print(df.describe())