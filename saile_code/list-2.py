def lis():
    n=[2,5,6,8,4,7,6]
    n1=n.copy()
    n1.sort()
    print('lowest value is:',n1[0])
    print('highest value is:', n1[len(n1)-1])

if __name__ == '__main__':

    lis()