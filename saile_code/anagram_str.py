def anagram():
	n=str(input('enter the word:'))
	n1=str(input('enter the word:'))
	a=''
    if len(n)==len(n1):
        for i in range(len(n)):
			if n.rfind(n[i])==1:
				a+=y
			else:
				a+=N
		if a.rfind(N)==1:
			print('this isnot anagrams')
		else:
			print('this is anagrams')
    else:
        print('this isnot anagrams')
if __name__ == '__main__':
	anagram()
