def lop():
    first_number=0
    second_number=1
    print(first_number)
    print(second_number)
    for i in range(0,20):
        number = first_number+second_number
        print(number)
        first_number=second_number
        second_number=number       		

if __name__ == "__main__":
    lop()
