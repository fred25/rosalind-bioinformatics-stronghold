"""
Problem

A reversal of a permutation creates a new permutation by inverting some
interval of the permutation; (5,2,3,1,4), (5,3,4,1,2), and (4,1,2,3,5)
are all reversals of (5,3,2,1,4). The reversal distance between two 
permutations π and σ, written drev(π,σ), is the minimum number of
reversals required to transform π into σ (this assumes that π and σ have 
the same length).

Given: A collection of at most 5 pairs of permutations, all of which have length 10.

Return: The reversal distance between each permutation pair.
"""
import sys

# Special thanks for https://github.com/erexhepa
# Special thanks for Arianna Locatelli
# I've read a lot of code from both to solve this


def n_breakpoints(perm: str) -> int:
    """
    Function that calculates the number of breakpoints
    **Breakpoint = place where there are two consecutives numbers
                    side by side ex: 78 98
    """
    bk = 0
    added_perm = [0] + list(perm) + [len(perm) + 1]
    for index in range(len(added_perm) - 1):
        if abs(added_perm[index] - added_perm[index + 1]) != 1:
            bk += 1
    return bk


def breakpoints_indices(perm: list) -> list:
    # return the indices of every breakpoint
    indices = []
    added_perm = [0] + list(perm) + [len(perm) + 1]
    for index in range(len(added_perm) - 1):
        if abs(added_perm[index] - added_perm[index + 1]) != 1:
            indices.append(index)
    return indices


def reverse_interval(perm, i, j):
    return perm[:i] + perm[i : j + 1][::-1] + perm[j + 1 :]


def greedy_algorithm(perm1: list, perm2: list) -> int:
    from itertools import product

    # transform the permutations in (123...10) and other with the
    # same transformations as the original
    identity = {value: i + 1 for i, value in enumerate(perm2)}
    norm_perm = [identity[value] for value in perm1]

    # variables
    norm_perm = tuple(norm_perm)
    current_perms = [norm_perm]
    min_breaks = n_breakpoints(norm_perm)
    dist = 0

    while True:
        new_perms = []
        dist += 1

        for perm in current_perms:
            for rev in product(breakpoints_indices(perm), repeat=2):
                temp_perm = tuple(reverse_interval(perm, rev[0], rev[-1] - 1))
                temp_breaks = n_breakpoints(temp_perm)

                if temp_breaks == 0:
                    return dist

                elif temp_breaks < min_breaks:
                    min_breaks = temp_breaks
                    new_perms = [temp_perm]

                elif temp_breaks == min_breaks:
                    new_perms.append(temp_perm)

        current_perms = new_perms



if __name__ == '__main__':
    reversal_distances = []
    data = []

    current = []
    with open(sys.argv[1]) as file:
        for line in file.readlines():
            if line[0].isnumeric():
                current.append(tuple(map(int, line.replace("\n", "").split(" "))))
            else:
                data.append(current)
                current = []

    data.append(current)

    for p1, p2 in data:
        if p1 != p2:
            reversal_distances.append(
                min(greedy_algorithm(p1, p2), greedy_algorithm(p2, p1))
            )
        else:
            reversal_distances.append(0)

    print(*reversal_distances)
