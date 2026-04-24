def palindrom():
    n=str(input('enter the word:'))
    n1=n[::-1]
    a=''
    for i in range(len(n)):
        if n[i]==n1[i]:
            a+='y'
        else:
            a+='no'
    if a.rfind('no')==1:
        print('print is not palindrom')
        
    else:
        print('print is palindrom')
        
        
if __name__ == '__main__':
	palindrom()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
