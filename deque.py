from collections import deque

# method_to_call = getattr(deque,'appendleft')
# print(method_to_call)
d = deque()
with open('input00.txt', 'r')as file:
    for _ in range(int(file.readline())):
        method = file.readline().split()
        getattr(d, method[0])(*((method[1]) if len(method) == 2 else ()))
print(*d)
