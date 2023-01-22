num1 = int(input("enter the first no:"))
num2 = int(input("enter the second no:"))
if(num1 > num2 ): 
    lcm= num1
else:
    lcm= num2
while(True):
    if(lcm % num1 == 0 and lcm % num2 == 0):   
        print(lcm)
        break;
    lcm= lcm+ 1