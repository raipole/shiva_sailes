import numpy as np
from pandas.core.interchange import dataframe
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
from sklearn.model_selection import KFold,cross_val_score
from sklearn.metrics import r2_score
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    # i am saparating features and target features
    [X,y]=load_diabetes(return_X_y=True)


    dat = pd.DataFrame(X) # i am tried this way but is not workin asking 2-d data

    X=dat[[2]]

    return X,y




def mymain():

    [X,y]=load_data()

    model = LinearRegression()

    k_fold = KFold(n_splits=10,shuffle=True,random_state=88)

    score=cross_val_score(model,X,y,cv=k_fold)

    print('10_fold cross validition:',score)
    print('mean r2 score of 10 fold:',score.mean())

    print('std r2 score of 10 fold:',score.std())

#
#
# # A2.a dot product of two vectors

x=[2,1,2]
y=[1,2,3]

def dot_product_A2_a(x,y):

    # i am finding dot product of two vectors by using list compression
    dot_product = sum([x[i]*y[i] for i in range(len(x))])

    print('dot product of two vectors:',dot_product)


#A2.b implement  function in plot


def plot_A2_b():
    x=[]
    a = -10
    # i am creating 100 numbers  between -10 to 10 by for loop
    for i in range(0, 100):
        b = a + 0.2

        x.append(b)
        a=b
        if b==10:
            break

 # i am substuting values in function


    y=[((3*i**2)-(2*i)+1.5) for i in x]

# i am plot x values and function values
    plt.plot(x,y)
    plt.show()
#
#
#
def my_main():
    model_avalution_A1()
    dot_product_A2_a(x, y)
    plot_A2_b()
#
# #
# #
# #
if __name__ == '__main__':
    mymain()
#
[X,y]=load_diabetes(return_X_y=True, as_frame=True)
dat = pd.DataFrame(X)

# X=dat.iloc[:,2:3]
# X_3 = X[-['bmi']]
# print(type(X['bmi']))
# print('x',X.columns)
#
# model = LinearRegression()
# model.fit(X_3,y)
# y_pred = model.predict(X_3)
#
# r2 = r2_score(y, y_pred)
# print('r2',r2)


