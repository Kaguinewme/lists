a=[[1,2,3],[4,5,1],[6,7,1]]
i=0
sum=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j]<=3:
           sum=sum+a[i][j]
        j+=1
    i+=1
print(sum)
        
        