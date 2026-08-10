from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def load_data():
    [X,y]=fetch_california_housing(return_X_y=True)
    return [X,y]


def mymain():
    [X,y]=load_data()

    x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=40)

    print('n=%d'% len(X))

    print('....training.....')

    model=LinearRegression()
    model.fit(x_train,y_train)

    y_pred=model.predict(x_test)

    r_score=r2_score(y_test,y_pred)
    print('r2 score is %0.2f'% r_score)
    print(r_score)


if __name__=="__main__":
    mymain()
#
#
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# def dataset():
#     [X,y]=fetch_california_housing(return_X_y=True)
#     return [X,y]
#
#
# def main():
#     [X,y]=dataset()
#     x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=99)
#     model=LinearRegression()
#     model.fit(x_train,y_train)
#     y_pred=model.predict(x_test)
#     r=r2_score(y_test,y_pred)
#     print('r score is %0.2f'% r)
#
# if __name__=='__main__':
#     main()

#
#
from sklearn.datasets import load_diabetes

def di_dataset():
    [X,y]=load_diabetes(return_X_y=True)
    return[X,y]

def dia_main():

    [X,y]=di_dataset()

    print(len(X))
    print(len(y))


    x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=99)

    print(len(x_train))

    model=LinearRegression()

    model.fit(x_train,y_train)

    y_pred=model.predict(x_test)

    r2=r2_score(y_test,y_pred)

    print('r2 score is %0.2f'% r2)

if __name__=='__main__':
    dia_main()
#
#
# from sklearn.datasets import load_boston
#
from fontTools.misc.cython import returns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
#
# def load_boston():
#     [X,y]=load_boston(returns_X_y=True)
#     return X,y
#
# def model_evaluation():
#     [X,y]=load_boston()
#
#     x_train,x_test,y_train,y-test=train_test_split(X,y,test_size=0.2,random_state=0
#                                                    )
#
#     model = LinearRegression()
#     model.fit(x_train,y_train)
#     y_pred=model.predict(x_test)
#
#     r_score=r2_score(y_test,y_pred)
#     kf = KFold(n_splits=5, shuffle=True, random_state=42)
#
#     scores = cross_val_score(model, X, y, cv=kf)



