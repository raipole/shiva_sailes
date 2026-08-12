def decimal(n):
    lis=[]
    
    while(2<=n):
        a=n//2
        b=n%2
        lis.append(b)
        n=a
        if (a<2):
            lis.append(a)
            lis.reverse()
            print(*lis)
        
            break
def decim():
    n=int(input("Enter the number:"))
    decimal(n)
    
if __name__ == "__main__":
	decim()
	    
