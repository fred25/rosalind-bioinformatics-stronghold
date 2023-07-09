"""
Problem

A DNA string is a reverse palindrome if it is equal to its 
reverse complement. For instance, GCATGC is a reverse palindrome 
because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the
string having length between 4 and 12. You may return these pairs 
in any order.
"""
import sys
from Extras.rosalind_functions import reverse_complement, FASTA_to_dict

DNA = list(FASTA_to_dict(sys.argv[1]).values())[0]

il_list = []

for i in range(len(DNA)):
    l = 4
    while l <= 12:
        current = DNA[i:i+l]
        if current == reverse_complement(current) and i+l <= len(DNA):
            il_list.append([i+1, l])
        l+=1

out_file = open(sys.argv[2], 'w')
for item in il_list:
    print(item[0], item[1])
    out_file.write(str(item[0])+" "+str(item[1])+"\n")