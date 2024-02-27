"""
Problem

The prefix spectrum of a weighted string is the collection of all its prefix weights.

Given: A list L of n (n≤100) positive real numbers.

Return: A protein string of length n−1 whose prefix spectrum is equal to L (if multiple
solutions exist, you may output any one of them). Consult the monoisotopic mass table.
"""

from Extras.rosalind_functions import mass_table_to_dict
import sys

TABLE = mass_table_to_dict(sys.argv[1])

L = []

with open(sys.argv[2]) as file:
    L = list(map(lambda x:float(x.replace("\n", "")), file.readlines()))

prefix = ''
for i in range(len(L)-1):
    mass = round(L[i+1] - L[i], 4)
    amino_acid = list((TABLE.keys()))[list(map(lambda x:round(x, 4), TABLE.values())).index(mass)]
    prefix += amino_acid

print(prefix)