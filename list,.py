##create a program that takes 2 integers in form of string as an input and outputthe sum
##"2","6"
##"8","8"

a=input("enter the first no")
b=input("enter the sec no")
if a=="" and b=="":
    print(0)
elif a=="":
    print(b)
elif b=="":
    print(a)
if a!="" and b!="":
    print(str(int(a)+int(b)))
