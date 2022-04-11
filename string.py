list=['abc','xyz','aba','1221',"123421"]
i=0
count=0
while i<len(list):
    if len(list[i])>1 and list[i][0]==list[i][-1]:
        count=count+1
    i=i+1
print(count)