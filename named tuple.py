# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6
#
#
# 5
# MARKS      CLASS      NAME       ID
# 92         2          Calum      1
# 82         5          Scott      2
# 94         2          Jason      3
# 55         8          Glenn      4
# 82         2          Fergus     5


from collections import namedtuple

with open('input00.txt', 'r') as file:
    t = int(file.readline())
    G = namedtuple('G', file.readline().split())
    print('{:.2f}'.format(sum([int(G._make(file.readline().split()).MARKS) for _ in range(t)]) / t))
from collections import namedtuple


