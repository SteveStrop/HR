def rotLeft(a,d):
    for i in range(d):
        a.append(a.pop(0))
    return a


a= [1,2,3,4,5]
d=4
result = rotLeft(a,d)
print (result)
