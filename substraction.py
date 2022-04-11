a=[30,10,10,5,25,5]
i=0
x=[]
while i<len(a):
    c=a[i+1]
    b=a[i]-c
    x.append(b)
    i=i+2
print(x)