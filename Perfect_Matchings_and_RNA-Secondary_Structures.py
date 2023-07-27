from Extras.rosalind_functions import FASTA_to_dict
from math import factorial
import sys

RNA = "".join(list(FASTA_to_dict(sys.argv[1]).values()))

print(factorial(RNA.count("A")) * factorial(RNA.count("G")))
