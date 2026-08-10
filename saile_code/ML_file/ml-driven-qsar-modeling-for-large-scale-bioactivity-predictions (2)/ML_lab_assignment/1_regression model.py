from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def load_data():
    [X,y]=fetch_california_housing(return_X_y=True)
    return [X,y]



    print('Hello')
def mymain():
    [X,y]=load_data()
    # spliting data 70% of training and 30% for test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=999)

    print('----TRAINING-----''')

    print("N=%d"% (len(X)))

    model=LinearRegression()

    #train the model
    model.fit(X_train,y_train)

    #prediction on a test set
    y_pred=model.predict(X_test)

    #comput the r2 score
    r2=r2_score(y_test,y_pred)
    print("r2 score is %0.2f closer to 1 is good" % r2)

if __name__=='__main__':
    mymain()