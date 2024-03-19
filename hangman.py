"""
This file is a non-functional Hangman game
"""

def hangman():
    import getpass
    import random

    lst=[]
    finlst=[]
    ans=[]
    tries=0
    host=getpass.getpass('Host please enter word for hangman: ').lower()
    hints=int(input("Host how many hints do you want to give?: "))
    for i in host:
        lst+=[i]
    finlst=lst.copy()
    while tries<=6:
        
        answer=input("Players enter your guess or write\"word\" if you have guessed the word: ").lower()
        
        if hints>0:
            if answer=="hint" or answer=="hints":
                x=random.choice(finlst)
                print("You have used one of your hints. \nA correct letter is",x,"\nYou have",hints,"remaining")
                hints-=1
        if host!="word":
            if answer=="word":
                answer=input("Enter The word you have guessed: ").lower()
                if answer==host:
                    print("You have correctly guessed the word", host)
            elif len(answer)>1:
                print("Error")
                print("")
                return False
        if answer not in lst:
            tries+=1
            print("That is not correct, you have",7-tries,"tries remaining. You also have",hints,"hints remaining.")
            print("\nType hint if you want a hint\n")
        elif answer in lst:
            print("That is a correct letter")
            finlst.remove(answer)
            ans+=[answer]
            
        if set(ans)==set(lst):
             print("YOU WIN!!!! You successfully guessed",host)
    if tries==7:
        print("Better luck next time..... The correct word was",host)
    
        
hangman()
