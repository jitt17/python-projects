
import random as r
import math as m
def guess():
    a=int(input("Enter lower limit :"))
    b=int(input("Enter Upper limit :"))
    
    computer = r.randint(a,b)
    
    chance= m.ceil(m.log(b - a +1,2))
    attempt = 1
    result = False
    while attempt != chance:
        guess=int(input(f"Guess the number between {a} to {b} : " ))
        if(guess == computer):
            print("Congratulation!! You Guess Right Number..")
            print(f"you Guess {computer} number in {attempt}.")    
            
            result= True
            break      
        elif(guess<computer):
            print("Please ! Enter Higher Number..")
            attempt += 1
        elif(guess>computer):
            print("Please ! Enter Lower Number..")
            attempt += 1
    
    if not result:
        print(f"The number is {computer}")
        
        print("Better Luck Next time")
        
guess()
again=input("You want Play Again ?? Yes/No :")
if(again.lower() == "yes"):
    guess()
        
