a=[1,2,3,4,5,6,7,7,8,9,10,11,12,14,1,516,8,4]
b=[1,2,4,6,8,9,45,22,11,6,7,9,]
c=[]
for i in range(len(a)):
    if a[i] in b:
        c.append(a[i])
c=set(c)
print(c)