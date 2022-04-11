list=[2,4,6,8]
i=1
a=3
b=[]
while i<len(list):
    c=list[i-a+2]
    b.append(c)
    a+=1
    i+=1
print(b)