a=["a","b","a","d","b"]
user=input("enter") 
i=0
c=0
while i<len(a):
    if user in a[i]:
        c+=1
    i+=1
print(c)