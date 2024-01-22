"""
Problem

Our aim in this problem is to determine the probability with which a given motif 
(a known promoter, say) occurs in a randomly constructed genome. Unfortunately, 
finding this probability is tricky; instead of forming a long genome, we will
form a large collection of smaller random strings having the same length as the 
motif; these smaller strings represent the genome's substrings, which we can then
test against our motif.

Given a probabilistic event A, the complement of A is the collection Ac of
outcomes not belonging to A. Because Ac takes place precisely when A does not,
we may also call Ac "not A."

For a simple example, if A is the event that a rolled die is 2 or 4, 
then Pr(A)=13. Ac is the event that the die is 1, 3, 5, or 6, and Pr(Ac)=23.
In general, for any event we will have the identity that Pr(A)+Pr(Ac)=1.

Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s 
of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as
s are constructed with GC-content x (see “Introduction to Random Strings”),
then at least one of the strings equals s. We allow for the same random string 
to be created more than once.
"""

import sys

DNA = ""
N = 0
GC_cont = 0.0

with open(sys.argv[1]) as file:
    lines = file.readlines()
    N = int(lines[0].replace("\n", "").split(" ")[0])
    GC_cont = float(lines[0].replace("\n", "").split(" ")[1])
    DNA = lines[1].replace("\n", "")

GC = GC_cont / 2
AT = (1 - GC_cont) / 2

p = 1
for i in DNA:
    if i == "G" or i == "C":
        p *= GC
    if i == "A" or i == "T":
        p *= AT

print("%0.3f" % (1 - (1 - p) ** N))
