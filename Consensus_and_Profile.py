"""
Problem

A matrix is a rectangular table of values divided into rows and columns. An m×n
matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate
the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n.
Their profile matrix is a 4×n matrix P in which P1,j represents the number of 
times that 'A' occurs in the jth position of one of the strings, P2,j represents 
the number of times that C occurs in the j th position, and so on (see below).

A consensus string c is a string of length n formed from our
collection by taking the most common symbol at each position; 
the jth symbol of c therefore corresponds to the symbol having 
the maximum value in the j-th column of the profile matrix. 
Of course, there may be more than one most common symbol, leading to 
multiple possible consensus strings.

	        A T C C A G C T
	        G G G C A A C T
	        A T G G A T C T
DNA Strings	A A G C A A C C
	        T T G G A A C T
	        A T G C C A T T
	        A T G G C A C T
	        
            A   5 1 0 0 5 5 0 0
Profile	    C   0 0 1 4 2 0 6 1
	        G   1 1 6 3 0 1 0 0
	        T   1 5 0 0 0 1 1 6

Consensus	    A T G C A A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) 
in FASTA format.

Return: A consensus string and profile matrix for the collection.
(If several possible consensus strings exist, then you may return any one of them.)
"""
from Extras.rosalind_functions import FASTA_to_dict
import sys

DNAs = FASTA_to_dict(sys.argv[1])

index_count = {}

for index in range(len(list(DNAs.values())[0])):
    index_count[index] = {"A":0, "C":0, "G":0, "T":0}
    for dna in DNAs.values():
        if dna[index] == "A": index_count[index]["A"] += 1
        if dna[index] == "C": index_count[index]["C"] += 1
        if dna[index] == "G": index_count[index]["G"] += 1
        if dna[index] == "T": index_count[index]["T"] += 1
        
consensus = ""
for i in index_count.keys():
    consensus += max(index_count[i].keys(), key=index_count[i].get)
print(consensus)
for i in ["A", "C", "G", "T"]:
    string = i+": "
    for index in index_count:
        string += str(index_count[index][i])
        string += " "
    print(string)
    