def compries():
	n=str(input('enter the word:'))
	a=''
	
	for i in range(len(n)-1):#for making character and their count
	    b=n[i]+str(n.count(n[i]))
	    if n[i]!=n[i+1]:     #if character will same as next character  to avoid same character and count 
	        a+=b
	                         #for include last character if it count is 1
	if n.count(n[len(n)-1])==1:
	    k=n[len(n)-1]+str(n.count(n[len(n)-1]))
	    a+=k
	    print(a)
	
	        
if __name__ == '__main__':
	compries()
	        
	    
