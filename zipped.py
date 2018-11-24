N, X = map(int, input().split())
Y = [(list(map(float, input().split()))) for _ in range(X)]
for l in zip(*Y):
    print(round(sum(l) / X, 1))
