import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing

data=pd.read_csv("iris.csv")
data.head()

x=data.iloc[:,:4]
x.head()

y=data.iloc[:,-1]
y.head()

x=preprocessing.StandardScaler().fit_transform(x)
x[0:4]

"""Train-test-split"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
y_test.shape

"""Training and predicting"""

knmodel=KNeighborsClassifier(n_neighbors=3)
knmodel.fit(x_train,y_train)
y_pred=knmodel.predict(x_test)

"""Accuracy"""

from sklearn.metrics import accuracy_score
acc=accuracy_score(y_test,y_pred)
print(acc)
