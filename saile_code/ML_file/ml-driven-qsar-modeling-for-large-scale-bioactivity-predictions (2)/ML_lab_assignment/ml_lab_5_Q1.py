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



#from Ml_lab_4 import features_train

#
# def mload_data(file='simulated_data_multiple_linear_regression_for_ML.csv',target='disease_score_fluct'):
#
#     data=pd.read_csv(file)
#     print(data.head())
#     print(data.shape)
#
#     #Form x and y (disease_score_fluct)
#
#     #/home/sails/
#
#     m=int(round(((data.shape[0]*80)/100),2))
#     q=int(round(((data.shape[0]*20)/100),2))
#
#     # i am going to saparete 70% target variable for train
#     target_train=list(data[target][: m])
#     target_test=list(data[target][: q])
#     print(len(target_train))
#     print(len(target_test))
#     # i am going to saparet 70% train data and 30% test data
#     features=['age','BMI','BP','blood_sugar','Gender','disease_score']
#     # titha=[0.5,0.5,0.5,0.6,6,0.8]
#     # print('titha:',titha)
#     # func=mload_data(file='simulated_data_multiple_linear_regression_for_ML.csv',target='target')
#
# # def feature_scaling(func):
#     features_train = []
#     features_test = []
#    # titha = [0.5, 0.5, 0.5, 0.6, 6, 0.8]
#     titha = [1, 2, 3, 4, 1, 1]
#     for i in features:
#         lis=list(data[i][:m])
#         features_train.append(lis)
#         lis1 = list(data[i][:q])
#         features_test.append(lis1)
#
#
#
#     print('number of elements or rows:',len(features_train[0]))
#     print('length of feature_matrics:', len(features_train))
#     print('number of elements or rows:', len(features_test[0]))
#     print('length of feature_matrics:', len(features_test))
#     print('t',target_train)
#func=mload_data(file='simulated_data_multiple_linear_regression_for_ML.csv',target='target')
#     return features,target_train,target_test,features_train,features_test,titha
#
#
# #Write a function to compute hypothesis
# def hypothesis_fun():
#     features, target_train, target_test, features_train, features_test, titha=mload_data(file='simulated_data_multiple_linear_regression_for_ML.csv',target='disease_score_fluct')
#     y_pred_value = []
#     # while True:
#     hypothesis = []
#     for k in range(len(features_train[0])):
#         hypothesis_train = sum([titha[i] * features_train[i][k] for i in range(len(titha))])
#         hypothesis.append(hypothesis_train)
#
#
#     print(hypothesis)
#     return features, target_train, target_test, features_train, features_test, titha,hypothesis
#
#
# #       y_pred_value = []
# #     # for k in range(len(features_test[0])):
# #     #     y_pred = sum([titha[i] * features_test[i][k] for i in range(len(titha))])
# #     #     y_pred_value.append(y_pred)
# #     #
# #     # print('x',y_pred_value)
# #     # print(len(y_pred_value))
# #     # return y_pred_value,hypothesis,features_train
# #     # return hypothesis
# def derivation_function():
#     features, target_train, target_test, features_train, features_test, titha,hypothesis=hypothesis_fun()
#     cost_fun = sum([(i - j) ** 2 for i, j in zip(hypothesis, target_train)])
#     print(cost_fun)
#
#     cost_j = (1 / 2) * (cost_fun)
#
#     print('cost function', cost_j)
#     # return cost_j
#
#     cos_derivation = []
#
#     n = [(hypothesis[l] - target_train[l]) for l in range(len(hypothesis))]
#
#     print('n_len', len(features_train))
#     sum_derivation = []
#
#
#     derivation_thit1 = sum([n[i] * features_train[0][i] for i in range(len(n))])
#     derivation_thit0 = sum([n[i] * features_train[1][i] for i in range(len(n))])
#     derivation_thit2 = sum([n[i] * features_train[2][i] for i in range(len(n))])
#     derivation_thit3 = sum([n[i] * features_train[3][i] for i in range(len(n))])
#     derivation_thit4 = sum([n[i] * features_train[4][i] for i in range(len(n))])
#     derivation_thit5 = sum([n[i] * features_train[5][i] for i in range(len(n))])
#
#     sum_derivation.append(derivation_thit1)
#     sum_derivation.append(derivation_thit0)
#     sum_derivation.append(derivation_thit2)
#     sum_derivation.append(derivation_thit3)
#     sum_derivation.append(derivation_thit4)
#     sum_derivation.append(derivation_thit5)
#
#     print(n)
#
#     print('x', sum_derivation)
#     print(len(sum_derivation))
#     return cost_j,features, target_train, target_test, features_train, features_test, titha, hypothesis, sum_derivation
# def get_new_thita():
#     cost_j,features, target_train, target_test, features_train, features_test, titha, hypothesis, sum_derivation=derivation_function()
#     alph = 0.00000001
#     titha = [titha[i] - alph * sum_derivation[i] for i in range(len(titha))]
#     print(titha)
#
#     print(cost_j)
#. Implement logistic regression using scikit-learn for the breast cancer dataset -
#https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data


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
def Model_training():


    X_train, X_test, y_train, y_test = splitting_data(data)
    le=LabelEncoder()
    y_train=le.fit_transform(y_train)
    y_test=le.transform(y_test)
    model = LogisticRegression(max_iter=10000)
    print(type(model))
    model.fit(X_train,y_train)
    y_predict = model.predict(X_test)
    print(y_predict)
    confu=confusion_matrix(y_test,y_predict)
    print('confussion matric:', confu)




