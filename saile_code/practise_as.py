# def swap():
#     a=2
#     b=3
#     print(a,b)
#
#     a=a+b
#     b=a-b
#     a=a-b
#     print('swap number are :',a,b)
#
# swap()
# #
# def odd():
#     a=2
#     num=['even' if a%2==0 else 'odd']
#     print('the given number is',*num)
#
# odd()
# #
# def sum_integers():
#     a=[1,2,5,3,6,7]
#     sum_num=sum([i for i in a ])
#     print(sum_num)
#
# sum_integers()
# #
# def febonic_num():
#
#     first_num=0
#     second_num=1
#     print(first_num)
#     print(second_num)
#     for i in range(0,21):
#         num=first_num+second_num
#         first_num=second_num
#         second_num=num
#         print(num)
# febonic_num()
# #
# def sum_square():
#     a=[1,2,3,4,5,6,7,8,9,10]
#     num_squar=sum([i**2 for i in a])
#     print('number square is:',num_squar)
#
# sum_square()
#
# #
# # def binary_decimal():
# #     a=[11,13,24,15,16]
# #     lis=[]
# #     for i in a:
# #         k=i
# #         while (2 <= i):
# #             b=i//2
# #             c=i%2
# #             lis.append(c)
# #             i=b
# #
# #             if b<2:
# #                 lis.append(b)
# #                 lis.reverse()
# #                 print(k,'binary number is',*lis)
# #                 lis=[]
#
#
# #
# def binary():
#     a=[22,52,63,89,85,74,95,36,55]
#     lis=[]
#     for i in a :
#         while (2<=i):
#             b=i//2
#             c=i%2
#             lis.append(c)
#             i=b
#             if b<2:
#                 lis.append(b)
#                 lis.reverse()
#                 print(lis)
#                 lis=[]
# binary()
#
#
#
#
# def binary_decimal():
#
#     a=[20,30,25,40,48,46,23,78,89]
#     lis=[]
#     for i in a:
#         while(2<=i):
#             b=i//2
#             c=i%2
#             lis.append(c)
#             i=b
#             if b<2:
#                 lis.append(b)
#                 lis.reverse()
#                 n=lis.count(1)
#                 print(n)
#                 lis=[]
#
# binary_decimal()


#a()

#
# def prime_num():
#
#     a=int(input("enter number"))
#     lis=[]
#
#
#     if a==2 and a==3:
#         print("this is prime  number")
#
#     if a % 10 == 0:
#         print("this isnot prime  number")
#
#     else:
#         for i in range(2,a):
#             if a%i==0:
#                 lis.append('no')
#
#                 break
#             if a%i!=0:
#                 lis.append('yes')
#     if 'no' in lis:
#         print("this is not prime  number")
#     else:
#         print("this is  prime  number")
# prime_num()



# def indi_num():
#
#    a=int(input('enter the number:'))
#    lis=[]
#
#    while(a>=10):
#        b=a//10
#        c=a%10
#        lis.append(c)
#        a=b
#        if a<10:
#            lis.append(b)
#
#            break
#    lis.reverse()
#    print(*lis)
# indi_num()

##lab_4
#
# b='shivananda  reddy'
# k=(len(b)/2)
# m= b[0:5]
# print(m)
#
#
# print(b[0::2])
#
# a='shiva'
# n='nandu'
# s=a+n
# print(s)
# v=a[(len(a)-1)]
# print(v)
# high_freq=[b.count(i) for i in b]
# ibdex=high_freq.index(max(high_freq))
#
# print(b[ibdex])
#
# def replace():
#     a='shivanandareddy'
#     m=''
#     for i in range(len(a)-2):
#         n=a.replace(a[i],a[i+1])
#         m+=a[i+1]
#     print(m)
#
#
#     print(a)
#
# replace()
#
# nuw_str=b.replace(' ','')
# print(nuw_str)
# print(b)

# def anagrams():
#     a=str(input('enter the word:'))
#     b=str(input('enter the word:'))
#     if len(a)==len(b):
#
#         lis=['yes' if a[i] in b else 'no' for i in range(len(a))]
#         if 'no' in lis:
#             print('this is not anagram')
#
#         else:
#             print('this is  anagram')
#
#     else:
#         print('this is not anagrams')
#
# anagrams()


#

# def palindrom():
#
#
#
#     a=str(input('enter the word'))
#     b=a[::-1]
#     if len(a)==len(b):
#         lis = ['yes' if a[i] == b[i] else 'no' for i in range(len(a))]
#         if 'no' in lis:
#             print('this is not palindrom')
#         else:
#             print('this is  palindrom')
#
# palindrom()

#

#

# test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
# #Output : "Best"
# unique={len(set(i)):k for k,i in test_dict.items()}
# valu=max([i for i in unique.keys()])
# print('heist unique values:',unique[valu])


string='''Sets: Finding Unique Mutations: You have sequenced the genomes of two different viral strains.
 You need to identify which mutations are unique to the new strain and which are shared between both'''

m=''
lis=[]
for i in string:
    if i!=' ':
        m+=i
    if i==' ':
        lis.append(m)
        m=''


    dict={keys:lis.count(keys) for keys in lis }

    for key in dict.keys():
        if dict[key]>1:
            v=string.replace(key,'')

print(v)