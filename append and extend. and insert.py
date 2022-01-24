# list1=['a','b','c']
# list2=[1,2,3]
# list1.append(list2)
# print(list1)

# list1=['a','b','c']
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)

# a=["1234"]
# b=["abcd"]
# b.extend(a)
# print(b)

# list=["sam","niki","priya"]
# list.insert(2,5)
# print(list)

a=["1","2","3","4","5","6"]
i=0
c=[]
while i<len(a)-1:
    b=(a[i]+a[i+1])
    c.append(b)
    i=i+2
print(c)

