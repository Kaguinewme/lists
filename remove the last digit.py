list=[1234,1245,456,321]
i=0
last=0
while i<len(list):
    if list[i]>=1:
        last=list[i]//10
    i+=1
    print(last,end=" ")