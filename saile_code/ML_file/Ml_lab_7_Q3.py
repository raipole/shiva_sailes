
#Implement bagging regressor and classifier using scikit-learn. Use diabetes and iris datasets.



from pandas.core.interchange import dataframe
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import load_diabetes
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold,cross_val_score
from sklearn.metrics import r2_score
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def load_data():
    # i am saparating features and target features
    [X,y]=load_diabetes(return_X_y=True)


    dat = pd.DataFrame(X) # i am tried this way but is not workin asking 2-d data

    X=dat[[2]]

    return X,y




def mymain_regression():

    [X,y]=load_data()

    model = BaggingRegressor()

    k_fold = KFold(n_splits=10,shuffle=True,random_state=88)

    score=cross_val_score(model,X,y,cv=k_fold)

    print('10_fold cross validition:',score)
    print('mean r2 score of 10 fold:',score.mean())

    print('std r2 score of 10 fold:',score.std())
#


def iris_data():
    # i am saparating features and target features
    [X,y]=load_diabetes(return_X_y=True)


    dat = pd.DataFrame(X) # i am tried this way but is not workin asking 2-d data

    X=dat[[2]]

    return X,y
def my_main_classification():
    X,y=iris_data()

    x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=99)

    bagging_model = BaggingClassifier(n_estimators=50, random_state=42)

# 2. Train the model
    bagging_model.fit(x_train, y_train)

# 3. Method A: Get accuracy directly using .score()
    accuracy_direct = bagging_model.score(x_test, y_test)
    print(f"Direct Accuracy: {accuracy_direct}")

# 3. Method B: Get accuracy using accuracy_score function
    y_pred = bagging_model.predict(x_test)
    accuracy_metric = accuracy_score(y_test, y_pred)
    print(f"Metric Accuracy: {accuracy_metric}")
#
#
def my_main():
    mymain_regression()
    my_main_classification()
# #
# #
# #
if __name__ == '__main__':
    my_main()