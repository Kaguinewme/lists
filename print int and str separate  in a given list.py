a="iam 40 years old"
s=list(a)
i=0 
while i<=len(a)-1:
    if s[i]=="4" or s[i]=="0":
        s[i]=int(s[i])
    print(type(s[i]),":",s[i])
    i+=1