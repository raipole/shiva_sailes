##1Compute the covariance matrix using matrix multiplications.
# Verify your results by using numpy library operations
X = [[1,0,2,1,0],[0,1,1,1,2],[2,2,0,1,1]]

def variance():
    x = [[1, 0, 2, 1, 0], [0, 1, 1, 1, 2], [2, 2, 0, 1, 1]]



    mean_matrics=[]

    # i am going to calculate mean of each feature
    x1_mean=sum([i for i in X[0] ])/len(X[0])

    mean_matrics.append(x1_mean)
    x2_mean=sum([i for i in X[1] ])/len(X[0])
    mean_matrics.append(x2_mean)
    x3_mean=sum([i for i in X[2]])/len(x[0])
    mean_matrics.append(x3_mean)

    print(mean_matrics)
#     # i am going to subtract mean their respetive data
#
    dist_mean_matrix=[]
    x1_mean_dist=[X[0][i]-x1_mean for i in range(len(X[0])) ]
    dist_mean_matrix.append(x1_mean_dist)
    x2_mean_dist=[x[1][i]-x2_mean for i in range(len(X[0])) ]
    dist_mean_matrix.append(x2_mean_dist)
    x2_mean_dist=[X[2][i]-x3_mean for i in range(len(X[0])) ]
    dist_mean_matrix.append(x2_mean_dist)

    print('x',dist_mean_matrix)

    t_dist_mean_matrix = []
    for i in range(len(X[0])):
        T = [dist_mean_matrix[j][i] for j in range(len(dist_mean_matrix))]
        t_dist_mean_matrix.append(T)
    print(t_dist_mean_matrix)
#

    # Covariance matrix =1/n-1((dist_mean_matric).transpose of dist_mean_matric)

    dist_mean_matrix_dot_t_dist_mean_matrix=[]

#
# # i am going to multyply both matrics dist_mean_matrix and t_dist_mean_matrix
    l= 5 # n is number of features
    dist_mean_matrix_dot_t_dist_mean_matrix = []
    lis=[]
    for i in range(len(dist_mean_matrix)):
        for k in range(len(dist_mean_matrix)):

            n=[dist_mean_matrix[i][j]*t_dist_mean_matrix[j][k] for j in range(len(dist_mean_matrix[0]))]

            lis.append(sum(n))

        dist_mean_matrix_dot_t_dist_mean_matrix.append(lis)
        lis=[]
    print('d',dist_mean_matrix_dot_t_dist_mean_matrix)
    covariance_matrix=[]
    lis=[]
    for i in range(len(dist_mean_matrix_dot_t_dist_mean_matrix)):
        for j in range(len(dist_mean_matrix_dot_t_dist_mean_matrix[0])):
            num=dist_mean_matrix_dot_t_dist_mean_matrix[i][j]/(l-1)
            lis.append(num)
        covariance_matrix.append(lis)
        lis=[]

    print('this is co_variance of matrics:',covariance_matrix)




variance()



#Compute the dot product of two vectors, x and y given below
#x = [2  1  2]T and y = [1  2  2]T . What is the meaning of the dot product of two vectors? Illustrate that with your own example.

def dot_product():

    x_t=[1,2,2]
    y_t=[1,2,2]

    #x_dot_y= multiplication of transope of x and  y

    x_t=[1,2,2]
    y=[[i] for i in y_t]

    print(y)
# i am calculating  dot product
    x_t_dot_y=sum([x_t[i]*y[i][0] for i in range(len(x_t))])
    print('dot product of  x,y is:',x_t_dot_y)

dot_product()


