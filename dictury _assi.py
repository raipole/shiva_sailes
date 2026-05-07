#Write a program to iterate over a dictionary and print key and values
def dic():
    dicte={'shiva':37,'nandu': 36,'hari':30}

    lis=[(key,val) for key,val in dicte.items()]

    print(lis)

if __name__=='__main__':
    dic()


#Write a program to sum all values of a dictionary.

def dic_sum():
    dict={'shiva':37,'nandu': 36,'hari':30}

    lis= sum(val for val in dict.values())
    print(lis)

if __name__=='__main__':
     dic_sum()



#Write a program to find the maximum and minimum value of a dictionary


def dic_m():
    dict={'shiva':37,'nandu': 36,'hari':30}

    lis= max(val for val in dict.values())
    lis1 = min(val for val in dict.values())
    print(lis)
    print(lis1)

if __name__=='__main__':
     dic_m()


#Given a dictionary with a values list, extract the key whose value has the most unique values.

def dict_c():
    test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}

    uniqu={key:len(set(lis)) for key,lis in test_dict.items()}
    print(uniqu)

    keyvalue=list(uniqu.values())

    keys=list(uniqu.keys())

    v=keyvalue.index(max(keyvalue))

    print(keys[v])


if __name__=='__main__':
     dict_c()


#Remove all duplicate words from given sentence using a dictionary

def duplicat_w():
    sant='''West Bengal Chief Minister Mamata Banerjee on Friday issued a strong warning over alleged EVM irregularities 
    after spending more than three hours inside a strongroom in Kolkata, saying any attempt to tamper with voting machines or 
    the counting process would be met with a “life-and-death” fight.'''
    lis=[]
    a=''
    for i in sant:# i writing code for isolating words with exluding space
        if i == ' ': #i given condition where space there skip that space

            pass
        else:
            a+=i
        if i == ' ': # i am sarating words upto space by storing list
            lis.append(a)

            a=''  #
    print(lis)
    dict={key:sant.count(key)for key in lis} # i am creating dict word as keys and their count as values

    print(dict)
    for n,m in dict.items():
        if m>1:
            sant_u=sant.replace(n,'') # i am removing duplicate words given sentance by where count more than 1

    print(sant_u) # here it is the unique words form given santence

if __name__=='__main__':

    duplicat_w()





#The Common Friends Finder: You have two sets of user IDs: followers and following.
# a. Write a program to find "mutuals" (people who follow you AND you follow back).
# b. Find "fans" (people who follow you, but you don't follow back).

def fowlers():
    user_id={'U1001':'lice Johnson','U1002':'Bob Smith','U1003':'Carol Martinez','U1004':'David Lee','U1005':'Eva Brown'
    ,'U1006':'Carol Martinez','U1007':'Eva','U10010':'shiva'}
    follwers={'U1001':{'U1002','U10010','U1004'},'U1002':{'U1007','U1002','U1005'},'U1003':{'U1004','U10010','U1001'},
    'U1004':{'U1002','U1007','U1005'},'U1005':{'U10010','U1004'},'U1006':{'U1007','U1001'},'U1007':{'U10010','U1001'},
    'U10010': {'U1002','U1001','U1003','U1005'}}

    for k in follwers['U10010']:
         if 'U10010' in follwers[k]:
            print(user_id[k]) #'follwowing me whome i am folloeing back:'

         if 'U10010' not in follwers[k]:
            print('not following back:',user_id[k])  # 'follwowing me whome i am folloeing back:'


if __name__=='__main__':
    fowlers()






lis=[[0]*3]*3
lis[0]=1

print(lis)

def liss(a=[]):
    a.append(1)

liss()


