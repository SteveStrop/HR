s = 7
t = 11
a = 5
b = 15
m = 3
n = 2
apples = [-2, 2, 1]
oranges = [5, -6]

for fruit in zip((a, b), (apples, oranges)) :
    print(sum(1 for f in fruit[1] if fruit[0] + f in range(s, t + 1)))
