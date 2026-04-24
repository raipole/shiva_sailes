def convert_tem_fah(f):
	c=(f-32)*(5/9)
	return c
def convert():
	f=100
	a=convert_tem_fah(f)
	print(a)
	
if __name__  == "__main__":
	convert()
