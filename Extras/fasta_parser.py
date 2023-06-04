class FASTA_parser:
    
    def parse_dict(file_path:str) -> dict:
        """
        Function that receive a text file of DNA in FASTA format and returns
        a dictionary in shape {label:DNA}
        """
        
        file_content = open(file_path).readlines()
        
        dictionary = {}
        
        current = ""
        for line in file_content:
            if line[0] == ">":
                current = line
                dictionary[line] = ""
                continue
            if current != "": dictionary[current] += line
        
        return dictionary