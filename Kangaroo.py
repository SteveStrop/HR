x1=43
v1=3
x2=43
v2=2

try:
    n=(x1-x2)/(v2-v1)
except ZeroDivisionError:
    n=-1
print((n%1==0and n>=0) and 'YES' or 'NO')

