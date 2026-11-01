import random
print("+-----------------------------------+")
print("|           NUMBER GUESSING         |")
print("|               GAME                |")
print("+-----------------------------------+")
comp=random.randint(1,9)
no_attempt=0
while no_attempt<4:
    no_attempt_left= 4-no_attempt
    num=int(input("Enter an no between 1 and 9 :-",))
    if num==comp:
        print("Congratulations you won :)")
        break
    elif num>comp:
        print("Guess lower")
        no_attempt+=1
        no_attempt_left= 4-no_attempt
        print("no of attempt left :-",no_attempt_left)
    elif num<comp:
        print("Guess higher")
        no_attempt+=1
        no_attempt_left= 4-no_attempt
        print("no of attempt left :-",no_attempt_left)
if no_attempt==4:
    print("You lost :(")
    