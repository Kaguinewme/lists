list=["1","2","3","4","5","6","7","8"]
i=0
a=[]
while i<len(list):
    b=list[i]+list[i+1]
    a.append(b)
    i+=2
print(a)