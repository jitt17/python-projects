
'''
1 snake
-1 water
0 gun
'''
import random as r



def snake_game():
    computer = r.choice([0,-1,1])
    youstr=input("Enter your choice :")
    youdict={"s":1,"w":-1,"g":0}
    you=youdict[youstr]

    rdict={1:"Snake",-1:"Water",0:"Gun"}

    print(f"your choise is {rdict[you]} and \ncomputer choise {rdict[computer]}")

    if(computer==you):
        print("its Draw !!!")
    else:
        if(computer==-1 and you==0):
            print("You lose !")
        elif(computer==-1 and you==1):
            print("You won !")
        elif(computer==1 and you==0):
            print("You win !")
        elif(computer==1 and you==-1):
            print("You win !")
        elif(computer==0 and you==1):
            print("You lose !")
        elif(computer==0 and you==-1):
            print("You win !")
        else:
            print("wrong")

snake_game()



