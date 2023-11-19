from Extras.rosalind_functions import FASTA_to_dict
import sys

data = list(FASTA_to_dict(sys.argv[1]).values())

S1 = data[0]
S2 = data[1]

m = len(S1)
n = len(S2)

table = [[0 for x in range(n + 1)] for x in range(m + 1)]

for i in range(m + 1):
    for j in range(n + 1):
        if i == 0 or j == 0:
            table[i][j] = 0
        elif S1[i - 1] == S2[j - 1]:
            table[i][j] = table[i - 1][j - 1] + 1
        else:
            table[i][j] = max(table[i - 1][j], table[i][j - 1])

index = table[m][n]
subs = [""] * (index + 1)
subs[index] = ""

i = m
j = n

while i > 0 and j > 0:
    if S1[i - 1] == S2[j - 1]:
        subs[index - 1] = S1[i - 1]
        i -= 1
        j -= 1
        index -= 1
    elif table[i][j - 1] >= table[i - 1][j]:
        j -= 1
    else:
        i -= 1

print("".join(subs))
