user=input("enter the char:")
i=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
while i<len(user):
    if user[i]=="{":
        count1+=1
    if user[i]=="}":
        count2+=1
    if user[i]=="[":
        count3+=1
    if user[i]=="]":
        count4+=1
    if user[i]=="(":
        count5+=1
    if user[i]==")":
        count6+=1
    i+=1
if count1==count2 and count3==count4 and count5==count6:
    print(True)
else:
    print(False)


