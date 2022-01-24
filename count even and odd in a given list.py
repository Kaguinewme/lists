# elements=[23,14,56,12,19,9,15,25,31,42,43]
# even=0
# odd=0
# i=0
# while i<len(elements):
#     if elements [i]%2==0:
#         even=even+1
#     else:
#         odd=odd+1
#     i=i+1
# print("no of even",even)
# print("no of odd",odd)

elements=[23,14,56,12,19,9,15,25,31,42,43]
sum_even=0
sum_odd=0
i=0
while i<len(elements):
    if elements [i]%2==0:
       sum_even=sum_even+elements[i]
    else:
      sum_odd=sum_odd+elements[i]   
    i=i+1
print("sum of even",sum_even)
print("sum of odd",sum_odd)


        
        