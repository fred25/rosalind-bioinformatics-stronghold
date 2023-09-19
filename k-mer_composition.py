"""
Problem

For a fixed positive integer k, order all possible k-mers taken from
an underlying alphabet lexicographically.

Then the k-mer composition of a string s can be represented by an array  A for which 
A[m] denotes the number of times that the mth k-mer (with respect to the lexicographic
order) appears in s.

Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s.
"""

import sys
from Extras.rosalind_functions import FASTA_to_dict, DNA_BASES
import itertools as it

data = list(FASTA_to_dict(sys.argv[1]).values())[0]

kmers = list(map(lambda x: "".join(x), it.product(DNA_BASES, repeat=4)))
kmers.sort()

counts = {}

for kmer in kmers:
    counts[kmer] = 0

for i in range(0, len(data) - 3):
    counts[data[i : i + 4]] += 1

for i in counts.values():
    print(i, end=" ")
print()
