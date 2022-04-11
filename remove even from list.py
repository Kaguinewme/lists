list=[1,2,3,4,5,6,7,8,9]
i=1
a=[]
b=[]
while i<len(list):
    if i%2==0:
        a.append(list[i])
    else:
        b.append(list[i])
    i+=1
print(a)
