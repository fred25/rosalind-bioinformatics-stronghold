import sys
from Extras.rosalind_functions import FASTA_to_dict

def lev_dist(a: str, b: str) -> int:
    d = [[0 for y in range(len(b)+1)] for x in range(len(a)+1)]

    for i in range(len(a)+1):
        d[i][0] = i

    for i in range(len(b)+1):
        d[0][i] = i

    for j in range(1, len(b)+1):
        for i in range(1, len(a)+1):
            subs_cost = abs((a[i-1] == b[j-1]) - 1)

            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + subs_cost)
    
    return d[len(a)][len(b)], d

a, b = tuple(FASTA_to_dict(sys.argv[1]).values())

distance, table = lev_dist(a, b)

i = len(a)
j = len(b)

a_fixed = ""
b_fixed = ""

while i*j != 0:
    left = table[i][j-1]
    top = table[i-1][j]
    diagonal = table[i-1][j-1]
    m = min(left, top, diagonal)
    
    if table[i][j] == m or (m == left and m == top) or (m != left and m != top):
        a_fixed = a[i-1] + a_fixed
        b_fixed = b[j-1] + b_fixed
        i -= 1
        j -= 1
    elif m == top and m != left:
        a_fixed = a[i-1] + a_fixed
        b_fixed = "-" + b_fixed
        i -= 1
    elif m == left and m != top:
        a_fixed = "-" + a_fixed
        b_fixed = b[j-1] + b_fixed
        j -= 1
    
        

print(distance)
print(a_fixed)
print(b_fixed)