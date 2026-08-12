def kmers():
    n=str(input('enter the word:'))
    k=int(input('enter the number:'))
    k1=len(n)-k
    for i in range(k1):
        print(n[i:i+k])
        
if __name__ == '__main__':
	kmers()
