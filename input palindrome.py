string=input("enter the string=")
rev_string=string[::-1]
print("reverse string:", rev_string)
if string==rev_string:
    print("string is s palindrone")
else:
    print("string is not a palindrone")