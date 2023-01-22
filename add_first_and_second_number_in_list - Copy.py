list=[2,7,13,4,9]
i=0
sum=0
a=[]
while i<=len(list[:1]):
    a.append(list[i])
    sum=sum+a[i]
    print(list[i])
    i+=1
print(sum)