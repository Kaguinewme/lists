
list=[1,3,2]
i=0
a=[]
while i<len(list)-1:
    c=list[i+1]-list[i]
    j=0
    if c<0:
        j=j-c
    else:
        a.append(c)
    i+=1
a.append(j)
print(a)
    