def sume(n):
    num=1
    sum=0
    while (num<=n):
       
        sum=num+sum
        
        num=num+1
    
    print(sum)
        		
if __name__ == "__main__":
	sume(10)
	
	
def sume(n):
    a=sum(i for i in range(0,n+1))
    print(a)
if __name__ == "__main__":
	sume(10)
