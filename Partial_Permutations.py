from math import factorial
import sys

n = 0
k = 0

with open(sys.argv[1]) as file:
    l = file.read().split(" ")
    n = int(l[0])
    k = int(l[1])

print(int(factorial(n) / factorial(n - k) % 1000000))
