"""
Problem

A reversal of a permutation can be encoded by the two indices at the endpoints of the interval
that it inverts; for example, the reversal that transforms (4,1,2,6,3,5) into (4,1,3,6,2,5) is
encoded by [3,5].

A collection of reversals sorts π into γ if the collection contains drev(π,γ) reversals, 
which when successively applied to π yield γ.

Given: Two permutations π and γ , each of length 10.

Return: The reversal distance drev(π,γ), followed by a collection of reversals sorting π into
γ. If multiple collections of such reversals exist, you may return any one.
"""

from Reversal_Distance import *
import sys

def greedy_algorithm(perm1: list, perm2: list) -> tuple:
    from itertools import product

    # transform the permutations in (123...10) and other with the
    # same transformations as the original
    identity = {value: i + 1 for i, value in enumerate(perm2)}
    norm_perm = [identity[value] for value in perm1]

    # variables
    norm_perm = tuple(norm_perm)
    current_perms = {norm_perm:[]}
    min_breaks = n_breakpoints(norm_perm)
    dist = 0
    rev_hist = []
    
    while True:
        new_perms = {}
        dist += 1

        for perm in current_perms.keys():
            for rev in product(breakpoints_indices(perm), repeat=2):
                temp_perm = tuple(reverse_interval(perm, rev[0], rev[-1] - 1))
                temp_breaks = n_breakpoints(temp_perm)
                temp_transformation = current_perms[perm] + [str(rev[0]+1) + " " + str(rev[-1])]

                if temp_breaks == 0:
                    rev_hist.append(rev)
                    return dist, temp_transformation

                elif temp_breaks < min_breaks:
                    min_breaks = temp_breaks
                    new_perms = {temp_perm: temp_transformation}

                elif temp_breaks == min_breaks:
                    new_perms[temp_perm] = temp_transformation

        current_perms = new_perms

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        P, G = map(lambda x:x.replace("\n", "").split(), file.readlines())
        ans = greedy_algorithm(P, G)
        print(ans[0])
        print(*ans[1], sep="\n")