"""
Problem

As is the case with point mutations, the most common type of sequencing
error occurs when a single nucleotide from a read is interpreted incorrectly.

Given: A collection of up to 1000 reads of equal length (at most 50 bp)
in FASTA format. Some of these reads were generated with a single-nucleotide
error. For each read s in the dataset, one of the following applies:

    s was correctly sequenced and appears in the dataset at least twice
    (possibly as a reverse complement);

    s is incorrect, it appears in the dataset exactly once, and its Hamming
    distance is 1 with respect to exactly one correct read in the dataset 
    (or its reverse complement).

Return: A list of all corrections in the form "[old read]->[new read]".
(Each correction must be a single symbol substitution, and you may return
the corrections in any order.)
"""
import sys
from Extras.rosalind_functions import (
    FASTA_to_dict,
    reverse_complement,
    hamming_distance,
)

DNA_list = list(FASTA_to_dict(sys.argv[1]).values())

rights = []
wrongs = []

mutations = []

for dna in DNA_list:
    rev = reverse_complement(dna)
    if DNA_list.count(dna) >= 2 or rev in DNA_list:
        if dna not in rights and rev not in rights:
            rights.append(dna)
            rights.append(reverse_complement(dna))
        continue
    wrongs.append(dna)

for wrong in wrongs:
    for right in rights:
        if hamming_distance(wrong, right) == 1:
            mutations.append((right, wrong))

with open(sys.argv[2], "w") as file:
    for pair in set(mutations):
        print("".join((pair[1], "->", pair[0])), file=file)
