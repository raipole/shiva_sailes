def motif():
    DNA="ATGCGTACGTTAGCCTAGGCTAATCGGATCGTACGATCGTACGATCGTAGCTAGC"
    print('total count of CG:',DNA.count('CG'))
    for i in range(len(DNA)-1):
        if DNA[i]+DNA[i+1]=='CG':
            print('possition of CG:',i+1)

if __name__ == '__main__':
    motif()
