import random

computer = random.choice([-1, 0, 1])

youstr=input("Enter your choice")
youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr]
reversedict={1:"Snake", -1:"Water" , 0:"Gun"}


print(f"You chose {reversedict[you]}\nComputer Chose {reversedict[computer]}")
if(computer==you):
    print("Its a draw ")

else:    

    if(computer==-1 and you==1):
        print("you win")

    elif(computer==-1 and you==0):
        print("you Lose")
    elif(computer==1 and you==-1):
        print("you lose")
    elif(computer==1 and you==0):
        print("you win")

    elif(computer==-0 and you==1):
        print("you lose")

    elif(computer==0 and you==-1):
        print("you win")

    else:
        print("somehting went wrong")



