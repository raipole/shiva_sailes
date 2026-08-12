def matr():
    lis=[]
    lis_s=[]
    list1 = [[1,2,4],[5,6,7],[5,7,9]]
    list2 = [[5,6,7],[4,5,6],[7,8,9]]
    c=0
    b=0
    v=(len(list1))
    while c!=v:

        a=list1[c][b]-list2[c][b]
        b+=1
        lis.append(a)
        if b==(len(list1)):
            lis_s.append(lis)
            lis=[]
            b=0 # i given b=0 for avoid icrimental of b value
            c+=1 # i given +1 for change a index of list
        if c == (len(list1) - 1): # i given condition for stop iteration
            pass

    print(lis_s)

if __name__ == '__main__':

    matr()

lis=[i-j for i,j in lis1,lis2 ]
print(lis)