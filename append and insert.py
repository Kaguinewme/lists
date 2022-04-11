num=[11,1,13,14,16,10]
i=0
a=[]
while i<len(num):
    if num[i]>11 :
        a.append(num[i])
    i+=1
a.insert(0,-1)
a.insert(5,-1)
print(a)
