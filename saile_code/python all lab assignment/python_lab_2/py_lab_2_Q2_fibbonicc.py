																																																																																		
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
