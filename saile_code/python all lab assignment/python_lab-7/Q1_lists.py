def lis():
    n=[2,3,5,4,7,6]
    a=0
    for i in n:
        a=a+i
    print('sum of list:',a)
    print('avarage of list:',a/len(n))


if __name__ == '__main__':
    lis()