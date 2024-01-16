"""
Problem

The graph theoretical analogue of the quandary stated in the introduction above 
is that if we have an RNA string s that does not have the same number of occurrences 
of 'C' as 'G' and the same number of occurrences of 'A' as 'U', then the bonding 
graph of s cannot possibly possess a perfect matching among its basepair edges.
For example, see Figure 1; in fact, most bonding graphs will not contain 
a perfect matching.

In light of this fact, we define a maximum matching in a graph as a matching 
containing as many edges as possible. See Figure 2 for three maximum matchings
in graphs.

A maximum matching of basepair edges will correspond to a way of forming as
many base pairs as possible in an RNA string, as shown in Figure 3.

Given: An RNA string s of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the
bonding graph of s.
"""

from math import factorial
from Extras.rosalind_functions import FASTA_to_dict
import sys

RNA = list(FASTA_to_dict(sys.argv[1]).values())[0]

A = RNA.count("A")
U = RNA.count("U")
G = RNA.count("G")
C = RNA.count("C")

AU_links = factorial(max(A, U)) // factorial(max(A, U) - min(A, U))

CG_links = factorial(max(C, G)) // factorial(max(C, G) - min(C, G))


print(AU_links * CG_links)
