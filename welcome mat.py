y,x=map(int,input().split())
for i in range(1, y - 1, 2):
    print("-" * int((x - 3 * i) / 2) + ".|." * i + "-" * int((x - 3 * i) / 2))
print("-" * ((x - 7) // 2) + "WELCOME" + "-" * ((x - 7) // 2))
for i in range(y - 2, 0, -2):
    print("-" * int((x - 3 * i) / 2) + ".|." * i + "-" * int((x - 3 * i) / 2))

