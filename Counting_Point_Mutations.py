"""
Problem

Given two strings s and t of equal length, the Hamming distance 
between s and t, denoted dH(s,t), is the number of corresponding
symbols that differ in s and t

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""
import sys

with open(sys.argv[1]) as file:
    data = file.readlines()
    
    dH = 0
    for i in range(len(data[0])-1):
        if data[0][i] != data[1][i]: dH += 1
    
    print(dH)