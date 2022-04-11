
a=["What is the capital of India?"]
b=["Chandigarh","Bhopal","Chennai","Delhi"]
solution=[4]
i=0
j=0
while i<len(a) and j<len(b):
    print(a[i])
    k=0
    while k<(len(b)):
        print(b[k])
        k+=1
    sol=int(input("Enter the number:"))
    if sol==solution[i]:
        print("Congratulations! Correct answer")
    else:
        print("Better luck next time")
    print()
    i+=1
    j+=1