import sys
from itertools import count


class Trie:
    
    def __init__(self):
        self._max_ind = count(start = 1)
        self.root = [next(self._max_ind), {}]
    
    def insert(self, key):
        current = self.root
        for letter in key:
            if letter not in current[1]:
                current[1][letter] = [next(self._max_ind), {}]
            current = current[1][letter]

def pprint_trie(tree, node = None):
    if node == None: node = tree.root
    for letter, children in node[1].items():
        print(node[0], children[0], letter)
        pprint_trie(tree, children)   

def export_trie(tree, file):
    items = []
    def Format(tree, node = None):
        if node == None: node = tree.root
        for letter, children in node[1].items():
            items.append(str(node[0]) + " " + str(children[0]) + " " + letter)
            Format(tree, children)
    Format(tree)
    with open(file, "w") as f:
        for item in items:
            f.write(item +"\n")
        
         
if __name__ == "__main__":

    data = []

    with open(sys.argv[1]) as file:    
        data = file.read().split("\n")
    trie = Trie()
    
    for i in data:
        trie.insert(i)

    export_trie(trie, sys.argv[2])
    pprint_trie(trie)