# a=[1,2,3,4,5,6]
# print(a)
# b=a
# print(b)
# a[0]=20
# print(a)
# print(b)

# a=[1,2,3]
# print(a)
# b=list(a)
# print(b)
# a[0]=30
# print(a)
# print(b)

# a=[1,2,3],[4,5]
# print(a)
# b=list(a)
# print(b)
# a[0][0]=25
# print(a)
# print(b)

a=[[1,2,3],[4,5]]
print(a)
import copy
b=copy.deepcopy(a)
print(b)
a[0][0]=25
print(a)
print(b)