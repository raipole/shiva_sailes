def rna():
	DNA="ATGCGTACGTTAGCCTAGGCTAATCGGATCGTACGATCGTACGATCGTAGCTAGC"
	RNA=DNA.replace('T','U')
	print(RNA)
	v=int(len(DNA))
	c=RNA.count('G')
	per_g=(c/v)*100
	print('% of G in RNA:',per_g)
	g=RNA.count('C')
	per_c=(g/v)*100
	print('% of G in RNA:',per_c)
rna()
	
	
