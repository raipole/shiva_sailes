def decima(n):
	lis=[]
	
	while (n>=2):
		a=n//2
		b=n%2
		lis.append(b)
		n=a
		if (a<2):
			lis.append(a)
			lis.reverse()
			c=lis.count(1)
			print(c)
			
def numcout():
    n= int(input("enter the number:"))
    decima(n)
if __name__ == "__main__":
    numcout()
