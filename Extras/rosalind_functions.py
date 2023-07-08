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

def mass_table_to_dict(filepath:str) -> dict:
    """
    Function that receives the path to a monoisotopic mass table in
    Rosalind.info format and return a equivalent dict.
    """
    table = open("./Extras/Monoisotopic_mass_table.txt").readlines()

    parsed_table = {}

    for data in table:
        parsed_table[data[0]] = float(data[4:].replace("\n", ""))

    return parsed_table

def DNA_to_RNA(DNA:str) -> str:
    """
    Function that receives a DNA string and return its translated
    mRNA string
    """
    return DNA.replace("T", "U")

def translate_codon(codon:str, codon_table:dict) -> str:
    """
    Function that receives a codon string and returns its respective
    amino-acid translated by a table passed as argument.
    """
    
    if len(codon) == 3 and codon in codon_table.keys():
    
        return codon_table[codon]
    
    return None

def reverse_complement(DNA:str) -> str:
    """
    Function that receives a DNA string and return its reverse complement DNA
    """
    
    base_pairs = {"A":"T", "T": "A", "G": "C", "C": "G"}
    
    return "".join([base_pairs[b] for b in reversed(DNA)])