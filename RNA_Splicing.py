"""
Problem

After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s
(of length at most 1 kbp) and a collection of substrings of s

acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s
. (Note: Only one solution will exist for the dataset provided.)
"""
from Extras.rosalind_functions import FASTA_to_dict, RNA_table_to_dict, DNA_to_RNA, translate_codon
import sys

CODON_TABLE = RNA_table_to_dict(sys.argv[2])

data = FASTA_to_dict(sys.argv[1])

original_DNA = list(data.values())[0]

for dna in list(data.values())[1:]:
    original_DNA = original_DNA.replace(dna, "")

mRNA = DNA_to_RNA(original_DNA)
protein = ""

pos = 0
while True:
    aminoAcid = mRNA[pos:pos+3]
    if len(aminoAcid) < 3 or CODON_TABLE[aminoAcid] == "Stop":
        break
    protein += CODON_TABLE[aminoAcid]
    pos+=3

print(protein)