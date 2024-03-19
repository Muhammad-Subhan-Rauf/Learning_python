"""
This is a ludo simulator. (this one does not assume snakes on the 
board only which players gets to 100 first)
"""

def ludo():
    import random
    player1=0
    player2=0
    count=1
    print("player1 score     player2 score")
    while player1<=100 or player2<=100:
        x=random.randint(1,6)
        if count%2==0:
            print(player1,end="")
            if player1+x <= 100:
                player1+=x
            count+=1
        else:
            print("                                      ",player2,)
            if player2+x <=100:
                player2+=x
            count+=1
        if player1>=100:
            print("\n",player1,end="")
            print("\n\nCongrats player1 you reached 100 first")
            break
        elif player2>=100:
            print("                                      ",player2,)
            print("\n\nCongrats player2 you reached 100 first")
            break
ludo()
input("")

    
            
