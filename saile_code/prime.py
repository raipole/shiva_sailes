def prime(n):
    if n==2 or n==3:
        print("this is prime number")
    
    else:
        for i in range(2,n-1):
        
            if n%i==0 :
                print("this is not  prime number")
                break
            else:
                print("this is  the prime number")
                break
def main1():
    n=int(input("enter the input:"))
    prime(n)
if __name__ == "__main__":
	main1()
