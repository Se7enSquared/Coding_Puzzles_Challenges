def to_rna(dna_strand):
    strand_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = ''
    for i in range(0, len(dna_strand)):
        if dna_strand[i] in strand_dict:
            rna += strand_dict[dna_strand[i]]
        else:
        	rna_strand = ''
        	return rna_strand
    return rna
