# ##Implement ATA  -  A = [1 2 3 4 5 6]



def martics_multiplly(A):


    # transpose of matrics is AT


    AT=[A[0],A[3],A[1],A[4],A[2],A[5]]

    print(AT)

    ata=([AT[0]*A[0]+AT[1]*A[3],AT[0]*A[1]+AT[1]*A[4],AT[0]*A[2]+AT[1]*A[5]],[AT[2]*A[0]+AT[3]*A[3],AT[2]*A[1]+AT[3]*A[4],AT[2]*A[2]+AT[3]*A[5]],[AT[4]*A[0]+AT[5]*A[3],AT[4]*A[1]+AT[5]*A[4],AT[4]*A[2]+AT[5]*A[5]]  )

    print('multiplication oa ATA is :',list(ata))

if __name__ == '__main__':
    b=[5,6,4,2,8,7]
    martics_multiplly(b)

#
def ts_multy():
    a = [[1, 2, 3], [4, 5, 6]]
    at = []  # at = [[1, 4],[2, 5],[3, 6]]

    m=len(a)
    n=len(a[0])

    for i in range(n):
        lis=a[0][i],a[1][i]
        at.append(list(lis))

    return at ,a
#
#
#
def mul_matrics():
    at,a=ts_multy()
    num=0
    cou=0
    number=[]
    ata=[]
    for i in range(len(at)):
        for l in range(len(at)):

            R=at[i][num]*a[num][i]

            R1=at[i][num+1]*a[num+1][l]

            lis=R+R1
            number.append(lis)

        ata.append(number)
        number=[]
    print(ata)


mul_matrics()

##1.i am writng programe for any matrics to transpose  folled by multiplication that matrics
def ts_multy():
    A = [[1, 2],[4, 5],[7,8],[10,11],[5,8]]
    AT = []  # at = [[1, 4],[2, 5],[3, 6]]

    m=len(A)
    n=len(A[0])

    for i in range(n):
        # i am writing for transpose of matrics

        lis=[A[p][i] for p in range(m) ]

        AT.append(lis)
    print('transpose os a is:',AT)
    return AT,A
#
def ata_multy2():
    num=[]
    AT,A=ts_multy() # i am invoking above function here
    ATA=[]
    for i in range(len(AT)):
        for j in range(len(AT)):

            # i am multipling each number in row of AT and each number of column in A

            R=[(AT[i][q]*A[q][j]) for q in range(len(AT[0])) for h in range(len(AT))]

            num.append(int(sum(R)/len(AT)))


        ATA.append(num)
        num=[]
    print(ATA)


if __name__ == '__main__':
    ata_multy2()
#
# #i am wring programe for any two matrics multiplication

def mul_mart(A,B):

    if len(A[0])==len(B):
        num=[]
     # i am invoking above function here
        AB=[]
        for i in range(len(A)):
            for j in range(len(A)):

                # i am multipling each number in row of AT and each number of column in A

                R=[(A[i][q]*B[q][j]) for q in range(len(A[0])) for h in range(len(A))]

                num.append(int(sum(R)/len(A)))


            AB.append(num)
            num=[]
        print(AB)
    else:
        print('Number of columns of first matrix is not  same Number of rows of second matrix')

if __name__ == '__main__':
    a=[[1, 2, 3],
              [4, 5, 6]]
    b=[[7, 8],
              [9, 10],
              [11, 12]]
    mul_mart(a,b)

# #2Implement y = 2x1 + 3 and plot x1, y [start=-100, stop=100, num=100]
#
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
def linear_function():
    # y=2x1+3
    y_valu=[]
    x1=[i for i in range(-100,100,2)]

    for j in x1:
        y=(2*j)+3
        y_valu.append(y)

    print(len(x1))
    print(y_valu)

    plt.plot(x1,y_valu)
    plt.show()
from matplotlib import pyplot as plt



if __name__ == '__main__':
    linear_function()