# Model_training()

#     print('new', cost_j)
#     print('new titha:', titha)
#     while True:
#         hypothesis = []
#         cost_first=[0]
#         for k in range(len(features_train[0])):
#             hypothesis_train = sum([titha[i] * features_train[i][k] for i in range(len(titha))])
#             hypothesis.append(hypothesis_train)
#         cost_fun = sum([(i - j) ** 2 for i, j in zip(hypothesis, target_train)])
#         print(cost_fun)
#         cost_j1 = (1 / 2) * (cost_fun)
#         cost_first.append(cost_j1)
#
#         print('cost function', cost_j)
#         n = [(hypothesis[l] - target_train[l]) for l in range(len(hypothesis))]
#
#         print('n_len', len(features_train))
#         sum_derivation = []
#
#         derivation_thit1 = sum([n[i] * features_train[0][i] for i in range(len(n))])
#         derivation_thit0 = sum([n[i] * features_train[1][i] for i in range(len(n))])
#         derivation_thit2 = sum([n[i] * features_train[2][i] for i in range(len(n))])
#         derivation_thit3 = sum([n[i] * features_train[3][i] for i in range(len(n))])
#         derivation_thit4 = sum([n[i] * features_train[4][i] for i in range(len(n))])
#         derivation_thit5 = sum([n[i] * features_train[5][i] for i in range(len(n))])
#
#         sum_derivation.append(derivation_thit1)
#         sum_derivation.append(derivation_thit0)
#         sum_derivation.append(derivation_thit2)
#         sum_derivation.append(derivation_thit3)
#         sum_derivation.append(derivation_thit4)
#         sum_derivation.append(derivation_thit5)
#         titha = [titha[i] - alph * sum_derivation[i] for i in range(len(titha))]
#         diff=cost_first[0]-cost_j
#         ss_tot = sum([i - np.mean(target_train) for i in target_train])
#         r_score = 1 - (cost_fun / ss_tot)
#         if diff >=100:
#             print(cost_j)
#             print('new titha:', titha)
#             print('cost function', cost_job)
#             print('new r_score:', r_score)
#
#             break
#         y_pred_value=[]
#
#         for k in range(len(features_test[0])):
#             y_pred = sum([titha[i] * features_test[i][k] for i in range(len(titha))])
#             y_pred_value.append(y_pred)
#
#         print('x',y_pred_value)
#         cost_f = sum([(i - j) ** 2 for i, j in zip(y_pred_value, target_test)])
#         print(cost_fun)
#         cost_job = (1 / 2) * (cost_f)
#         print(cost_job)
#         ss_tot=sum([i-np.mean(target_test) for i in target_train])
#         r_score=1-(cost_job/ss_tot)
#         print(r_score)
#         plt.plot(target_test, label='Actual', marker='o')
#
#         # Plot predicted values
#         plt.plot(y_pred_value, label='Predicted', marker='x')
#
#         plt.xlabel('Sample')
#         plt.ylabel('Value')
#         plt.title('Actual vs Predicted Values')
#         plt.legend()
#         plt.grid(True)
#         if r_score == 0.5:
#             print(cost_j)
#             print('new titha:', titha)
#             print('cost function', cost_job)
#             print('new r_score:', r_score)
# #rom sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
# #
# #
#             break
#
# hypothesis_fun()
# derivation_function()
# feature_scaling(data)
# mload_data(file='simulated_data_multiple_linear_regression_for_ML.csv',target='disease_score_fluct')
# get_new_thita()


