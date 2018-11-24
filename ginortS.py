l = []
u = []
o = []
e = []
s = "Sorting1234"
for char in s:
    if char.islower():
        l.append(char)
    elif char.isupper():
        u.append(char)
    elif char.isdigit():
        char = int(char)
        if char % 2 == 0:
            e.append(char)
        else:
            o.append(char)
print(*sorted(l), *sorted(u), *sorted(o), *sorted(e), sep="")

print(*sorted(s, key=lambda c: (c.isdigit() - c.islower(), c.isdigit() and int(c) % 2 == 0 or False, c)), sep='')

# c = "A"
# print(c.isdigit())
# print(c.islower())
# print(c.isdigit() - c.islower())
#
# for c in s:
#     print((c.isdigit() - c.islower(), c in '02468', c))

c = "S"
print(c.isdigit() and int(c) % 2 == 0 or False)
