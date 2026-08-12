#1Implement a linear regression model using scikit-learn for the simulated dataset - simulated_data_multiple_linear_regression_for_ML.csv
# - to predict the “disease_score” from multiple clinical parameters.
from pandas.core.interchange import column
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

import pandas as pd
from sklearn.preprocessing import StandardScaler

# data=pd.read_csv('simulated_data_multiple_linear_regression_for_ML.csv')
# def dis_score():
#
#
#     print(data.head())
#     print(data.shape)
#     x=data.drop(columns=['disease_score'])
#     y=data['disease_score']
#     return x,y
#
# def main():
#
#     x,y=dis_score()
#     x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=99)
#
#     model=LinearRegression()
#     model.fit(x_train,y_train)
#     y_pred=model.predict(x_test)
#     r_scor=r2_score(y_test,y_pred)
#
#     print(round(r_scor,2))
#
# main()
#
#
# #2Implement a linear regression model using scikit-learn for the simulated dataset - simulated_data_multiple_linear_regression_for_ML.csv
# # - to predict the “disease_score_fluct” from multiple clinical parameters.
#
# data=pd.read_csv('simulated_data_multiple_linear_regression_for_ML.csv')
# def dis_score():
#
#
#     print(data.head())
#     print(data.shape)
#     x=data.drop(columns=['disease_score_fluct'])
#     y=data['disease_score_fluct']
#     return x,y
#
# def main():
#
#     x,y=dis_score()
#     x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=99)
#
#     model=LinearRegression()
#     model.fit(x_train,y_train)
#     y_pred=model.predict(x_test)
#     r_scor=r2_score(y_test,y_pred)
#
#     print(round(r_scor,2))
#
# main()
#
# 3Use the above simulated CSV file and implement the following from scratch in Python
# Read simulated data csv file
# Form x and y (disease_score_fluct)
# Write a function to compute hypothesis
# Write a function to compute the cost
# Write a function to compute the derivative
# Write update parameters logic in the main function
#
# Read simulated data csv file

data=pd.read_csv('simulated_data_multiple_linear_regression_for_ML.csv')
print(data.head())

#Form x and y (disease_score_fluct)



m=int(round(((len(data['disease_score_fluct'])*70)/100),2))
n=int(round(((len(data['disease_score_fluct'])*30)/100),2))

# i am going to saparete 70% target variable for train
target_train=list(data['disease_score_fluct'][: m])
target_test=list(data['disease_score_fluct'][: n])
print(len(target_train))
print(len(target_test))

features_train=[]
features_test=[]

# i am going to saparet 70% train data and 30% test data
features=['age','BMI','BP','blood_sugar','Gender','disease_score']
titha=[i for i in range(1,7)]
def feature_scaling(data):
   for i in features:
       lis=list(data[i][:m])
       features_train.append(lis)
       lis1 = list(data[i][:n])
       features_test.append(lis1)



   print('number of elements or rows:',len(features_train[0]))
   print('length of feature_matrics:', len(features_train))
   print('number of elements or rows:', len(features_test[0]))
   print('length of feature_matrics:', len(features_test))
   print('t',target_train)
   return features_train,features_test


#Write a function to compute hypothesis

def hypothes():
    features_train, features_test=feature_scaling(data)
    titha=[i for i in range(1,7)]
    print(titha)
    hypothesis=[]
    y_pred_value = []
    for k in range(len(features_train[0])):
        hypothesis_train = sum([titha[i] * features_train[i][k] for i in range(len(titha))])
        hypothesis.append(hypothesis_train)



    print(len(hypothesis))
    print((hypothesis))
    print(len(target_train))

    for k in range(len(features_test[0])):
        y_pred = sum([titha[i] * features_test[i][k] for i in range(len(titha))])
        y_pred_value.append(y_pred)

    print('x',y_pred_value)
    print(len(y_pred_value))
    return y_pred_value,hypothesis,features_train

def cost_function():


    y_pred_value,hypothesis,features_train=hypothes()
    cost = []
    cost_fun = sum([(i - j) ** 2 for i, j in zip(target_test, y_pred_value)])
    print(cost_fun)

    print(cost)
    cost_j=(1/2)*(cost_fun)

    print(cost_j)
    return hypothesis,features_train


def cost_derivation():
    hypothesis,features_train=cost_function()

    cos_derivation = []

    n=[(hypothesis[l]-target_train[l])for l in range(len(hypothesis))]
    print((features_train))

    print('n_len',len(features_train))
    sum_derivation=[]

    derivation_thit1 =sum([n[i]*features_train[0][i] for i in range(len(n))])
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
    # print(len(n))

    # print(len(derivation))
    print('x',sum_derivation)
    print(len(sum_derivation))
    return sum_derivation


def get_new_thita():

    sum_derivation=cost_derivation()

    alph=0.001
    new_thita=[ titha[i]-alph*sum_derivation[i] for i in range(len(titha))]


    print(new_thita)




get_new_thita()
