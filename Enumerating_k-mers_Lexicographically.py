"""
Problem

Assume that an alphabet A has a predetermined order; that is,
we write the alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak.
For instance, the English alphabet is organized as (A,B,…,Z).

Given two strings s and t having the same length n, we say that s precedes
t in the lexicographic order (and write s<Lext) if the first symbol s[j] that 
doesn't match t[j] satisfies sj<tj in A.

Given: A collection of at most 10 symbols defining an ordered alphabet, 
and a positive integer n(n≤10).

Return: All strings of length n that can be formed from the alphabet, 
ordered lexicographically (use the standard order of symbols in the 
English alphabet).
"""
import sys

data = open(sys.argv[1]).readlines()

alpha = [x for x in data[0] if not x.isspace()]
length = int(data[1])


def a(alpha: list, length: int, current="") -> list:
    total_list = []

    def all_possibilities(alpha: list, length: int, current=""):
        if len(current) == length:
            total_list.append(current)
            return
        for letter in alpha:
            all_possibilities(alpha, length, current=current + letter)

    all_possibilities(alpha, length)

    return total_list


possibilities = a(alpha, length)

possibilities.sort()

output = open("answer.txt", "w")

for item in possibilities:
    output.write(item + "\n")
    print(item)
