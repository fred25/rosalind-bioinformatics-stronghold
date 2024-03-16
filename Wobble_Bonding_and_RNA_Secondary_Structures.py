"""
Problem

Given an RNA string s, we will augment the bonding graph of s

by adding basepair edges connecting all occurrences of 'U' to all occurrences of 'G' in order to represent
possible wobble base pairs.

We say that a matching in the bonding graph for s
is valid if it is noncrossing (to prevent pseudoknots) and has the property that a basepair edge in the matching cannot connect symbols sj 
and sk unless k≥j+4 (to prevent nearby nucleotides from base pairing).

See Figure 1 for an example of a valid matching if we allow wobble base pairs. In this problem, we will wish to 
count all possible valid matchings in a given bonding graph; see Figure 2 for all possible valid matchings in 
a small bonding graph, assuming that we allow wobble base pairing.

Given: An RNA string s(of length at most 200 bp).

Return: The total number of distinct valid matchings of basepair edges in the bonding
graph of s. Assume that wobble base pairing is allowed.
"""

import sys

def motzkin_numbers(s: str, memo={}) -> int:
    if len(s) <= 1:
        return 1
    if memo.get(s, False):
        return memo[s]
    n = motzkin_numbers(s[1:], memo)
    for i in range(4, len(s)):
        if {s[0], s[i]} in ({"A", "U"}, {"C", "G"}, {"U", "G"}):
            n += motzkin_numbers(s[1:i], memo) * motzkin_numbers(s[i + 1 :], memo)

    memo[s] = n
    return n

with open(sys.argv[1]) as file:
    data = file.read().strip()

print(motzkin_numbers(data))