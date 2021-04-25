
#  Snake Water Gun Game

import random

def game(comp,you):

    if comp == you:
        return None 
    elif comp == "s":
        if you== "w":
            return False
        else:
            return True
    elif comp == 'w':
        if you== "s":
            return True
        else:
            return False

    elif comp=="g":
        if you== "s":
            return False
        else:
            return True




       
comp= random.randint(1,3)

if comp == 1:
    comp ="s"
elif comp == 2:
    comp= "w"
else:
    comp= "g"

you= input("Enter your choice: Snake(s) Water(w) and Gun(g)  :  ")

print(f"computer selected : {comp}")
print(f" You selected : {you} ")
a= game(comp,you)
if a== None:
    print(" Tie!!!...")
elif a:
    print(" You win !!!...")
else:
    print("You lose!!!...")