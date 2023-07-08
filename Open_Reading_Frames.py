"""
Problem

Either strand of a DNA double helix can serve as the coding strand 
for RNA transcription. Hence, a given DNA string implies six total
reading frames, or ways in which the same region of DNA can be translated
into amino acids: three reading frames result from reading the string 
itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon
and ends by stop codon, without any other stop codons in between. Thus, 
a candidate protein string is derived by translating an open reading frame 
into amino acids until a stop codon is reached.

Given: A DNA string s nof length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated
from ORFs of s. Strings can be returned in any order.
"""
from Extras.rosalind_functions import *
import sys

CODON_TABLE = RNA_table_to_dict(sys.argv[2])

DNA = list(FASTA_to_dict(sys.argv[1]).values())[0]

reverse_comp = reverse_complement(DNA)

def possible_protein(RNA:str)->str:
    results = []
    
    for i in range(len(RNA)):
        
        aminoAcid = translate_codon(RNA[i:i+3], CODON_TABLE)
        
        if aminoAcid and aminoAcid == "M":
        
            protein = ""
            for j in range(i, len(RNA), 3):
                amn = translate_codon(RNA[j:j+3], CODON_TABLE)
                if amn != None and amn != "Stop":
                    protein += amn
                else:
                    results.append(protein)
                    break
                    
    return results

results = set((possible_protein(DNA_to_RNA(DNA)))).union(set(possible_protein(DNA_to_RNA(reverse_comp))))

for prot in results:
    print(prot)