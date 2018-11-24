from itertools import combinations
N = 10
s = 'a a e i o a f g h k'
K = 3
s = s.split(' ')
C = list(combinations(s, K))
print(sum([1 for item in C if 'a' in item]) / len(C))

