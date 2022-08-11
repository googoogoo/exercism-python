poly = {"G":"C", "C":"G", "T":"A", "A":"U"}

def to_rna(dna_strand):
    rna = ''
    for d in dna_strand:
        rna += poly[d]
    return rna    
