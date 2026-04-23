import pandas as pd
import sklearn.datasets
from sklearn.preprocessing import LabelEncoder

cancer_data = pd.read_csv("data.csv")

cancer_data.head()
