import sys
from Bio import Phylo
from io import StringIO

with open(sys.argv[1]) as file:
    data = file.read().split("\n\n")

data_lists = [x.split("\n") for x in data]
parsed_data = [[x[0], x[1].split()] for x in data_lists]

distances = []
for info in parsed_data:
    tree = Phylo.read(StringIO(info[0]), "newick")
    distances.append(int(tree.distance(info[1][0], info[1][1])))

print(*distances)