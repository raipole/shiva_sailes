#5. Build a classification model for wisconsin dataset using Ridge and Lasso classifier using
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.interchange import column
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import RidgeClassifier


# i am loading data
data=pd.read_csv('/home/sails/Downloads/archive (2)/data.csv')
print(data['diagnosis'].value_counts())
def load_cancer_data(data):

    print('d',data.head())
    print(data.columns)
    print(data.shape)
    return data

def splitting_data(data):

    #i am doing EDA
    # i am removing unnecessary columns id  and unbamed32 culumns ,unnamed contain NAN
    data.drop('id', axis=1, inplace=True)
    data.drop('Unnamed: 32', axis=1, inplace=True)

    print(data.shape)

    print(data.head())

    print(data['diagnosis'].unique())

    X=data.drop('diagnosis', axis=1)

    y=data["diagnosis"]

    X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 42 , test_size = 0.2 , shuffle = True , stratify = y)

    print(X_train.shape , X_test.shape , y_train.shape , y_test.shape)

    return X_train, X_test, y_train, y_test

from sklearn.metrics import confusion_matrix

def Model_training_lasso():


    X_train, X_test, y_train, y_test = splitting_data(data)
    le=LabelEncoder()
    y_train=le.fit_transform(y_train)
    y_test=le.transform(y_test)
    model = LogisticRegression(penalty='l1', solver='liblinear',max_iter=10000)
    print(type(model))
    model.fit(X_train,y_train)
    y_predict = model.predict(X_test)
    print(y_predict)
    confu=confusion_matrix(y_test,y_predict)
    print('confussion matric lasso_classifier:', confu)




def Model_training_Ridge():


    X_train, X_test, y_train, y_test = splitting_data(data)
    le=LabelEncoder()
    y_train=le.fit_transform(y_train)
    y_test=le.transform(y_test)
    model = RidgeClassifier()

    model.fit(X_train,y_train)

    y_predict = model.predict(X_test)

    print(y_predict)

    confu=confusion_matrix(y_test,y_predict)
    print('confussion matric_Ridge_classifier:', confu)


Model_training_lasso()
#Model_training_Ridge()

#Note: please do run Model_training_lasso() and comment as Model_training_Ridge()
# then ofter do run Model_training_Ridge() and comment as Model_training_lasso() other error will come