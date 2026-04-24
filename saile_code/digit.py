def digit(n):
	lis=[]
	while(n>10):
		a=n//10
		b=n%10
		lis.append(b)
		n=a
		if (a<10):
			lis.append(a)
			lis.reverse()
			print(*lis)
def numcout():
    n= int(input("enter the number:"))
    digit(n)
if __name__ == "__main__":
    numcout()	
	
