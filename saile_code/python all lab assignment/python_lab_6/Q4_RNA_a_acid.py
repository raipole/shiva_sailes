def RNA_s_a():
    Phenylalanine=["UUU","UUC"]
    Tyrosine =["UAU","UAC"]
    Cysteine=["UGU","UGC"]
    Tryptophan=["UGA","UGG"]
    Leucine=["CUU","CUC","CUA","CUG","UUA","UUG"]
    Proline=["CCU","CCC","CCA","CCG"]
    Histidine=["CAU","CAC"]
    Glutamine=["CAA","CAG"]
    Arginine=["CGU","CGC","CGA","CGG","AGA","AGG"]
    Isoleucine=["AUU","AUC","AUA"]
    Tryptophan=["AUG"]
    Threonine=["ACU","ACC","ACA","ACG"]
    Asparagine=["AAU","AAC"]
    Lysine=["AAA","AAG"]
    Serine=["AGU","AGC"]
    Valine=["GUU","GUC","GUA","GUG"]
    Alanine=["GCU","GCC","GCA","GCG"]
    sparticacid=["GAU","GAC"]
    Glutamicacid=["GAA","GAG"]
    Glycine=["GGU","GGC","GGA","GGG"]

    DNA="ATGCGTACGTTAGCCTAGGCTAATCGGATCGTACGATCGTACGATCGTAGCTAGC"
    RNA = DNA.replace('T', 'U')
    print('RNA is :', RNA)
    for i in range(len(RNA)-2):
        a=RNA[i]+RNA[i+1]+RNA[i+2]
        if a in Phenylalanine:
            print(a,'is pnenylalanine')

        elif a in Leucine:
            print(a, 'is Leucine')
        elif a in Tyrosine:
            print(a, 'is Tyrosine')
        elif a in Cysteine:
            print(a, 'is Leucine')
        elif a in Proline:
            print(a, 'is Proline')
        elif a in Histidine:
            print(a, 'is Histidine')
        elif a in Glutamine:
            print(a, 'is Glutamine')
        elif a in Arginine:
            print(a, 'is Arginine')
        elif a in Isoleucine:
            print(a, 'is Isoleucine')
        elif a in Asparagine:
            print(a, 'is Asparagine')
        elif a in Threonine:
            print(a, 'is Threonine')
        elif a in Lysine:
            print(a, 'is Lysine')
        elif a in Serine:
            print(a, 'is Serine')
        elif a in Valine:
            print(a, 'is Valine')
        elif a in Alanine:
            print(a, 'is Alanine')
        elif a in sparticacid:
            print(a, 'is sparticacid')
        elif a in Glutamicacid:
            print(a, 'is Glutamicacid')
        elif a in Glycine:
            print(a, 'is Glycine')


if __name__ == '__main__':
    RNA_s_a()
