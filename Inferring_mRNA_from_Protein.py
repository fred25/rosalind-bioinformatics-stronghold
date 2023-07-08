"""
Problem

For positive integers a and n, a modulo n (written amodn in shorthand)
is the remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.

Modular arithmetic is the study of addition, subtraction, multiplication,
and division with respect to the modulo operation. We say that a and b
are congruent modulo n if amodn=bmodn; in this case,
we use the notation a≡bmodn.

Two useful facts in modular arithmetic are that if a≡bmodn
and c≡dmodn, then a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding 
of these rules, you may wish to verify these relationships for a=29, b=73, c=10,
d=32, and n=11.

As you will see in this exercise, some Rosalind problems will 
ask for a (very large) integer solution modulo a smaller number to avoid 
the computational pitfalls that arise with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which 
the protein could have been translated, modulo 1,000,000. 
(Don't neglect the importance of the stop codon in protein translation.)
"""
import sys
from Extras.rosalind_functions import RNA_table_to_dict

table = RNA_table_to_dict(sys.argv[2])

data = open(sys.argv[1]).read()

possibilities = 1

for aa in data:
    possibilities *= list(table.values()).count(aa)

possibilities *= list(table.values()).count("Stop")

print(possibilities%1000000)