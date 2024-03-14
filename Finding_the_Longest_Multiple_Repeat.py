import sys
    
#parse data
with open(sys.argv[1]) as file:
    data = file.readlines()
S = data.pop(0).strip()
K = int(data.pop(0))
nodes = [[[line[0], line[1]], int(line[2]), int(line[3])] for line in map(lambda x:x.strip().split(), data)]
edges = [node[0] for node in nodes]

#previous nodes
previous_nodes = {"node1" : "ROOT"}
previous_nodes.update({edge[1] : edge[0] for edge in edges})

#nodes to its substrings
nodes_str = {"node1": ""}
nodes_str = {node[0][1]:S[node[1]-1:node[1]+node[2]-1].strip("$") for node in nodes}

# determine the leaves
heads = {edge[0] for edge in edges}
tails = {edge[1] for edge in edges}
leaves = tails - heads

# number of descendants for every node
n_nodes = max([int(node[4:]) for node in leaves])
descendants = [0]*n_nodes
for leaf in leaves:
    descendants[int(leaf[4:])-1] += 1
    temp_node = previous_nodes[leaf]
    while temp_node != "ROOT":
        descendants[int(temp_node[4:])-1] += 1
        temp_node = previous_nodes[temp_node]
        
# find candidates
candidate_nodes = []
for i, n in enumerate(descendants[1:]):
    if n >= K:
        candidate_nodes.append("node"+ str(i+2))

# find candidate strings
candidate_strings = []
for node in candidate_nodes:
    temp_str = ""
    temp_node = node
    while temp_node != "node1":
        temp_str = nodes_str[temp_node] + temp_str
        temp_node = previous_nodes[temp_node]
    candidate_strings.append(temp_str)

print(max(candidate_strings, key=len))