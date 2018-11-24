#
# counted_words = []
# count = 0
# while n-1:
#     word = word_list.pop()
#     while True:
#         try:
#             count += 1
#             word_list.remove(word)
#         except:
#             counted_words.append(count)
#             count=0
#             n-=1
#             break
# print(len(counted_words))
# print(*counted_words)

# from collections import OrderedDict
# d = OrderedDict()
# with open('input00.txt', 'r')as file:
#     n = int(file.readline())
#     for i in range(n):
#         word = file.readline()
#         d[word] = d.get(word, 0) + 1
# print(len(d))
# print(*d.values())

from collections import OrderedDict

d = OrderedDict()
n = int(input())
for i in range(n):
    word = input()
    d[word] = d.get(word, 0) + 1
print(len(d))
print(*d.values())
