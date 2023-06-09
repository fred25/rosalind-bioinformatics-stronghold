"""
Problem

A common substring of a collection of strings is a substring
of every member of the collection. We say that a common substring 
is a longest common substring if there does not exist a longer 
common substring. For example, "CG" is a common substring of "ACGTACGT"
and "AACCGTATA", but it is not as long as possible; in this case,
"CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique;
for a simple example, "AA" and "CC" are both longest
common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of
length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. 
(If multiple solutions exist, you may return any single solution.)
"""
from Extras.rosalind_parsers import FASTA_to_dict
import sys

data = FASTA_to_dict(sys.argv[1])

shortest = min(data.values(), key= lambda x:len(x))

substrings = []


def check_substring(substring):
    for dna in data.values():
        if dna.find(substring) == -1: return False
    return True

for i in range(len(shortest)+1):
    for j in range(len(shortest)-i+1):
        sub = shortest[i:i+j]
        if sub == "": continue
        if check_substring(sub): substrings.append(sub)

print(max(substrings, key = lambda x: len(x)))