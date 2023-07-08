"""
Problem

In a weighted alphabet, every symbol is assigned a positive real 
number called a weight. A string formed from a weighted alphabet is 
called a weighted string, and its weight is equal to the sum of the 
weights of its symbols.

The standard weight assigned to each member of the 20-symbol
amino acid alphabet is the monoisotopic mass of the corresponding 
amino acid.

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
"""
from Extras.rosalind_functions import mass_table_to_dict
import sys

MASS_TABLE = mass_table_to_dict(sys.argv[2])

protein = open(sys.argv[1]).read()

t_mass = 0
for amn in protein:
    t_mass += MASS_TABLE[amn]

print(t_mass)