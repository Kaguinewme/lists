
a = ["A","B"]
i=1
j=2
b=[]
while i<=j:
    k=0
    while k<len(a):
        c=(a[k]+str(i))
        b.append(c)
        k+=1
    i+=1
print(b)

