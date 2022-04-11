a=[1.5,1,"savita",4,2.6,8,"kagui"]
i=0
x=[]
y=[]
z=[]
while i< len(a):
    if type(a[i])==float:
        x.append(a[i])
    elif type(a[i])==int:
        y.append(a[i])
    elif type(a[i])==str:
       z.append(a[i])
    i+=1 
print(x)
print(y)
print(z)