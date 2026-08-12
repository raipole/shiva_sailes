# #You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].
# #Create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...].
# import numbers
#
#
# def capital():
#     fruits = ['mango','kiwi','strawberry','guava','pineapple','mandarin orange']
#
#     capita=[i[0].upper()+i[1:len(i)] for i in fruits]
#
#     print(capita)
#
#
# if __name__ == '__main__':
#     capital()
#
#
#
#
#
# #You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].
# #Make a variable named fruits_with_only_two_vowels. Use list comprehension to produce ['mango', 'kiwi', 'strawberry'], a list of fruits with only two vowels.
#
#
# def owel():
#     fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
#
#     vowels = ['a','e','i','o','u']
#     b=vowels[2]
#
#     fruits_ovel=[i for i in fruits for j in  vowels if i.count(j)==2]
#
#     print(fruits_ovel)
#
# if __name__ == '__main__':
#         owel()
#
#
# #Given numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Create a dictionary of numbers and their squares,
# # excluding odd numbers using dictionary comprehension.
#
# def dict():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     dict={key:key*key for key in numbers if key%2==0}
#     print(dict)
#
#
# if __name__ == '__main__':
#     dict()
#
#
#
# #sentence = "Hello, how are you?". Write a dictionary comprehension to map words to their reverse in a sentence.
# # The output should be - {'Hello,': ',olleH', 'how': 'woh', 'are': 'era', 'you?': '?uoy'}
#
# def revers_dict():
#     sentence = "Hello, how are you?"
#
#     lis=[] # here i am isolating words before space occured in list
#     a=''
#     for c in sentence:
#         a+=c
#         if c==' ':
#             lis.append(a) # here i am appendind words to lis which are sapareted by space
#             a=''
#
#     dict_revers={key:key[::-1] for key in lis } # here i am creating dict word along their revers
#
#     print(dict_revers)
#
# if __name__ == '__main__':
#     revers_dict()



##Given org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"], org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"],
# find all similar pairs of genome sequences (one sequence from org1, one from org2) using list comprehension.
# “Similar” means: similarity(seq1, seq2) > threshold

def strain():
    org1 = ["ACGTTTCA","AGGCCTTA","AAAACCTG"]
    org2 = ["AGCTTTGA","GCCGGAAT","GCTACTGA"]

    lis=[]
    a=0
    for i in range(len(org1)):
        for j in range(len(org1[i])):

            if org1[i][j]==org2[i][j]:
                    a+=1
            if j==(len(org1[i])-1):
                lis.append(a)
                a=0
    print(lis)
if __name__ == "__main__":
    strain()

# it is onether way of doing above question with list compression

org1 = ["ACGTTTCA","AGGCCTTA","AAAACCTG"]
org2 = ["AGCTTTGA","GCCGGAAT","GCTACTGA"]

# i am writing  take index where same nuleotide matching
similarity_index=[i for i in range(len(org1)) for j in range(len(org1[i])) if org1[i][j]==org2[i][j]]

print(similarity_index)

count_similarity=[similarity_index.count(i) for i in range(len(org1))]

print('no of similarity between two sequence in two list is: ',count_similarity)




