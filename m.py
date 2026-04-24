
def compries():
    n=str(input('enter the word:'))
    c=''
    for i in n:
        a=1
        while n[i]==n[i+1]:
            a+=1
        b=n[i]+(a)
       
        if n[i]!=n[i+1]:
            c+=k
            c+=b
    print(c)
	   
	
	        
if __name__ == '__main__':
	compries()
