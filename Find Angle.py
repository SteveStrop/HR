#for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
i=5
x=[*range(1,i+1)]
y=[*range(i,0,-1)]
#print(*[*range(1,i+1)],*[*range(i,0,-1)][1:],sep='')
for a in x:
    print(type(a))

