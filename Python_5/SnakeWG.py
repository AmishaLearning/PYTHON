#Snake Water Gun
# import random

# print("WELCOME TO THE GAME OF SNAKE - WATER - GUN\n")
# print("1-SNAKE\n2-WATER\n3-GUN \n")

# choice_user = int(input("Enter your choice : "))
# choice_comp = random.randint(1,4)
# print(f"The Choice of Computer : {choice_comp}")

# if choice_user == 1 and choice_comp == 1 or choice_user == 2 and choice_comp == 2 or choice_user == 3 and choice_comp == 3 :
#     print("The Result is DRAW")
    
# elif (choice_user == 1 and choice_comp == 2) or (choice_user == 2 and choice_comp == 3) or (choice_user == 3 and choice_comp == 1) :
#     print("The USER won and the COMPUTER lost")
    
# elif (choice_user == 1 and choice_comp == 3) or (choice_user == 2 and choice_comp == 1) or (choice_user == 3 and choice_comp == 2) :
#     print("The CONPUTER won and the USER lost")


#Using String
# import random

# print("WELCOME TO THE GAME OF SNAKE - WATER - GUN\n")
# print("1-SNAKE\n2-WATER\n3-GUN \n")
# choice_user = input("Enter ur Choice(as String) : ".upper())
# print(f"User's Choice : {choice_user.upper()}")

# list1 = ["SNAKE", "WATER", "GUN"]
# choice_comp = random.choice(list1)
# print(f"Computer's Choice : {choice_comp}")

# if choice_user.upper() == "SNAKE" and choice_comp == "SNAKE" or choice_user.upper() == "WATER" and choice_comp == "WATER" or choice_user.upper() == "GUN" and choice_comp == "GUN" :
#     print("The Result is DRAW")
    
# elif (choice_user.upper() == "SNAKE" and choice_comp == "WATER") or (choice_user.upper() == "WATER" and choice_comp == "GUN") or (choice_user.upper() == "GUN" and choice_comp == "SNAKE") :
#     print("The USER won and the COMPUTER lost")
    
# elif (choice_user.upper() == "SNAKE" and choice_comp == "GUN") or (choice_user.upper() == "WATER" and choice_comp == "SNAKE") or (choice_user.upper() == "GUN" and choice_comp == "WATER") :
#     print("The COMPUTER won and the USER lost")

#Using for loop

import random

print("~~~~~~~~~~~~~WELCOME TO THE GAME OF SNAKE - WATER - GUN~~~~~~~~~~~~~~~~~~\n")
rounds = int(input("Enter the number of rounds you want to play : "))
print("1-SNAKE\n2-WATER\n3-GUN \n")

win_user = 0
win_comp =0

for i in range(rounds):

    print(f"Round {i + 1}:")
    
    choice_user = input("Enter ur Choice(as String) : ".upper())
    print(f"User's Choice : {choice_user.upper()}\n")

    list1 = ["SNAKE", "WATER", "GUN"]

    choice_comp = random.choice(list1)
    print(f"Computer's Choice : {choice_comp}\n")
    
    if choice_user.upper() == choice_comp :
        win_user = 0
        win_comp = 0
        
    elif (choice_user.upper() == "SNAKE" and choice_comp == "WATER") or (choice_user.upper() == "WATER" and choice_comp == "GUN") or (choice_user.upper() == "GUN" and choice_comp == "SNAKE") :
        
        win_user += 1 
        print(f"Number of times USER won     : {win_user}\n")
        print(f"Number of times COMPUTER won : {win_comp}\n")
        
    elif (choice_user.upper() == "SNAKE" and choice_comp == "GUN") or (choice_user.upper() == "WATER" and choice_comp == "SNAKE") or (choice_user.upper() == "GUN" and choice_comp == "WATER") :
        
        win_comp += 1
        print(f"Number of times USER won     : {win_user}\n")
        print(f"Number of times COMPUTER won : {win_comp}\n")

if win_user > win_comp:
    print(f"The Game Ended After Round {rounds} USER is the WINNER!!\n")

elif win_user < win_comp:
    print(f"After Round {rounds} COMPUTER is the WINNER!!\n")

else:
    print(f"The Game Ended After Round {rounds} THE GAME IS DRAW")
        
        





