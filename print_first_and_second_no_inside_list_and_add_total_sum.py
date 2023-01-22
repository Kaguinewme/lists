# list=[9,8,6,5,3,4,7,2]
# i=0
# a=[]
# while i<len(list[:2]):
#     a.append(list[i])
#     j=0
#     sum=0
#     while j<=len(a):
#         sum=sum+a[i]
#         j+=1
#     i+=1
# print(a)
# print(sum)

list=[5,7,9,4,2,5,7,9]  
i=0
a=[]
sum=0
while i<len(list[:3]):
    a.append(list[i])
    sum=sum+a[i]
    i+=1
print(a)
print(sum)
