ch=input("enter any character")
a=[]
b=[]
i=0
while i<=1:
    if ch[i] not in ch:
        a.append(True, (ch[i]))
    else:
        if ch[i] in a:
            b.append(ch[i])
    i+=1
print(a)
print(b)
            
    

      