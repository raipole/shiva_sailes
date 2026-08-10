from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

import pandas as pd
#
import pandas as pd
df = pd.read_csv('~/shiva_sailes/simulated_data_multiple_linear_regression_for_ML.csv')

print(df.head())

def dat_linear():


    X = df.drop("disease_score",axis=1) # i am saparating all rows and all columns  target

    y = df["disease_score"] # i am isolating target labels

    return X,y

def my_main():
    X,y=dat_linear()

    x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=99)

    model = DecisionTreeRegressor(random_state=99)

    model.fit(x_train,y_train)

    y_pred=model.predict(x_test)

    r2=r2_score(y_test,y_pred)

    print('r scor is %0.2f'% r2)

if __name__=='__main__':
    my_main()