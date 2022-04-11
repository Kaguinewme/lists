l=[1,23,1,3,4,23,4]	
a=[]
i=0
while i<len(l):
    if l[i] not in a:
        a.append(l[i])
    i=i+1
print(a) 