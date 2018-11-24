import numpy

n, m = map(int, input().split())
a = numpy.array(list(map(int, input().split())), int)
b = numpy.array(list(map(int, input().split())), int)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
