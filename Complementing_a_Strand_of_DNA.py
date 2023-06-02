"""
Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
is the string sc formed by reversing the symbols of s , then taking 
the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""
import sys

dna_str = open(sys.argv[1]).read()

comp_dna = ""

for nucleotide in dna_str:
    if nucleotide == "A": comp_dna += "T"
    if nucleotide == "T": comp_dna += "A"
    if nucleotide == "C": comp_dna += "G"
    if nucleotide == "G": comp_dna += "C"
    
comp_dna = comp_dna[::-1]

print(comp_dna)