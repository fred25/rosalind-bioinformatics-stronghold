"""
Problem

Given a collection of n taxa, any subset S of these taxa can be seen as encoding a character 
that divides the taxa into the sets S and Sc; we can represent the character by S∣Sc, which 
is called a split. Alternately, the character can be represented by a character array A of
length n for which A[j]=1 if the jth taxon belongs to S and A[j]=0 if the jth taxon belongs to Sc 
(recall the "ON"/"OFF" analogy from “Counting Subsets”).

At the same time, observe that the removal of an edge from an unrooted binary tree produces
two separate trees, each one containing a subset of the original taxa. So each edge may also 
be encoded by a split S∣Sc.

A trivial character isolates a single taxon into a group of its own. The corresponding split S∣Sc
must be such that S or Sc contains only one element; the edge encoded by this split must be incident 
to a leaf of the unrooted binary tree, and the array for the character contains exactly one 0 or 
exactly one 1. Trivial characters are of no phylogenetic interest because they fail to provide us
with information regarding the relationships of taxa to each other. All other characters are called 
nontrivial characters (and the associated splits are called nontrivial splits).

A character table is a matrix C in which each row represents the array notation for a nontrivial 
character. That is, entry Ci,j denotes the "ON"/"OFF" position of the ith character with respect 
to the jth taxon.

Given: An unrooted binary tree T in Newick format for at most 200 species taxa.

Return: A character table having the same splits as the edge splits of T. The columns of the
character table should encode the taxa ordered lexicographically; the rows of the character 
table may be given in any order. Also, for any given character, the particular subset of taxa 
to which 1s are assigned is arbitrary.
"""
from Bio import Phylo
from io import StringIO
import sys

get_name = lambda x:x.name
tree_str = ""

with open(sys.argv[1]) as file:
    tree_str = file.read().replace("\n", "")

tree = Phylo.read(StringIO(tree_str), "newick")
root = tree.root
TAXA = sorted(list(map(get_name, tree.find_clades(lambda x:bool(x.name)))))

table = []

def fill_table(matrix, clade, TAXA):
    
    for subclade in clade.clades:
        
        if not subclade.is_terminal():
        
            array = []
            subtree_clades = set(map(get_name, subclade.get_terminals()))
        
            for taxon in TAXA:
        
                if taxon in subtree_clades:
                    array.append(1)
        
                else:
                    array.append(0)
        
            matrix.append(array)
            matrix = fill_table(matrix, subclade, TAXA)
    
    return matrix

table = fill_table(table, root, TAXA)

with open(sys.argv[2], "w") as file:
    
    for i in table:
        file.write("".join(map(str, i)) + "\n")