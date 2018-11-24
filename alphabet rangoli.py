alpha = "abcdefghijklmnopqrstuvwxyz"

n = 5
l = []
for i in range(n):
    s = "-".join(alpha[i:n])
    l.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))

# print('\n'.join(l[::-1]+l[1:]))

s= "0123456789"
print(s[0])
print (s[::-1])