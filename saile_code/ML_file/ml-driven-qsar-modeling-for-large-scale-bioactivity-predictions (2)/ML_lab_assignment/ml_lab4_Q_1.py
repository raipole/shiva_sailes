import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('simulated_data_multiple_linear_regression_for_ML.csv')
print(data.head())

#Form x and y (disease_score_fluct)

#/home/sails/

m=int(round(((len(data['disease_score_fluct'])*80)/100),2))
q=int(round(((len(data['disease_score_fluct'])*20)/100),2))

# i am going to saparete 70% target variable for train
target_train=list(data['disease_score_fluct'][: m])
target_test=list(data['disease_score_fluct'][: q])
print(len(target_train))
print(len(target_test))
# i am going to saparet 70% train data and 30% test data
features=['age','BMI','BP','blood_sugar','Gender','disease_score']
# titha=[0.5,0.5,0.5,0.6,6,0.8]
# print('titha:',titha)
def feature_scaling(data):
    features_train = []
    features_test = []
   # titha = [0.5, 0.5, 0.5, 0.6, 6, 0.8]
    titha = [1, 2, 3, 4, 1, 1]
    for i in features:
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

    sum_derivation.append(derivation_thit1)
    sum_derivation.append(derivation_thit0)
    sum_derivation.append(derivation_thit2)
    sum_derivation.append(derivation_thit3)
    sum_derivation.append(derivation_thit4)
    sum_derivation.append(derivation_thit5)

    print(n)

    print('x', sum_derivation)
    print(len(sum_derivation))

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
        plt.plot(target_test, label='Actual', marker='o')

        # Plot predicted values
        plt.plot(y_pred_value, label='Predicted', marker='x')

        plt.xlabel('Sample')
        plt.ylabel('Value')
        plt.title('Actual vs Predicted Values')
        plt.legend()
        plt.grid(True)
        if r_score == 0.5:
            print(cost_j)
            print('new titha:', titha)
            print('cost function', cost_job)
            print('new r_score:', r_score)



            break


feature_scaling(data)