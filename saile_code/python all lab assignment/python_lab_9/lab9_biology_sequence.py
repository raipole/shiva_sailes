#Sets: Finding Unique Mutations: You have sequenced the genomes of two different viral strains.
#You need to identify which mutations are unique to the new strain and which are shared between both.
strain_a = {"C241T", "C3037T", "A23403G"}
strain_b = {"C241T", "G25563T", "C3037T", "T28144C"}

# a.Find the mutations present in both strains (Intersection).
# b.Find the mutations that exist only in strain_b (Difference).
# c.Combine all unique mutations found across both strains into one master list (Union).

a=[i for i in strain_a if i in strain_b]

print('both strain is :', *a)

b=list(i for i in strain_b if i not in strain_a)

print('only  strain prasent in strain_b is :', *b)

both_strain=list(strain_a) + list(strain_b)

print('strain prasent in both strain_a,strain_b is:', *both_strain)

#2. Given a DNA sequence, find its reverse complement. First, find the complement (A↔T, C↔G), then reverse the entire string.

complementory_link={'A':'T','G':'C','T':'A','C':'G'}

DNA="ATGCGTACGTTAGCCTAGGCTAATCGGATCGTACGATCGTACGATCGTAGCTAGC"

dna_complementory=[complementory_link[i] for i in DNA]

reverse_dna_complementory=dna_complementory[::-1]

dna_complementory=''.join(dna_complementory)



print('Complementory of DNA sequence:',dna_complementory)

reverse_dna_complementory=''.join(reverse_dna_complementory)

print('Reverse of DNA complementory :', reverse_dna_complementory)

#3. Simulating Restriction Enzyme Digestion: Restriction enzymes cut DNA at specific "recognition sites" (e.g., EcoRI cuts at GAATTC).
# Given a long DNA string and a recognition sequence, write a function that "digests" the DNA and returns a list of fragments.

DNAA="AGCTTAGGCTAATCGGATCCTTAGGCTA"

enzymee={'EcoRI':'GAATTC','BamHI':'GGATCC','HindIII':'AAGCTT','HaeIII':'GGCC','SmaI':'CCCGGG','PstI':'CTGCAG'}

def enzyme():
    for key,value in enzymee.items():
        if value  in DNAA:
            print('in given DNA sequence digeste=ive enzyme along sequence is:',(key,value))

            if value=='GAATTC':
                print('site fragment is:', 'G','AATTC')
            elif value=='GGATCC':
                print('site fragment is:', 'G','GATCC')
            elif value == 'AAGCTT':
                print('site fragment is:', 'A', 'AGCTT')
            elif value == 'GGCC':
                print('site fragment is:', 'GG', 'CC')
            elif value == 'CCCGGG':
                print('site fragment is:', 'CCC', 'GGG')
            elif value == 'CTGCAG':
                print('site fragment is:', 'G', 'CTGCA')





if __name__ == '__main__':
    enzyme()


#4. Calculating Hamming Distance: The Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different.
# It’s used to measure evolutionary distance. Compare two sequences and return the total number of point mutations (mismatches).



def hamminh_distance():
    dna_1='ATGCGTACCTGAATCG'

    dna_2='CGTTAAGGCTTACGGA'

    mismatct=0

    for i,j in zip(dna_1,dna_2):
        if i!=j:
            mismatct+=1

    print('mis match of given two DNA is:',mismatct)



if __name__=='__main__':
    hamminh_distance()