import math
import os
import random
import re
import sys
import string

nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
alnum = string.ascii_letters + string.digits
string = ""
string2=""
truth_table= []
for j in range(m):
    for i in range(n):
        string += (matrix[i][j])
        truth_table.append(matrix[i][j] in alnum)
try:
    start = truth_table.index(True)
    end = len(truth_table) - truth_table[::-1].index(True)
except ValueError:
    print("exception",string)
else:

    for letter in string:
        string2 += letter in alnum and letter or " "
    string2 = string2.rstrip()
    string2 = string2.strip()
    while "  " in string2:
        string2=string2.replace("  "," ")
    tail=string[end:]
    head=string[:start]
    print(head+string2+tail)


#
#**********DATA*********#
# 7 3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ir!
