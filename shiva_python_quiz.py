#A1 writ program to print first N fibonacci numbers
import numpy
from pandas.core.computation.expr import intersection


def fibonacci(n):
    # i am printing first and second number as it is
    first_number=0
    second_number=1
    print(first_number)
    print(second_number)
    # i am taking range for given number with plus one for include given number in itaration
    for i in range(n+1):
        # i adding first number and second number
        number=first_number+second_number
        print(number)
        # i am here matching numbers for continuous adding
        first_number=second_number
        second_number=number



#    1. Sets: Finding Unique Mutations: You have sequenced the genomes of two different viral strains. You need to identify which mutations are unique to the new strain and which are shared between both.
	#Data:  strain_a = {"C241T", "C3037T", "A23403G"}
           #strain_b = {"C241T", "G25563T", "C3037T", "T28144C"}

#a. Find the mutations present in both strains (Intersection).
#b. Find the mutations that exist only in strain_b (Difference).
#c. Combine all unique mutations found across both strains into one master list (Union).



def strains():
    strain_a = {"C241T", "C3037T", "A23403G"}
    strain_b = {"C241T", "G25563T", "C3037T", "T28144C"}

    # i am doing list compression for common mutation
    intersection=[j for j in strain_b if j in strain_a]

    # i am doing list compression for diff mutations in only b
    diff = [j for j in strain_b if j not in strain_a]

    union = []
    for i in strain_a:
        union.append(i)
    for j in strain_b:
        union.append(j)


    print('mutations present in both strains:',intersection)
    print('the mutations that exist only in strain_b:',diff)
    print('master list is :',union)



def main():
    fibonacci(10)
    strains()


if __name__ == '__main__':
    main()

#    4. Given a dictionary with a values list, extract the key whose value has the most unique values.
#Input : test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
#Output : "Best"
#Explanation : 3 (max) unique elements, 9, 6, 5 of "Best".

test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}

def unique_number():
    # i am doing dict compression for key and len of unque values by using set function and len
    dist={key:len(set(value)) for key,value in test_dict.items()}
    print(dist)

    # by writing list compression for i solating dict vales and finding max value
    max_uniqu=max([i for i in dist.values()])

    # i uning for loops for whereve matching max value to key
    for i in dist.keys():
        if dist[i]==max_uniqu:
            print('most unique values:',i)




def main():
    fibonacci(10)
    strains()
    unique_number()


if __name__ == '__main__':
    main()

import numpy as np
a = np.mean([5,7,8])
a = np.std([5,7,8])
print(a)