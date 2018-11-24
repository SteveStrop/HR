n =6
arr =[-4,3,-9,0,4,1]
print('{:.6f}'.format(len([x for x in arr if x > 0]) / n))
print('{:.6f}'.format(len([x for x in arr if x < 0])/n))
print('{:.6f}'.format(len([x for x in arr if x == 0])/n))
