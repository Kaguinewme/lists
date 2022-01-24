# n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# print(n)
# a=[]
# for i in n:
#     if i not in a:a
#         a.append(i)
# print(a)

n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
print(n)
i=0
a=[]
while i<len(n):
    if n[i] not in a :
        a.append(n[i])
    i=i+1
print(a)