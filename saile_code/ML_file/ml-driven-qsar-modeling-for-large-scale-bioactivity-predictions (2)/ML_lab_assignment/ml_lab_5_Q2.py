# Compute the derivative of a sigmoid function and visualize it

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