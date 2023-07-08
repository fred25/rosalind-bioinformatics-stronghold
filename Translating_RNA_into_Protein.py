"""
Problem

The 20 commonly occurring amino acids are abbreviated by using 20 
letters from the English alphabet (all letters except for B, J, O, U, X, and Z).
Protein strings are constructed from these 20 symbols. Henceforth, the term genetic
string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific
codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
"""
from Extras.rosalind_functions import RNA_table_to_dict
import sys

CODONS_TABLE = RNA_table_to_dict(sys.argv[2])

DNA = open(sys.argv[1]).read()

protein = ""

position = 0
while True:
    aminoAcid = DNA[position:position+3]
    if CODONS_TABLE[aminoAcid] == "Stop":
        break
    protein += CODONS_TABLE[aminoAcid]
    position+=3

print(protein)