# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']

list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list2 = []
for x in range(1,4):
   list2.append(list1[x])
print(list2)