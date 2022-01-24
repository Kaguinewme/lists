# a="missisippy"
# print(a)
# countm=a .count('m')
# counti=a.count("i")
# counts=a.count("s")
# countp=a.count("p")
# county=a.count("y")
# print("m",countm)
# print("i",counti)
# print("s",counts)
# print("p",countp)
# print("y",county)

a="missisippy"
i=0
while i<len(a):
    list=a[i]
    count=0
    j=0
    while j<len(a):
        if a[j]==list:
            count=count+1
        j=j+1
    print(list,count)
    i+=1
    

   




        