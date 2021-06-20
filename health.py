import pandas as pd
from sklearn.preprocessing import StandardScalar
from numpy import set_printoptions
data=pd.read_csv('C://Users//Maansi//Desktop//diabetes.csv').values
features=data[:,0:8]
labels=data[:,8]
print(labels[:5])
'''minmaxscaler=MinMaxScaler(feature_range=(0,1))
new_features=minmaxscaler.fit_transform(features)
set_printoptions(3)
print(new_features[:5])'''
nn=Normalizer().fit(features)
new_fetures=nn.transform(features)
set_printoptions(3)
print(new_fetures(0:2))
