import random
import pandas as pd
from pandas.core.array_algos.masked_reductions import mean
import numpy as np
from pandas.core.interchange import column
data=pd.read_csv('simulated_data_multiple_linear_regression_for_ML.csv')
print(data.head())


def stochastic_gradient_descent(data):
    features_train = []
    features_test = []
    # titha = [0.5, 0.5, 0.5, 0.6, 6, 0.8]
    titha = [0.1, 0.01, 0.1, 0.1, 0.001, 0.001]
    for i in features:
        lis = list(data[i][:m])
        features_train.append(lis)
        lis1 = list(data[i][:q])
        features_test.append(lis1)

    print('number of elements or rows:', len(features_train[0]))
    print('length of feature_matrics:', len(features_train))
    print('number of elements or rows:', len(features_test[0]))
    print('length of feature_matrics:', len(features_test))
    print('t', target_train)

    # Write a function to compute hypothesis

    y_pred_value = []
    # while True:


    # for k in range(len(features_test[0])):
    #     y_pred = sum([titha[i] * features_test[i][k] for i in range(len(titha))])
    #     y_pred_value.append(y_pred)
    #
    # print('x',y_pred_value)
    # print(len(y_pred_value))
    # return y_pred_value,hypothesis,features_train
    # return hypothesis

    while True:
        b=random.randrange(1,m+1)
        hypothesis = []
        cost_first = [0]
        # for k in range(len(features_train[0])):
        hypothesis_train = sum([titha[i] * features_train[i][b] for i in range(len(titha))])
        hypothesis.append(hypothesis_train)
        cost_fun = hypothesis_train-target_train[b]#sum([(i - j) ** 2 for i, j in zip(hypothesis_train,target_train[b])])
        print(cost_fun)
        cost_j1 = (1 / 2) * (cost_fun)
        print(cost_j1)
        # cost_first.append(cost_j1)

        print('cost function', cost_j1)
        n = [(hypothesis[0] - target_train[b])] #for l in range(len(hypothesis))]

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
        alph = 0.000000000001
        titha = [titha[i] - alph * sum_derivation[i] for i in range(len(titha))]
        print(titha)
        b = random.randrange(1, m + 1)
        hypothesis = []
        cost_first = [0]
        # for k in range(len(features_train[0])):
        hypothesis_train = sum([titha[i] * features_train[i][b] for i in range(len(titha))])
        hypothesis.append(hypothesis_train)
        cost_fun = hypothesis_train - target_train[
            b]  # sum([(i - j) ** 2 for i, j in zip(hypothesis_train,target_train[b])])
        print(cost_fun)
        cost_j2 = (1 / 2) * (cost_fun)
        print(cost_j2)
        # cost_first.append(cost_j1)

        print('cost function', cost_j1)
        n = [(hypothesis[0] - target_train[b])]  # for l in range(len(hypothesis))]

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
        print(titha)
        diff = cost_j1 - cost_j2
        if diff < 0.00001:
            print(cost_j2)
            print('new titha:', titha)



            break


# stochastic_gradient_descent(data)

from sklearn.datasets import fetch_california_housing
[X,y]=fetch_california_housing(return_X_y=True)
print('v',y)
df=pd.DataFrame(X,y)
print('d',df.head())




# i am going to saparet 70% train data and 30% test data
# features=[i for i in X.column_tolist()]
# print(features)
feature_names = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "AveBedrms",
    "Population",
    "AveOccup",
    "Latitude",
    "Longitude",
]
df=pd.DataFrame(X,columns=feature_names)
df['target']=y

print(df.columns.tolist())

m=int(round(((len(df['target'])*80)/100),2))
q=int(round(((len(df['target'])*20)/100),2))
print(m,q)

