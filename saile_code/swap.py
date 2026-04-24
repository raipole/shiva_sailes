
def swap(a, b):
    sa = b
    sb = a
    return(sa, sb)
	
	
def mymain():
    #f = convert_c_to_f()
    
    # I am going to swap two numbers
    a = 5
    b = 8
    new_a, new_b = swap(a, b)
    print(new_a,new_b)
    
if __name__ == "__main__":
	mymain()
