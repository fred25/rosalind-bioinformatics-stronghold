"""
Problem

Say that we have strings s=s1s2⋯sm
and t=t1t2⋯tn with m<n. Consider the substring t′=t[1:m]. We have two cases:

    1. If s=t′, then we set s<Lext because s is shorter than t (e.g., APPLE<APPLET).

    2. Otherwise, s≠t′ . We define s<Lext if s<Lext′ and define s>Lext if s>Lext′ 
        (e.g., APPLET<LexARTS because APPL<LexARTS).

Given: A permutation of at most 12 symbols defining an ordered alphabet A
and a positive integer n (n≤4).

Return: All strings of length at most n formed from A, ordered lexicographically.
(Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order
in which the symbols are given.)
"""

from itertools import product
import sys

string = ""
length = 0

with open(sys.argv[1]) as file:
    file_lines = file.readlines()
    string = file_lines[0].replace(" ", "")
    string = string.replace("\n", "")
    length = int(file_lines[1])

anam_list = []
string_list = []

for i in range(length+1):
    anam_list.extend(list(product(string, repeat=i)))

for item in anam_list:
    if len(item) != 0:
        new_item = "".join(item)
        while len(new_item) < 3:
            new_item+=" "
        string_list.append(new_item)

print(*sorted(string_list, key=lambda x:[string.index(c) for c in x.strip()]), sep="\n")

with open(sys.argv[2], "w") as file:
    for item in sorted(string_list, key=lambda x:[string.index(c) for c in x.strip()]):
        file.write(item)
        file.write("\n")