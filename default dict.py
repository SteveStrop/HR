from collections import defaultdict
A=defaultdict(list)
B=[]
n,m = map(int,input().split())
for i in range(1,n+1):
    A[input()].append(i)
for i in range(m):
    B.append(input())
[print(*A[word]) if A[word] else print(-1) for word in B]
print(A)
print(B)

A=defaultdict(list)
A['a'] = [1, 2, 4]
A['b']= [3, 5]
print(A)
B=['a','b','c']

# for word in B:
#     if A[word]:
#         print (*A[word])
#     else:
#         print(-1)
[print(*A[word]) if A[word] else print(-1) for word in B]
