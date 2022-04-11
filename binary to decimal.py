
binary_number=[1,0,0,1,1,0,1,1]
d=0
i=1
for digit in binary_number:
    digit=int(digit) 
    d=d+(digit*i)
    i=i*2
print("decimal value=", d)

