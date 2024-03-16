"""
Problem

Similarly to our definition of the Catalan numbers, the n-th Motzkin number mn 
counts the number of ways to form a (not necessarily perfect) noncrossing matching 
in the complete graph Kn containing n nodes. For example, Figure 1 demonstrates 
that m5=21. Note in this figure that technically, the "trivial" matching that 
contains no edges at all is considered to be a matching, because it satisfies 
the defining condition that no two edges are incident to the same node.

How should we compute the Motzkin numbers? As with Catalan numbers, we will 
take m0=m1=1. To calculate mn in general, assume that the nodes of Kn are 
labeled around the outside of a circle with the integers between 1 and n, 
and consider node 1, which may or may not be involved in a matching. If 
node 1 is not involved in a matching, then there are mn−1 ways of matching 
the remaining n−1 nodes. If node 1 is involved in a matching, then say it is
matched to node k: this leaves k−2 nodes on one side of edge {1,k} and n−k 
nodes on the other side; as with the Catalan numbers, no edge can connect the 
two sides, which gives us mk−2⋅mn−k ways of matching the remaining edges. 
Allowing k to vary between 2 and n yields the following recurrence relation 
for the Motzkin numbers: mn=mn−1+∑nk=2mk−2⋅mn−k.

To count all possible secondary structures of a given RNA string that do not
contain pseudoknots, we need to modify the Motzkin recurrence so that it counts 
nly matchings of basepair edges in the bonding graph corresponding to the RNA 
string; see Figure 2.

Given: An RNA string s of length at most 300 bp.

Return: The total number of noncrossing matchings of basepair edges in the 
bonding graph of s, modulo 1,000,000.
"""

def motzkin_numbers(s: str, memo={}) -> int:
    if len(s) <= 1:
        return 1
    if memo.get(s, False):
        return memo[s]
    n = motzkin_numbers(s[1:], memo)
    for i in range(1, len(s)):
        if (s[0], s[i]) in (("A", "U"), ("U", "A"), ("C", "G"), ("G", "C")):
            n += motzkin_numbers(s[1:i], memo) * motzkin_numbers(s[i + 1 :], memo)

    memo[s] = n
    return n

if __name__ == "__main__":
    import sys

    DNA = ""

    with open(sys.argv[1]) as file:
        DNA = file.readlines()[1].replace("\n", "")


    print(motzkin_numbers(DNA) % 1000000)