# implimantation of sigmoid function in python

#
#
def sigmoid_function(titha,features_train):
    hypothesis=[]
    regressor_values=[]
    for k in range((features_train.shape[0])):

        # i am making regression values
        scalar = sum([titha[i] * features_train.iloc[k] for i in range(len(titha))])

        regressor_values.append(scalar)

        # converting regression values to probabilistic score
        sigmoid = 1/(1 + np.exp(-scalar))

        hypothesis.append(sigmoid)

    plt.plot(regressor_values,hypothesis)
    # plt.xlabel('Sample')
    # plt.ylabel('Value')
    # plt.title('Actual vs Predicted Values')
    plt.show()

    return hypothesis

data=pd.read_csv('simulated_data_multiple_linear_regression_for_ML.csv')
features_train=data.drop('disease_score_fluct',axis=1)
y_train=data['disease_score_fluct']
titha = [1, 2, 3, 4, 1, 1]
sigmoid_function(titha,features_train)
print(features_train[1:1])
print(features_train.shape[0])




# Compute the derivative of a sigmoid function and visualize it
def sigmoid_derivation(y_train):
    titha = [1, 2, 3, 4, 1, 1]
    # i am infuse above function to continue get operation
    hypothesis =sigmoid_function(titha,features_train)
    derivation=[]
    for k in range((features_train.shape[0])):

       # i am finding diff between ground truth value and hyopethesis(Y-h(thitha)) value of train data
        diff_ground_hypothesis=sum([(y_train[k]-hypothesis)])

       # i am row wise derivation Y-h(thitha))*xj

        row_derivation=sum([diff_ground_hypothesis*i for i in features_train.iloc[k] ])

        derivation.append(row_derivation)
        # regressor_values.append(scalar)
        # sigmoid = 1 / (1 + np.exp(-scalar))
        # hypothesis.append(sigmoid)
    print(derivation)

sigmoid_derivation(y_train)



#. Implement logistic regression using scikit-learn for the breast cancer dataset -
#https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data


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
def Model_training():


    X_train, X_test, y_train, y_test = splitting_data(data)
    le=LabelEncoder()
    y_train=le.fit_transform(y_train)
    y_test=le.transform(y_test)
    model = LogisticRegression(max_iter=10000)
    print(type(model))
    model.fit(X_train,y_train)
    y_predict = model.predict(X_test)
    print(y_predict)
    confu=confusion_matrix(y_test,y_predict)
    print('confussion matric:', confu)




# Model_training()





## implement l2_norm and l1_norm from scratch.


def mload_data(file='simulated_data_multiple_linear_regression_for_ML.csv',target='disease_score_fluct'):

    data=pd.read_csv(file)
    print(data.head())
    print(data.shape)

    #Form x and y (disease_score_fluct)

    #/home/sails/

    m=int(round(((data.shape[0]*80)/100),2))
    q=int(round(((data.shape[0]*20)/100),2))


    # i am going to saparete 70% target variable for train

    target_train=list(data[target][: m])
    target_test=list(data[target][: q])
    print(len(target_train))
    print(len(target_test))
    # i am going to saparet name of columns train data and 30% test data

    features=[i for i in data.columns]
    # i am taking randodom thitha values

    #titha=[i for i in range(len(data.columns))]
    titha = [0.5, 0.5, 0.5, 0.6, 6, 0.8]
    # print('titha:',titha)
    features_train = []
    features_test = []

    for i in features:
        lis=list(data[i][:m])
        features_train.append(lis)
        lis1 = list(data[i][:q])
        features_test.append(lis1)


    return features, target_train, target_test, features_train, features_test, titha

