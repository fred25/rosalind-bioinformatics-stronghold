from itertools import permutations, product
import sys

LEN = int(input("INPUT NUMBER: "))

perms = [list(i) for i in permutations(list(range(1, LEN + 1)))]
maps = list(product([False, True], repeat=LEN))

result = []

for perm in perms:
    for m in maps:
        current = perm.copy()
        for i in range(LEN):
            if m[i] == False:
                current[i] = -current[i]
        result.append(list(current))

l = len(result)

with open(sys.argv[1], "w") as file:
    file.write(str(l))
    file.write("\n")
    for item in result:
        for sub in item:
            file.write(str(sub))
            file.write(" ")
        file.write("\n")
