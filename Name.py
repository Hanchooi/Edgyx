import time
import random

def greeting():

    print("Hello!")

    name = input("What's your name ?")
    time.sleep(5)

    print("Hi,",name,"nice to meet you!")

def food():
    
    food = input("What do you wanna eat ? We have pizza and pasta.   \n")
    
    if food == "pizza":
        print("great!")
        
    elif food == "pasta":
        print("lovely!")
        
    else:
        print("Sorry, no food for you then./. Good bye!")
        
def game1():
    counts = 3
    answer = random.randint(1,10)
    while counts > 0:
        temp = input("Guess a number: ")
        guess = int(temp)
        
        if guess == answer:
            print("Wow, that's correct!")
            print("No cookie for you though.\n")
            break
        else:
            if guess < answer:
                print("Too small!\n")
                time.sleep(1)
            else:
                print("Too big!\n")
                time.sleep(1)
            counts = counts - 1
        print("You have",counts,"chance left.")

    if counts == 0:
        print("Too Bad! \nGame Over")
            Malachi Knight
def game2():
    
    counts = 1
    answer = random.randint(1,10)
    play = True
    
    while play:
        temp = input("Guess a number: ")
        guess = int(temp)
        
        if guess == answer:
            print("Wow, that's correct! You got it right with",counts,"attempt(s)!")
            print("No cookie for you though.\n")
            break
        else:
            if guess < answer:
                print("Too small!\n")
                
            else:
                print("Too big!\n")
        counts = counts + 1
        reply = str(input("Play again? (Y/N): "))
        
        if reply == "N":
            play = False
            
def game3():
    wait = random.randint(1,10)
    print("Ready...")
    time.sleep(wait)
    print("Go!")
    