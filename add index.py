
a=[12,13,24,234,12345]
i=0
while i<len(a):
    list=str(a[i])
    j=0
    sum=0
    while j<len(list):
        sum=int(list[j])+sum
        j+=1
    i+=1
    print(sum)


        
    