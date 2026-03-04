import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Placement_Dataset.csv")

fig, ax = plt.subplots(figsize=(8,8))
sns.histplot(df["salary"], ax=ax)
plt.show()