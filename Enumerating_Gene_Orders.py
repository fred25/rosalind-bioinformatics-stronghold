"""
Problem

A permutation of length n
is an ordering of the positive integers {1,2,…,n}. For example,
π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, 
followed by a list of all such permutations (in any order).
"""
# Note!! it is not just factorial :(
import sys
from itertools import permutations

number = int(open(sys.argv[1]).read())

original_list = list(range(1, number+1))

perm = list(permutations(original_list))

print(len(perm))
for perm in perm:
    for n in perm:
        print(n, end=" ")
    print()