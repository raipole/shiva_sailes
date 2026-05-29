##1Compute the covariance matrix using matrix multiplications.
# Verify your results by using numpy library operations
X = [[1,0,2,1,0],[0,1,1,1,2],[2,2,0,1,1]]

def variance():
    X = [[1, 0, 2, 1, 0], [0, 1, 1, 1, 2], [2, 2, 0, 1, 1]]

    ## i am going to calculate mean of each feature
    x1_mean=sum([i for i in range(len(X[0])) ])/len(X[0])
    x2_mean=sum([i for i in range(len(X[1])) ])/len(X[1])
    x3_mean=sum([i for i in range(len(X[2])) ])/len(X[2])

    ## i am calculating variance of each feature

    x1_mean_dist=[x1_mean-i for i in X[0]]
    x2_mean_dist=[x2_mean-i for i in X[1]]
    x3_mean_dist=[x3_mean-i for i in X[2]]

    ## i am calculating variance of each feature

    x1_var=[i**2 for i in x1_mean_dist]
    x2_var=[i**2 for i in x2_mean_dist]
    x3_var=[i**2 for i in x3_mean_dist]

    x1_var_sum=sum(x1_var)/(len(X[0])-1)
    x2_var_sum=sum(x2_var)/(len(X[1])-1)
    x3_var_sum=sum(x3_var)/(len(X[2])-1)

    ## i am calculating co_variance of (x,y),(y,z),(z,x)

    co_var_x1_x2=sum([i*j for i in x1_var for j in x2_var])
    co_var_x2_x3=sum([i*j for i in x2_var for j in x3_var ])
    co_var_x3_x1=sum([i*j for i in x3_var for j in x1_var])

variance()



