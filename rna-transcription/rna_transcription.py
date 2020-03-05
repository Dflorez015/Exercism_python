def to_rna(dna_strand = None):
    chain = {"G":"C","C":"G","T":"A","A":"U"} 
    value = ""
    if len(dna_strand) >= 1 and dna_strand != None:
        for x in dna_strand:
            value += chain[x]
        return value    
    elif dna_strand == "":
         return value
    