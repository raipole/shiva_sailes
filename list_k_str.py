def k_str(): #Write a program to extract words from a string list, L whose first character is k.
    lis=['shiva','krishna','bhoni','shyam']
    liss=[i for i in lis if i[0]=='k']
    print(liss)
if __name__=='__main__':
    k_str()