def hypothesis_fun():
    features, target_train, target_test, features_train, features_test, titha = mload_data(file='simulated_data_multiple_linear_regression_for_ML.csv',target='disease_score_fluct')
    y_pred_value = []

    # while True:
    hypothesis = []

    for k in range(len(features_train[0])):
        hypothesis_train = sum([titha[i] * features_train[i][k] for i in range(len(titha))])
        hypothesis.append(hypothesis_train)


    print(hypothesis)
    return features, target_train, target_test, features_train, features_test, titha,hypothesis


#       y_pred_value = []
#     # for k in range(len(features_test[0])):
#     #     y_pred = sum([titha[i] * features_test[i][k] for i in range(len(titha))])
#     #     y_pred_value.append(y_pred)
#     #
#     # print('x',y_pred_value)
#     # print(len(y_pred_value))
#     # return y_pred_value,hypothesis,features_train
#     # return hypothesis

def derivation_function():
    features, target_train, target_test, features_train, features_test, titha,hypothesis=hypothesis_fun()

    # i am adding penalty l2_norm
    lamda=0.01
    cost_fun = sum([(i - j) ** 2 for i, j in zip(hypothesis, target_train)])
    print(cost_fun)

    cost_j = ((1 / 2) * (cost_fun))+lamda*(np.sqrt(sum([i**2 for i in titha])))

    print('cost function', cost_j)
    # return cost_j

    cos_derivation = []

    n = [(hypothesis[l] - target_train[l]) for l in range(len(hypothesis))]

    print('n_len', len(features_train))
    sum_derivation = []


    derivation_thit1 = sum([n[i] * features_train[0][i] for i in range(len(n))])
    derivation_thit0 = sum([n[i] * features_train[1][i] for i in range(len(n))])
    derivation_thit2 = sum([n[i] * features_train[2][i] for i in range(len(n))])
    derivation_thit3 = sum([n[i] * features_train[3][i] for i in range(len(n))])
    derivation_thit4 = sum([n[i] * features_train[4][i] for i in range(len(n))])
    derivation_thit5 = sum([n[i] * features_train[5][i] for i in range(len(n))])

    sum_derivation.append(derivation_thit1)
    sum_derivation.append(derivation_thit0)
    sum_derivation.append(derivation_thit2)
    sum_derivation.append(derivation_thit3)
    sum_derivation.append(derivation_thit4)
    sum_derivation.append(derivation_thit5)

    print(n)

    print('x', sum_derivation)
    print(len(sum_derivation))
    return cost_j,features, target_train, target_test, features_train, features_test, titha, hypothesis, sum_derivation,lamda

def get_new_thita_l2():
    cost_j,features, target_train, target_test, features_train, features_test, titha, hypothesis, sum_derivation,lamda =derivation_function()
    alph = 0.00000001

    titha = [titha[i] - alph * sum_derivation[i] for i in range(len(titha))]
    print(titha)

    print(cost_j)
    print('new', cost_j)
    print('new titha:', titha)

    while True:
        hypothesis = []
        cost_first=[0]
        for k in range(len(features_train[0])):
            hypothesis_train = sum([titha[i] * features_train[i][k] for i in range(len(titha))])
            hypothesis.append(hypothesis_train)
        cost_fun = sum([(i - j) ** 2 for i, j in zip(hypothesis, target_train)])
        print(cost_fun)
        cost_j1 = ((1 / 2) * (cost_fun))+lamda*(np.sqrt(sum([i**2 for i in titha])))
        cost_first.append(cost_j1)

        print('cost function', cost_j)
        n = [(hypothesis[l] - target_train[l]) for l in range(len(hypothesis))]

        print('n_len', len(features_train))
        sum_derivation = []

        derivation_thit1 = sum([n[i] * features_train[0][i] for i in range(len(n))])
        derivation_thit0 = sum([n[i] * features_train[1][i] for i in range(len(n))])
        derivation_thit2 = sum([n[i] * features_train[2][i] for i in range(len(n))])
        derivation_thit3 = sum([n[i] * features_train[3][i] for i in range(len(n))])
        derivation_thit4 = sum([n[i] * features_train[4][i] for i in range(len(n))])
        derivation_thit5 = sum([n[i] * features_train[5][i] for i in range(len(n))])

        sum_derivation.append(derivation_thit1)
        sum_derivation.append(derivation_thit0)
        sum_derivation.append(derivation_thit2)
        sum_derivation.append(derivation_thit3)
        sum_derivation.append(derivation_thit4)
        sum_derivation.append(derivation_thit5)
        titha = [titha[i] - alph * sum_derivation[i] for i in range(len(titha))]
        diff=cost_first[0]-cost_j
        ss_tot = sum([i - np.mean(target_train) for i in target_train])
        r_score = 1 - (cost_fun / ss_tot)
        if diff >=100:
            print(cost_j)
            print('new titha:', titha)
            print('cost function', cost_job)
            print('new r_score:', r_score)

            break
        y_pred_value=[]

        for k in range(len(features_test[0])):
            y_pred = sum([titha[i] * features_test[i][k] for i in range(len(titha))])
            y_pred_value.append(y_pred)

        print('x',y_pred_value)
        cost_f = sum([(i - j) ** 2 for i, j in zip(y_pred_value, target_test)])
        print(cost_fun)
        cost_job = (1 / 2) * (cost_f)
        print(cost_job)
        ss_tot=sum([i-np.mean(target_test) for i in target_train])
        r_score=1-(cost_job/ss_tot)
        print(r_score)

        if r_score == 0.5:
            print(cost_j)
            print('new titha:', titha)
            print('cost function', cost_job)
            print('new r_score:', r_score)

