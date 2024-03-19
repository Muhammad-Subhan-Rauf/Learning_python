"""
This file converts simple text into goofy text that is used to 
portray sarcasm in ones text messages
"""


def goofytext(x):
    rando=["yes","no"]
    import random
    answer=""

    for j in x:
        f=random.choice(rando)
        if f=="yes":
            answer+=j
        elif f=="no":
            answer+=j.upper()
    print(answer)
x=input("enter text to make it goofy:   ")
goofytext(x)