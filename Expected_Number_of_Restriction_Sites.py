"""
Problem

Say that you place a number of bets on your favorite sports teams. If their
chances of winning are 0.3, 0.8, and 0.6, then you should expect on average 
to win 0.3 + 0.8 + 0.6 = 1.7 of your bets (of course, you can never win exactly 1.7!)

More generally, if we have a collection of events A1,A2,…,An, then the expected 
number of events occurring is Pr(A1)+Pr(A2)+⋯+Pr(An) (consult the note following 
the problem for a precise explanation of this fact). In this problem, we extend 
the idea of finding an expected number of events to finding the expected number 
of times that a given string occurs as a substring of a random string.

Given: A positive integer n (n≤1,000,000), a DNA string s of even length at 
most 10, and an array A of length at most 20, containing numbers
between 0 and 1.

Return: An array B having the same length as A in which B[i] 
represents the expected number of times that s will appear as 
a substring of a random DNA string t of length n, where t is
formed with GC-content A[i] (see “Introduction to Random Strings”).
"""

import sys

n = 0
s = ""
A = []

with open(sys.argv[1]) as file:
    data = list(map(lambda x: x.replace("\n", ""), file.readlines()))
    n = int(data[0])
    s = data[1]
    A = list(map(float, data[2].split(" ")))

s_probs = []
for GC_cont in A:
    GC_prob = GC_cont / 2
    AT_prob = (1 - GC_cont) / 2
    s_probs.append(
        1
        * GC_prob ** (s.count("G") + s.count("C"))
        * AT_prob ** (s.count("A") + s.count("T"))
    )

print(*list(map(lambda x: "%.3f" % (x * (n - (len(s) - 1))), s_probs)))
