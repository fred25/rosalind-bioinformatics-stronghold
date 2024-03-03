import sys
from Extras.rosalind_functions import reverse_complement

S = set()

with open(sys.argv[1]) as file:
    S = set(file.read().split("\n"))

Src = map(reverse_complement, S)
SUSrc = S.union(Src)

edges = set()
for i in SUSrc:
    edges.add("(" + i[:-1] + ", " + i[1:] + ")")

print(*edges, sep="\n")
if len(sys.argv) > 2:
    with open(sys.argv[2], "w") as ans:
        ans.writelines(map(lambda x:x+"\n", edges))