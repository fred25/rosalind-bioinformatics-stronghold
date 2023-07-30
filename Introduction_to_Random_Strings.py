from math import log10
import sys

DNA = ""
GC_contents = []

with open(sys.argv[1]) as file:
    data = file.readlines()
    DNA = data[0].replace("\n", "")
    for prob in data[1].split(" "):
        GC_contents.append(float(prob))

probs = []
for GC_cont in GC_contents:
    GC = GC_cont / 2
    AT = (1 - GC_cont) / 2
    p = 1
    for base in DNA:
        if base == "G" or base == "C":
            p *= GC
        if base == "A" or base == "T":
            p *= AT
    probs.append(p)

result = list(map(lambda x: "{:.3f}".format(log10(x)), probs))
print(*result)
