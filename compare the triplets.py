a = (5, 6, 7)
b = (3, 6, 10)


def solve(a, b):
    y,z = zip(*[(int(a[i] > b[i]),int(b[i] > a[i])) for i in range(3)])
    return sum(y),sum(z)


print(*solve(a,b))
