import pandas as pd
data=pd.read_csv('simulated_data_multiple_linear_regression_for_ML.csv')
print(data.head())
titha = [1,1,1,1,1,1]
#Form x and y (disease_score_fluct)

#/home/sails/

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
# titha=[0.5,0.5,0.5,0.6,6,0.8]
print('titha:',titha)
def feature_scaling(data):
   # titha = [0.5, 0.5, 0.5, 0.6, 6, 0.8]
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
   return features_train,features_test,titha


#Write a function to compute hypothesis

def hypothes(titha,features_train):
    # titha = [1, 1, 1, 1, 1, 1]
    features_train,features_test=feature_scaling(data)

    hypothesis=[]
    y_pred_value = []
    for k in range(len(features_train[0])):
        hypothesis_train = sum([titha[i] * features_train[i][k] for i in range(len(titha))])
        hypothesis.append(hypothesis_train)



    print(len(hypothesis))
    print((hypothesis))
    print(len(target_train))

    # for k in range(len(features_test[0])):
    #     y_pred = sum([titha[i] * features_test[i][k] for i in range(len(titha))])
    #     y_pred_value.append(y_pred)
    #
    # print('x',y_pred_value)
    # print(len(y_pred_value))
    # return y_pred_value,hypothesis,features_train
    return hypothesis

def cost_function(hypothesis,target_train):


    y_pred_value,hypothesis,features_train=hypothes(titha,features_train)

    cost_fun = sum([(i - j) ** 2 for i, j in zip(hypothesis,target_train)])
    print(cost_fun)


    cost_j=(1/2)*(cost_fun)

    print('cost function',cost_j)
    return cost_j


def cost_derivation(hypothesis):
    cost_j=cost_function(hypothesis,target_train)
    y_pred_value, hypothesis, features_train = hypothes(titha)

    cos_derivation = []

    n=[(hypothesis[l]-target_train[l])for l in range(len(hypothesis))]


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


def get_new_thita(titha,sum_derivation):

    sum_derivation=cost_derivation(hypothesis)

    alph=0.00001
    titha=[titha[i]-alph*sum_derivation[i] for i in range(len(titha))]
    print(titha)

    feature_scaling(data)
    hypothes(titha,features_train)
    cost_function(hypothesis)
    cost_derivation(hypothesis)

    print(cost_j)
    # print('new', cost_j)
    # print('new titha:',titha)

# def gradian_discent():
#     new_thita=get_new_thita()
#     print(new_thita)

#
#
#
#
    # y_pred_value,hypothesis,features_train=hypothes(new_thita)
    #
    #
    # hypothesis,features_train,cost_j=cost_function()
    # print('new',cost_j)
        # sum_derivation=cost_derivation()
        # new_thita=get_new_thita()
        # print(new_thita)
        # if cost_j<10:
        #     print(new_thita)
        #     break





get_new_thita(titha,sum_derivation)
