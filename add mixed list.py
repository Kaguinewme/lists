list=[3,5,"sk",2,4,1]
i=0
sum=0
a=[]
while i<len(list):
    if type(list[i])==int:
        a.append(list[i])
    i+=1
j=0
while j<len(a):
    sum=sum+a[j]
    j+=1
print(sum)






   