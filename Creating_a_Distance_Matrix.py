"""
Problem

For two strings s1 and s2 of equal length, the p-distance between them, denoted
dp(s1,s2), is the proportion of corresponding symbols that differ between s1 and s2.

For a general distance function d on n taxa s1,s2,…,sn (taxa are often 
represented by genetic strings), we may encode the distances between pairs
of taxa via a distance matrix D in which Di,j=d(si,sj).

Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length 
(at most 1 kbp). Strings are given in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given 
strings. As always, note that your answer is allowed an absolute
error of 0.001.
"""

from Extras.rosalind_functions import FASTA_to_dict, hamming_distance
import sys

sequences = list(FASTA_to_dict(sys.argv[1]).values())

MATRIX_SIZE = len(sequences)

SEQUENCE_SIZE = len(sequences[0])

matrix = [[0.0 for j in range(MATRIX_SIZE)] for i in range(MATRIX_SIZE)]

for index, item in enumerate(sequences):
    for jndex, jtem in enumerate(sequences):
        matrix[index][jndex] = hamming_distance(item, jtem) / SEQUENCE_SIZE

for sublist in matrix:
    for item in sublist:
        print("%.5f" % item, end=" ")
    print()
