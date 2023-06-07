"""
Problem

Recall the definition of the Fibonacci numbers from 
“Rabbits and Recurrence Relations”, which followed the 
recurrence relation Fn=Fn−1+Fn−2

and assumed that each pair of rabbits reaches maturity 
in one month and produces a single pair of offspring 
(one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to 
achieve a dynamic programming solution in the case that all
rabbits die out after a fixed number of months. See Figure 4 
for a depiction of a rabbit tree in which rabbits live for three
months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100and m≤20.

Return: The total number of pairs of rabbits that will 
remain after the n-th month if all rabbits live for m months.
"""
import sys

n = int(input("Input n (number of months): "))
m = int(input("Input m (max age for rabbits): "))

data_structure = []
for i in range(m):
    data_structure.append(0)

data_structure[0] = 1

for i in range(n-1):
    new_rabbits = sum(data_structure[1:])
    temp_list = data_structure.copy()
    
    for j in range(1, len(data_structure)):
        temp_list[j] = data_structure[j-1]
    
    temp_list[0] = new_rabbits
    data_structure = temp_list

print(sum(data_structure))