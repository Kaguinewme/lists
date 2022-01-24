print("welcome to kbc")
question=[" what is the capital of india",
          "what is the capital of manipur",
          "how many district are there in manipur"]
option=[["seven","eight","nine"],
        ["tml", "imphal","bishnupur"],
        ["ten","twelve","sixteen"]]
solution=[1,2,3]
life5050=[["seven","eight"],["imphal","bishnupur"],["ten","sixteen"]]
life=[1,1,2]
i=0
j=0
count=0
while i<len(question) and j<len(option):
    print(j+1,question[i])
    k=0
    while k<len(option)+1:
        print(k+1,option[j][k])
        k+=1
        life=input("do you want 5050 life?yes or no:")
        if life=="yes":
            if count==0:
                a=0
            while a<len(life[i]):
                print(a+1,life[i][j])
                a+=1
            count+=1
            sol1=int(input("enter your solution"))
            if sol1==life[i]:
                print("congrats! your ans is correct")
            else:
                print("sorry! your ans is incorrect")
                break
        else:
            print("your lifeline has been used")
        sol=int(input("enter your solution"))
        if sol==solution[i]:
            print("congratulation!your ans is correct")
        else:
            print("better luck next time")
            
            
            
        
            
                
                   
               
                    
                    
                
            

