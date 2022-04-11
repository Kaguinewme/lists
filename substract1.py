list=[1,3,6,8,7,5,4,2,9]
i=0
a=1
b=[]
while i<len(list):
    c=list[i-a+1]
    b.append(c)
    a+=1
    i+=1
print(b)