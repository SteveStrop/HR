from itertools import groupby
s=input()
print(*[(len(list(b)),int(a)) for a,b in groupby(s)])