get_new_thita_l2()



## implement l2_norm  from scratch.


def mload_data(file='simulated_data_multiple_linear_regression_for_ML.csv',target='disease_score_fluct'):

    data=pd.read_csv(file)
    print(data.head())
    print(data.shape)

    #Form x and y (disease_score_fluct)

    #/home/sails/

    m=int(round(((data.shape[0]*80)/100),2))
    q=int(round(((data.shape[0]*20)/100),2))


    # i am going to saparete 70% target variable for train

    target_train=list(data[target][: m])
    target_test=list(data[target][: q])
    print(len(target_train))
    print(len(target_test))
    # i am going to saparet name of columns train data and 30% test data

    features=[i for i in data.columns]
    # i am taking randodom thitha values

    #titha=[i for i in range(len(data.columns))]
    titha = [0.5, 0.5, 0.5, 0.6, 6, 0.8]
    # print('titha:',titha)
    features_train = []
    features_test = []

    for i in features:
        lis=list(data[i][:m])
        features_train.append(lis)
        lis1 = list(data[i][:q])
        features_test.append(lis1)


    return features, target_train, target_test, features_train, features_test, titha

def hypothesis_fun():
    features, target_train, target_test, features_train, features_test, titha = mload_data(file='simulated_data_multiple_linear_regression_for_ML.csv',target='disease_score_fluct')
    y_pred_value = []

    # while True:
    hypothesis = []

    for k in range(len(features_train[0])):
        hypothesis_train = sum([titha[i] * features_train[i][k] for i in range(len(titha))])
        hypothesis.append(hypothesis_train)


    print(hypothesis)
    return features, target_train, target_test, features_train, features_test, titha,hypothesis


#       y_pred_value = []
#     # for k in range(len(features_test[0])):
#     #     y_pred = sum([titha[i] * features_test[i][k] for i in range(len(titha))])
#     #     y_pred_value.append(y_pred)
#     #
#     # print('x',y_pred_value)
#     # print(len(y_pred_value))
#     # return y_pred_value,hypothesis,features_train
#     # return hypothesis

