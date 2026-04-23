import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

datasets = sklearn.datasets.load_breast_cancer()

#loadinf the data to a pandas df
df = pd.DataFrame(datasets.data, columns=datasets.feature_names)

X = df
Y = datasets.target  

#Splitting the data inot traiining data and test data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=3)