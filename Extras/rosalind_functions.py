def FASTA_to_dict(file_path:str) -> dict:
    """
    Function that receive a text file of DNA in FASTA format and returns
    a dictionary in shape {label:DNA}
    """
    
    file_content = open(file_path).readlines()
        
    dictionary = {}
    
    current = ""
    for line in file_content:
        fixed_line = line.replace("\n", "")
        if line[0] == ">":
            current = fixed_line
            dictionary[fixed_line] = ""
            continue
        if current != "": dictionary[current] += fixed_line
    
    return dictionary

def RNA_table_to_dict(file_path:str) -> dict:
    """
    Function that receive a text file of a RNA codon table in Rosalind's format
    and returns a dictionary in shape {RNA: A} (A for amino acid)
    """
    file_content = open(file_path).read()
    
    dictionary = {}
    
    for i in range(len(file_content)):
        substring = file_content[i:i+3]
        if min(map(lambda x:x.isupper(), substring)) == 1 and len(substring) == 3:
            if file_content[i+4:i+6] == "St":
                dictionary[substring] = "Stop"
                continue
            dictionary[substring] = file_content[i+4]
    
    return dictionary