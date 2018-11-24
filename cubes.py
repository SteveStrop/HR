from collections import deque

#
with open('input00.txt', 'r')as file:
    for T in range(int(file.readline())):
        n = (int(file.readline()))
        cubes = deque(file.readline().split())
        while (len(cubes) > 3):
            big = max(list(cubes)[1:-2])
            if cubes.popleft() > big and cubes.pop() > big:
                print('No')
                break
        print('Yes')
