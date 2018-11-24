from collections import OrderedDict
ordered_dict = OrderedDict()
with open('input00.txt', 'r') as file:
    for _ in range(int(file.readline())):
        f, _, p = file.readline().rpartition(' ')
        ordered_dict[f] = ordered_dict.get(f, 0) + int(p)
[print(k, v) for k, v in ordered_dict.items()]
