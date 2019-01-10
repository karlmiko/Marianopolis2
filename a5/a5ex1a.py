
"""
Karl Michel Koerich, 1631968
Friday, April 27
R. Vincent , instructor
Assignment 5
"""

fasta = open("patient1.fasta")
fasta.readline().strip()

st = fasta.read()



print(type(st))
print(st)

from re import *

result = search(r'(gcg)([ac]gg)+(ctg)', st)
str_result = result.group()

print("Number of cgg/agg repeats found:", ((len(str_result) - 6)/3))

