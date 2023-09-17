import random
#from random import choise, randint(random int)

while True:
    characters = ["rock", "paper", "scissors"]
    cc = random.choice(characters)
    
    while True:
        print("choose your chracter\n1-rock\n2-paper\n3-scissors")
        x = input(": ")
        
        if x == "1":
            x = "rock"
            break
        elif x == "2":
            x = "paper"
            break
        elif x == "3":
            x = "scissors"
            break
        else:
            print("wrong choise, please try again\n")
    
    print(f"your choise: {x}")
    print(f"computer choise: {cc}\n")
    
    if x == "rock":
        if cc == "rock":
            print("draw\n")
        elif cc == "paper":
            print("computer wins\n")
        else:
            print("you win\n")
    
    elif x == "paper":
        if cc == "rock":
            print("you win\n")
        elif cc == "paper":
            print("draw\n")
        else:
            print("computer wins\n")
    
    else:
        if cc == "rock":
            print("computer wins\n")
        elif cc == "paper":
            print("you win\n")
        else:
            print("draw\n")
    
    print("to quit press 'q'\nto continue press any key\n")
    y = input().lower()
    
    if y == "q":
        print("see you soon :3")
        break
    