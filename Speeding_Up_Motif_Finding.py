"""
Problem

A prefix of a length n string s is a substring s[1:j]; a suffix 
of s is a substring s[k:n].

The failure array of s is an array P of length n for which P[k] 
is the length of the longest substring s[j:k] that is equal to
some prefix s[1:k−j+1], where j cannot equal 1 (otherwise, P[k]
would always equal k). By convention, P[1]=0.

Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.
"""

from Extras.rosalind_functions import FASTA_to_dict
import sys

DNA = list(FASTA_to_dict(sys.argv[1]).values())[0]

m = len(DNA)
prefix = [0 for x in range(m)]
i = 0

for j in range(2, m + 1):
    while i > 0 and DNA[i] != DNA[j - 1]:
        i = prefix[i - 1]
    if DNA[i] == DNA[j - 1]:
        i += 1
    prefix[j - 1] = i

print(*prefix)
with open(sys.argv[2], "w") as file:
    string = ""
    for number in prefix:
        string += str(number) + " "
    file.write(string)
