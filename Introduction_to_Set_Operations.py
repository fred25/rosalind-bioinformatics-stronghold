"""
Problem

If A and B are sets, then their union A∪B is the set comprising any elements in 
either A or B; their intersection A∩B is the set of elements in both A and B; 
and their set difference A−B is the set of elements in A but not in B.

Furthermore, if A is a subset of another set U, then the set complement of A with 
respect to U is defined as the set Ac=U−A. See the Sample sections below for examples.

Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.

Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are taken with respect to {1,2,…,n}).
"""

import sys

n = 0
A = set()
B = set()


with open(sys.argv[1]) as file:
    data = file.readlines()
    n = int(data[0].replace("\n", ""))
    formatter = lambda x: set(map(int, x.replace("\n", "")[1:-1].split(", ")))
    A, B = map(formatter, data[1:])

prints = []
prints.append(A.union(B))
prints.append(A.intersection(B))
prints.append(A - B)
prints.append(B - A)
prints.append(set(range(1, n+1)) - A)
prints.append(set(range(1, n+1))- B)

with open(sys.argv[2], "w") as ans:
    ans.writelines(map(lambda x: str(x) + "\n", prints))

print("Done")