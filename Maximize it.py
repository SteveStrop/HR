K=3
M=1000
data = [
    '2 5 4',
    '3 7 8 9',
    '5 5 7 8 9 10'
]
def s(m,*args):
    total=0
    for X in args:
        total+=X**2
    return total % m
lines=[]
length=[]
for i in range(K):
    lines.append(data[i].split(' '))
    length.append(int(lines[i].pop(0)))
    # lines[i]=[int(item) for item in lines[i]]


for i in range(K):
    for j in range(length[i]):
        print(lines[i][j],end='')
    print()



# print(s(M,(5,9,10)))
