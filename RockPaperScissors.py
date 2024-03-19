"""
This file is a simple rock paper scissors game against a computer.
"""


def ropasc():
    lst=["scissors","paper","rock"]
    import random
    x=random.randint(0,2)
    return lst[x]



lst=["scissors","paper","rock"]


user=""
user_score=0
comp_score=0
while user!="q":
    user=input("Choose rock or paper or scissors or \"q\" to quit: ").lower()
    comp=["rock","scissors","paper"]
    import random
    comp=ropasc()
    if user not in lst:
        print("Wrong input try again\n\n")
        continue
    elif user!="q":
        print("You chose",user,"and the computer chose",comp)
    elif user=="q":
        break
    
    
    
    if comp==user:
        print("It is a draw\n\n")
    elif comp=="rock" and user=="paper":
        print("Congrats you won\n\n")
        user_score+=1
    elif comp=="paper" and user=="scissors":
        print("Congrats you won\n\n")
        user_score+=1
    elif comp=="scissors" and user=="rock":
        print("Congrats you won\n\n")
        user_score+=1
    elif user not in lst:
        print("Wrong input try again\n\n")
    else:
        print("You lost this round\n\n")
        comp_score+=1
print("At the end your score is",user_score,"and the computers score is",comp_score,end=" ")
if comp_score>user_score:
    print("so the computer won. Better luck next time!!")
elif user_score>comp_score:
    print("so you won. CONGRATULATIONS")
else:
    print("so it was a draw. Try again")
input("Press enter to continue")
        
