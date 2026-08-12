# Write a Python program to rearrange positive and negative numbers in a given array using Lambda.

lis=[-9,2,5,-6,1,7,-5,8,-3,-4,3,8]
# i am arraging negative values
print(sorted(lis, key=lambda x:-x))

# i am arraging negative values in to new variable

negativ_values=list(filter(lambda x:x<0, lis))

print('negative numbers is:',negativ_values)


#Sorting Complex Data: You have a list of tuples representing students and their grades: students = [("Alice", 88), ("Bob", 95), ("Charlie", 78), ("Diana", 92)].
# Sort this list by the grade (the second element) in descending order using a lambda function.
# Hint: The sort() and sorted() functions have a key parameter that is the most common use case for lambdas.

students = [("Alice", 88), ("Bob", 95), ("Charlie", 78), ("Diana", 92)]

ordered_list=sorted(students,key=lambda x: x[1])

print(ordered_list)





#create a new list containing only the positive even numbers.
# Input: numbers = [-10, 5, 8, -2, 4, 13, 0, 6], Write a single line of code that filters this list.


def neg_saparation():


    numbers = [-10, 5, 8, -2, 4, 13, 0, 6]

    positive_num=list(filter(lambda x:x>0, numbers))

    print('possitive number is :',positive_num)


if __name__=='__main__':
    neg_saparation()


#Data Transformation with Map: You are given a list of temperatures in Celsius: celsius_temps = [0, 12, 34, 100].
# Use the map() function and a lambda to convert these to Fahrenheit

def cel_to_farh():

    celsius_temps = [0, 12, 34, 100]

    farhen= list(map(lambda x: ((9/5)*x)+32,celsius_temps))

    print('these are harhenheat :',farhen)


if __name__=='__main__':

    cel_to_farh()


#Create a logging decorator to record function calls, arguments, and return values. For example, if we have an add function shown below and invoke it as add(2,3), create a decorator that prints the following:
	   # the decorator should print
	   #Calling add with args: (2, 3), kwargs: {}
     #add returned: 5


from statistics import mean