#
#
##3Implement y = 2x12 + 3x1 + 4 and plot x1, y in the range [start=--10, stop=10, num=100]

def lin_funt():

    x=-10
    x_f=[]
    x1=0 # i am genarating 100 numbers in between -10 t0 10
    for i in range(0,1000):
        x=x+0.2
        x_f.append(x)
        if x==10:
            break
    print(x_f)
# i am
    y=[2*(i**2)+(3*i)+4 for i in x_f ]
    print(y)
# i am plot between x_f and y values
    plt.plot(x_f,y)
    plt.show()


if __name__ == '__main__':
    lin_funt()



##4Implement Gaussian PDF - mean = 0, sigma = 15 in the range[start=-100, stop=100, num=100]
import math

def gauss_funt():

    sigma = 15
    mean = 0
    x1=[i for i in range(-100,100,2)]
    pdf_gussian=[]
    for j in x1:
        # i am going to compute gausian pdf values between (-100,100)
        pdf=(1/(sigma*math.sqrt(2*3.14)))*math.exp(-0.5*(((j-mean)/sigma)**2))

        pdf_gussian.append(pdf)
    # i am ploting between x1, pdf

    plt.plot(x1,pdf_gussian)

    plt.show()

if __name__ == '__main__':
    gauss_funt()


#5Implement y = x1^2, plot x1, y in the range [start=--10, stop=10, num=100]. Compute the value of derivatives at these points,
# x1 = -5, -3, 0, 3, 5.  What is the value of x1 at which the function value (y) is zero. What do you infer from this
#
def derivative():
    #y=x1^2 this is the function
    a=-10
    x=[]
    for i in range(0,1000):
        a=a+0.2
        x.append(a)
        if a==10:
            break

    return x
def function():
    x=derivative()
    y=[]
    for j in x:
        y1=j**2

        y.append(y1)

    return x,y

def fun_derivation():
    x,y=function()

    m = 1


    x1= [-5, -3, 0, 3, 5]

    y_fun='x**2'

    k = 2
    x1 = [-5, -3, 0, 3, 5]
    # i am writing here  derivation of function followed by giving slop of the values at given x1 points

    dy_dx=[k*(x**(k-1)) for x in x1]

    plt.plot(x,y)



    # i am writing code for where function will 0 at what x value

    Y_zero=[x for x in x1 if x**2==0]

    print('the given function will be zero at this x value:',*Y_zero)
    plt.show()

if __name__ == '__main__':

    fun_derivation()

##6Implement y = 2x1 + 3x2 + 3x3 + 4, where x1, x2 and x3 are three independent variables.
##Compute the gradient of y at a few points and print the values.


def gradiant():

    y = '2x1 + 3x + 3x2'
    x1=[i for i in range(1,100,2)]
    x2=[i/2 for i in range(1,100,2)]
    x3=[i for i in range(1,50)]

    y_vule=[2*x11 + 3*x22 + 3*x33+4 for x11,x22,x33 in zip(x1,x2,x3)]
    print(y_vule)

    y_min_value=[(x1,x2,x3) for x1,x2,x3 in zip(x1,x2,x3) if (2*x1 + 3*x2 + 3*x3+4)==min(y_vule)]

    print('the function y was get # def gradiant_disc(x1,x2,x3):',*y_min_value)
    y = '2x1 + 3x2 + 3x3 + 4'
    # these are given parameters
    theta = [2, 3, 3]
    # these are features named as x1,x2,x3 along their values
    x1 = [1, 0, 2, 1, 0]
    x2 = [0, 1, 1, 1, 2]
    x2 = [2, 1, 0, 1, 1]
    # these are feature matrix values
    # X = [[1, 0, 2],[0,1,2],[2,1,0],[1,1,1],[0,2,1]]
    X = [[1,0,2,1,0],[0,1,1,1,2],[2,2,0,1,1]]

    # i am goin to cumpute multiplication if feature matrics and parameters(theta to get y_pred values)
    #first i am going to transcpose matrics of X(features)
    x_tr=[]
    for i in range(len(X[0])):

        # i a writing logic tracspose of X(features matrics)

        x_T=[X[j][i]  for j in range(len(X))]

        # i am appending of each row elements as columns in new list as nexted list

        x_tr.append(list(x_T))

    print('transpose of X is:',x_tr)
    return x_tr,theta

        # i am wrint functu=ion for multiplication of matricsminimum value at these values of  (x1,x2,x3):', *y_min_value)

