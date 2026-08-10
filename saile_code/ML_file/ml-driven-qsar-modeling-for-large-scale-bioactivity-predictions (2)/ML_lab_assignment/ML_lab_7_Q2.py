#Implement a classification decision tree algorithm using scikit-learn for the sonar  dataset.
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


import pandas as pd
#
import pandas as pd
df = pd.read_csv('/home/sails/shiva_sailes/saile_code/ML_file/archive(3) (2)/sonar.csv')

print(df.head())
print(df.columns)

def dat_linear():


    X = df.drop("R",axis=1) # i am saparating all rows and all columns  target

    y = df["R"] # i am isolating target labels

    return X,y

def my_main():
    X,y=dat_linear()

    x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=99)

    model = DecisionTreeClassifier(random_state=99)

    model.fit(x_train,y_train)

    y_pred=model.predict(x_test)

    accuracy=accuracy_score(y_test,y_pred)

    print('accuracy is %0.2f'% accuracy)

if __name__=='__main__':
    my_main()