def derivation_function():
    features, target_train, target_test, features_train, features_test, titha,hypothesis=hypothesis_fun()

    # i am adding penalty l1_norm
    lamda=0.01
    cost_fun = sum([(i - j) ** 2 for i, j in zip(hypothesis, target_train)])
    print(cost_fun)

    cost_j = ((1 / 2) * (cost_fun))+lamda*(np.sqrt(sum([abs(i) for i in titha])))

    print('cost function', cost_j)
    # return cost_j

    cos_derivation = []

    n = [(hypothesis[l] - target_train[l]) for l in range(len(hypothesis))]

    print('n_len', len(features_train))
    sum_derivation = []


    derivation_thit1 = sum([n[i] * features_train[0][i] for i in range(len(n))])
    derivation_thit0 = sum([n[i] * features_train[1][i] for i in range(len(n))])
    derivation_thit2 = sum([n[i] * features_train[2][i] for i in range(len(n))])
    derivation_thit3 = sum([n[i] * features_train[3][i] for i in range(len(n))])
    derivation_thit4 = sum([n[i] * features_train[4][i] for i in range(len(n))])
    derivation_thit5 = sum([n[i] * features_train[5][i] for i in range(len(n))])

    sum_derivation.append(derivation_thit1)
    sum_derivation.append(derivation_thit0)
    sum_derivation.append(derivation_thit2)
    sum_derivation.append(derivation_thit3)
    sum_derivation.append(derivation_thit4)
    sum_derivation.append(derivation_thit5)

    print(n)

    print('x', sum_derivation)
    print(len(sum_derivation))
    return cost_j,features, target_train, target_test, features_train, features_test, titha, hypothesis, sum_derivation,lamda

def get_new_thita_l1():
    cost_j,features, target_train, target_test, features_train, features_test, titha, hypothesis, sum_derivation,lamda =derivation_function()
    alph = 0.00000001

    titha = [titha[i] - alph * sum_derivation[i] for i in range(len(titha))]
    print(titha)

    print(cost_j)
    print('new', cost_j)
    print('new titha:', titha)

    while True:
        hypothesis = []
        cost_first=[0]
        for k in range(len(features_train[0])):

            hypothesis_train = sum([titha[i] * features_train[i][k] for i in range(len(titha))])
            hypothesis.append(hypothesis_train)

        cost_fun = sum([(i - j) ** 2 for i, j in zip(hypothesis, target_train)])
        print(cost_fun)

        cost_j1 = ((1 / 2) * (cost_fun))+lamda*(np.sqrt(sum([abs(i) for i in titha])))
        cost_first.append(cost_j1)

        print('cost function', cost_j)
        n = [(hypothesis[l] - target_train[l]) for l in range(len(hypothesis))]

        print('n_len', len(features_train))
        sum_derivation = []

        derivation_thit1 = sum([n[i] * features_train[0][i] for i in range(len(n))])
        derivation_thit0 = sum([n[i] * features_train[1][i] for i in range(len(n))])
        derivation_thit2 = sum([n[i] * features_train[2][i] for i in range(len(n))])
        derivation_thit3 = sum([n[i] * features_train[3][i] for i in range(len(n))])
        derivation_thit4 = sum([n[i] * features_train[4][i] for i in range(len(n))])
        derivation_thit5 = sum([n[i] * features_train[5][i] for i in range(len(n))])

        sum_derivation.append(derivation_thit1)
        sum_derivation.append(derivation_thit0)
        sum_derivation.append(derivation_thit2)
        sum_derivation.append(derivation_thit3)
        sum_derivation.append(derivation_thit4)
        sum_derivation.append(derivation_thit5)

        titha = [titha[i] - alph * sum_derivation[i] for i in range(len(titha))]
        diff=cost_first[0]-cost_j

        ss_tot = sum([i - np.mean(target_train) for i in target_train])
        r_score = 1 - (cost_fun / ss_tot)

        if diff >=100:
            print(cost_j)
            print('new titha:', titha)
            print('cost function', cost_job)
            print('new r_score:', r_score)

            break
        y_pred_value=[]

        for k in range(len(features_test[0])):
            y_pred = sum([titha[i] * features_test[i][k] for i in range(len(titha))])
            y_pred_value.append(y_pred)

        print('x',y_pred_value)
        cost_f = sum([(i - j) ** 2 for i, j in zip(y_pred_value, target_test)])
        print(cost_fun)
        cost_job = (1 / 2) * (cost_f)
        print(cost_job)
        ss_tot=sum([i-np.mean(target_test) for i in target_train])
        r_score=1-(cost_job/ss_tot)
        print(r_score)

        if r_score == 0.5:
            print(cost_j)
            print('new titha:', titha)
            print('cost function', cost_job)
            print('new r_score:', r_score)

get_new_thita_l1()


def my_main():
