list=[1,2,3,3,6,5,4,4,6,8,9]
i=0
a=[]
count=0
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
        count+=1
    i+=1
print(count)