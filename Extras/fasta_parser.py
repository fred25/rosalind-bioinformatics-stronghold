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