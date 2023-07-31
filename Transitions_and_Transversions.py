import sys
from Extras.rosalind_functions import FASTA_to_dict

DNA1, DNA2 = tuple(FASTA_to_dict(sys.argv[1]).values())

transitions = 0
transversions = 0


def is_transition(n1: str, n2: str) -> bool:
    m = {"A": "G", "G": "A", "C": "T", "T": "C"}
    if m[n1] == n2:
        return True
    return False


for index in range(len(DNA1)):
    if DNA1[index] == DNA2[index]:
        continue

    if is_transition(DNA1[index], DNA2[index]):
        transitions += 1
        continue

    transversions += 1

print(round(transitions / transversions, 11))
