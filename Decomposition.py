import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
train = pd.read_table('data/train.csv')
encoder = LabelEncoder()
scaler = StandardScaler()
train["KC(Default)"] = encoder.fit_transform(train["KC(Default)"])
train["Step Name"] = encoder.fit_transform(train["Step Name"])
train["Opportunity(Default)"] = encoder.fit_transform(train["Opportunity(Default)"])
# train = scaler.fit_transform(train)
# for i in range(0,20):
#     print(train["KC(Default)"][i])
#     print(train["Opportunity(Default)"][i])