if __name__ == '__main__':

    gradiant()




##7Here is a linear model.
## 	y = 2x1 + 3x2 + 3x3 + 4
# #	The coefficients, represented as theta, is a vector given below
#  #   theta=[2,3,3]
#    # x1=[1,0,2,1,0]
#   #  x2=[0,1,1,1,2]
#     #x2=[2,1,0,1,1]
# 	There are 5 samples represented as a matrix, X, given below
#     X=[[1,0,2,1,0],[0,1,1,1,2],[2,1,0,1,1]]
#     Compute X*theta

def gradiant_disc():
    y = '2x1 + 3x2 + 3x3 + 4'
    # these are given parameters
    theta = [2, 3, 3]
    # these are features named as x1,x2,x3 along their values
    x1 = [1, 0, 2, 1, 0]
    x2 = [0, 1, 1, 1, 2]
    x2 = [2, 1, 0, 1, 1]
    # these are feature matrix values
    # X = [[1, 0, 2],[0,1,2],[2,1,0],[1,1,1],[0,2,1]]
    X = [[1,0,2,1,0],[0,1,1,1,2],[2,2,0,1,1]]

    # i am goin to cumpute multiplication if feature matrics and parameters(theta to get y_pred values)
    #first i am going to transcpose matrics of X(features)
    x_tr=[]
    for i in range(len(X[0])):

        # i a writing logic tracspose of X(features matrics)

        x_T=[X[j][i]  for j in range(len(X))]

        # i am appending of each row elements as columns in new list as nexted list

        x_tr.append(list(x_T))

    print('transpose of X is:',x_tr)
    return x_tr,theta
#
#         ## i am wrint functu=ion for multiplication of matrics
# #
def  multi_matric():
        X,theta=gradiant_disc()
        y_pred=[]
        for i in range(len(X)):

            # i am write substuting theta(parameters) in function y=2x1 + 3x2 + 3x3
            y_valu = [X[i][j]*theta[j] for j in range(len(X[0]))]

            # i am write code add intercept (bias) is 4

            H_theta=(sum(y_valu)+4)

            # i am sapareting the H-theta values for each eterating

            y_pred.append(H_theta)

        print('mechine predicted values is :', *y_pred)

def gradiant_disc():
    y = '2x1 + 3x2 + 3x3 + 4'
    # these are given parameters
    theta = [2, 3, 3]
    # these are features named as x1,x2,x3 along their values
    x1 = [1, 0, 2, 1, 0]
    x2 = [0, 1, 1, 1, 2]
    x2 = [2, 1, 0, 1, 1]
    # these are feature matrix values
    # X = [[1, 0, 2],[0,1,2],[2,1,0],[1,1,1],[0,2,1]]
    X = [[1,0,2,1,0],[0,1,1,1,2],[2,2,0,1,1]]

    # i am goin to cumpute multiplication if feature matrics and parameters(theta to get y_pred values)
    #first i am going to transcpose matrics of X(features)
    x_tr=[]
    for i in range(len(X[0])):

        # i a writing logic tracspose of X(features matrics)

        x_T=[X[j][i]  for j in range(len(X))]

        # i am appending of each row elements as columns in new list as nexted list

        x_tr.append(list(x_T))

    print('transpose of X is:',x_tr)
    return x_tr,theta

        # i am wrint functu=ion for multiplication of matrics
if __name__ == '__main__':

    multi_matric()
