from Extras.rosalind_functions import FASTA_to_dict
import sys

data = list(FASTA_to_dict(sys.argv[1]).values())

DNA = data[0]
sub = data[1]
sub_index = 0
res = []

for index, base in enumerate(DNA):
    if sub_index >= len(sub):
        break
    if base == sub[sub_index]:
        res.append(index + 1)
        sub_index += 1

print(*res)
