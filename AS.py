N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
print(*sorted(data, key=lambda c: c[K]))

