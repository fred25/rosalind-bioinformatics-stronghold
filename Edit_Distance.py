"""
Problem

Given two strings s
and t (of possibly different lengths), the edit distance dE(s,t) is the minimum
number of edit operations needed to transform s into t, where an edit operation 
is defined as the substitution, insertion, or deletion of a single symbol.

The latter two operations incorporate the case in which a contiguous
interval is inserted into or deleted from a string; such an interval
is called a gap. For the purposes of this problem, the insertion or 
deletion of a gap of length z still counts as k distinct edit operations.

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).

Return: The edit distance dE(s,t).
"""
# Algorithm from Wikipedia
def lev_dist(a: str, b: str) -> int:
    d = [[0 for y in range(len(b))] for x in range(len(a))]

    for i in range(len(a)):
        d[i][0] = i

    for i in range(len(b)):
        d[0][i] = i

    for j in range(1, len(b)):
        for i in range(1, len(a)):
            subs_cost = abs((a[i] == b[j]) - 1)

            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + subs_cost)
    return d[len(a) - 1][len(b) - 1]


if __name__ == "__main__":
    import sys
    from Extras.rosalind_functions import FASTA_to_dict

    data = list(FASTA_to_dict(sys.argv[1]).values())

    print(lev_dist(" " + data[0], " " + data[1]))
