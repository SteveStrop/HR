from itertools import product
#
# A = [1, 2]
# B = [3, 4]
# print(list(product(A, B)))

# A=input()
# B=input()

# A = tuple(*A)
# print (A,B)


# A= '1 2'
# A=A.split(' ')
# for i in range(len(A)):
#     A[i]=int(A[i])
# print(A)

A = map(int,input().split(' '))
B = map(int,input().split(' '))

print(*product(A,B))
