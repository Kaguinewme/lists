 ## to count positive and negative number and print the total sum of
##negative number 
a=[1,-2,3,-4,5,-6,7,8,-9]
pos_num=0
neg_num=0
i=0
sum=0
while i<len(a):
    if a[i]>= 0:
        pos_num+=1
    else: 
        neg_num+=1
        sum=sum+a[i]
    i+=1   
print("positive number in the list:",pos_num)
print("negative number in the list:",neg_num) 
print(sum,"negative")   