# i am going to saparete 70% target variable for train
target_train=list(df['target'][: m])
target_test=list(df['target'][: q])
print(len(target_train))
print(len(target_test))
def feature_scaling_california(data=df):
    features_train = []
    features_test = []

    titha = [40,50, 30, 20, 0.1, 0.2, 0.001, 0.3]
    for i in feature_names:
        lis=list(data[i][:m])
        features_train.append(lis)
        lis1 = list(data[i][:q])
        features_test.append(lis1)



    print('number of elements or rows:',len(features_train[0]))
    print('length of feature_matrics:', len(features_train))
    print('number of elements or rows:', len(features_test[0]))
    print('length of feature_matrics:', len(features_test))
    print('t',target_train)


    #Write a function to compute hypothesis


    y_pred_value = []
    # while True:
    hypothesis = []
    for k in range(len(features_train[0])):
        hypothesis_train = sum([titha[i] * features_train[i][k] for i in range(len(titha))])
        hypothesis.append(hypothesis_train)


    print((hypothesis))


    # for k in range(len(features_test[0])):
    #     y_pred = sum([titha[i] * features_test[i][k] for i in range(len(titha))])
    #     y_pred_value.append(y_pred)
    #
    # print('x',y_pred_value)
    # print(len(y_pred_value))
    # return y_pred_value,hypothesis,features_train
    # return hypothesis

    cost_fun = sum([(i - j) ** 2 for i, j in zip(hypothesis, target_train)])
    print(cost_fun)

    cost_j = (1 / 2) * (cost_fun)

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
    derivation_thit5 = sum([n[i] * features_train[5][i] for i in range(len(n))])
    derivation_thit6 = sum([n[i] * features_train[6][i] for i in range(len(n))])
    derivation_thit7 = sum([n[i] * features_train[7][i] for i in range(len(n))])

    sum_derivation.append(derivation_thit1)
    sum_derivation.append(derivation_thit0)
    sum_derivation.append(derivation_thit2)
    sum_derivation.append(derivation_thit3)
    sum_derivation.append(derivation_thit4)
    sum_derivation.append(derivation_thit5)
    sum_derivation.append(derivation_thit6)
    sum_derivation.append(derivation_thit7)


    print(n)

    print('x', sum_derivation)
    print(len(sum_derivation))

    alph = 0.000000000001
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
        cost_j1 = (1 / 2) * (cost_fun)
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
        derivation_thit6 = sum([n[i] * features_train[6][i] for i in range(len(n))])
        derivation_thit7 = sum([n[i] * features_train[7][i] for i in range(len(n))])

        sum_derivation.append(derivation_thit1)
        sum_derivation.append(derivation_thit0)
        sum_derivation.append(derivation_thit2)
        sum_derivation.append(derivation_thit3)
        sum_derivation.append(derivation_thit4)
        sum_derivation.append(derivation_thit5)
        sum_derivation.append(derivation_thit6)
        sum_derivation.append(derivation_thit7)

        titha = [titha[i] - alph * sum_derivation[i] for i in range(len(titha))]
        diff=cost_first[0]-cost_j
        for k in range(len(features_test[0])):
            y_pred = sum([titha[i] * features_test[i][k] for i in range(len(titha))])
            y_pred_value.append(y_pred)

        print('x',y_pred_value)
        cost_f = sum([(i - j) ** 2 for i, j in zip(hypothesis, target_train)])
        print(cost_fun)
        cost_job = (1 / 2) * (cost_f)
        print(cost_job)
        ss_tot=sum([i-np.mean(target_test) for i in target_train])
        r_score=1-(cost_job/ss_tot)
        # return y_pred_value,hypothesis,features_train
        # return hypothesis
        if r_score == 0.5:
            print(cost_j)
            print('new titha:', titha)
            print('cost function', cost_job)
            print('new r_score:', r_score)
            break





feature_scaling_california(df)


# from sklearn.linear_model import LinearRegression
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import r2_score
#
# def load_data():
#     [X,y]=fetch_california_housing(return_X_y=True)
#     return [X,y]
#
#
#
#     print('Hello')
# def mymain():
#     [X,y]=load_data()
#     # spliting data 70% of training and 30% for test
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=999)
#
#     print('----TRAINING-----''')