from itertools import combinations_with_replacement
string,k = input().split( ' ')
[print(*item,sep='') for item in combinations_with_replacement(sorted(list(string)),int(k))]


