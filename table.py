user_input=int(input("enter the number:-"))
i=1
a=[]
while i<=user_input:
    j=1
    b=[]
    while j<=10:
        table = (i*j)
        b.append(table)
        j=j+1
    print(i,b,end=",")
    i=i+1