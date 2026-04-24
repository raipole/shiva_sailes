def count_str(n):
    c= len(n)
    lis=[]
    for i in range(c):
        b=n.count(n[i])
        lis.append(b)
    print("highest frequency:",max(lis))
    v=lis.index(max(lis))
    print("highest frequency alphabets:",n[v])

   
           
def strin():

	n=str(input("enter the string:"))
	count_str(n)

if __name__ == "__main__":
	strin()     


	


