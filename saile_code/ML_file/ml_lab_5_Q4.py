
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