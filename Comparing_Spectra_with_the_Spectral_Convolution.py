from itertools import product
import sys

S1 = []
S2 = []

with open(sys.argv[1]) as file:
    S1, S2= map(lambda x:map(float, x.split()), file.read().split("\n")[:2])
    
minkowsi_dif = list(map(lambda x: round(x[0]-x[1], 5), product(S1, S2)))

print(minkowsi_dif.count(max(minkowsi_dif, key=lambda x:minkowsi_dif.count(x))))
print(max(minkowsi_dif, key=lambda x:minkowsi_dif.count(x)))