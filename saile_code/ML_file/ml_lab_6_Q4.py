#Compute SONAR classification results with and without data pre-processing (data
#normalization). Perform data pre-processing with your implementation and with
#scikit-learn methods and compare the results.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.interchange import column
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, minmax_scale
from sklearn.linear_model import RidgeClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MinMaxScaler


# i am loading data
data=pd.read_csv('/home/sails/Downloads/archive(2)/sonar.csv')
print(data.head())
print(data.shape)
print(data.columns)
print(data['R'].unique())
def load_cancer_data(data):

    print('d',data.head())
    print(data.columns)
    print(data.shape)
    return data

def splitting_data(data):

    #i am doing EDA
    # i am removing unnecessary columns id  and unbamed32 culumns ,unnamed contain NAN




    print(data['R'].unique())

    X=data.drop('R', axis=1)

    y=data["R"]

    X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 42 , test_size = 0.2 , shuffle = True , stratify = y)

    print(X_train.shape , X_test.shape , y_train.shape , y_test.shape)

    return X_train, X_test, y_train, y_test

from sklearn.metrics import confusion_matrix

def Model_training_sonar():


    X_train, X_test, y_train, y_test = splitting_data(data)

    le=LabelEncoder()
    # i am going to label encoding
    y_train=le.fit_transform(y_train)


    y_test=le.transform(y_test)

    model = LogisticRegression()

    cv=KFold(n_splits=10,shuffle=True,random_state=28)

    trans=MinMaxScaler()
    # i am doing x_train  normalization  about minmxscaler

    x_train_trans=trans.fit_transform(X_train)
    x_test_trans=trans.transform(X_test)

    score=cross_val_score(model,  x_train_trans,y_train,cv=cv)

    print(score)
    print(score.mean())
    print(score.std())

    final_model=model.fit(x_train_trans,y_train)

    y_predict = final_model.predict(x_test_trans)

    print(y_predict)

    confu=confusion_matrix(y_test,y_predict)
    

    print('confusion matric lasso_classifier:', confu)





Model_training_sonar()

