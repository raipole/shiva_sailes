# def k_mers():
#     lis=list(input('enter list:'))
#     k=int(input('enter k:'))
#     lis_k=[i for i in lis if lis.count(i)==k]
#     print(set(lis_k))
#
# if __name__=='__main__':
#     k_mers()
#Write a program to remove all occurrences of an element from a list,
def remov():
    lis=list(input('enter list:'))
    lis_r=[lis.remove(i) for i in lis ]
    print(lis_r)
if __name__=='__main__':
    remov()