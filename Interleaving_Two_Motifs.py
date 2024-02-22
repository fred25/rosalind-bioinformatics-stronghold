"""
Problem

A string s is a supersequence of another string t if s contains t as a subsequence.

A common supersequence of strings s and t is a string that serves as a supersequence of both 
s and t. For example, "GACCTAGGAACTC" serves as a common supersequence of "ACGTC" and 
"ATAT". A shortest common supersequence of s and t is a supersequence for which there 
does not exist a shorter common supersequence. Continuing our example, "ACGTACT" is a 
shortest common supersequence of "ACGTC" and "ATAT".

Given: Two DNA strings sand t.

Return: A shortest common supersequence of s and t. If multiple solutions exist, you may output any one.
"""

import sys
from Extras.rosalind_functions import FASTA_to_dict

def SCS(s:str, t:str) -> str:
    
    if len(s) > len(t):
        s, t = t, s
    
    # create table
    table = [[0 for y in range(len(t)+1)] for x in range(len(s)+1)]
    
    #fill in the table
    for i in range(len(s)+1):
        for j in range(len(t)+1):
            
            #rules to fill in the table:
            # 1- first row or col 1, 2, 3, 4, ...
            # 2- if letters are equal for current space = upper-left +1
            # 3- else = min of upper and left neighbors
            
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif t[j-1] == s[i-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = min(table[i-1][j], table[i][j-1]) + 1
        
    #i = s | j = t
    supersequence = ""
    i, j = len(s), len(t)
    while True:
        if i == 0:
            supersequence += t[:j][::-1]
            return supersequence[::-1]
        
        elif j == 0:
            supersequence += s[:i][::-1]
            return supersequence[::-1]
        
        elif s[i-1] == t[j-1]:
            supersequence += s[i-1]
            i -= 1
            j -= 1
        
        else:
            if table[i-1][j] > table[i][j-1]:
                supersequence += t[j-1]
                j-=1
            else:
                supersequence += s[i-1]
                i-=1

with open(sys.argv[1]) as file:
    s, t = map(lambda x:x.replace("\n", ""), file.readlines())
    print(SCS(s, t))