import sys

nodes = []

edges = []

with open(sys.argv[1]) as data:
    content = data.readlines()
    nodes = list(range(1, int(content[0]) + 1))
    for i in range(1, len(content)):
        text = content[i].replace("\n", "")
        edge = []
        for item in text.split(" "):
            edge.append(int(item))
        edges.append(edge)

graph = [{x} for x in nodes]

for edge in edges:
    x, y = edge
    x_fam = set()
    y_fam = set()
    for family in graph.copy():
        if x in family:
            x_fam = family
            graph.remove(family)
        if y in family:
            y_fam = family
            graph.remove(family)
    graph.append(x_fam.union(y_fam))

print(len(graph) - 1)
