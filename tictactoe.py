"""
A simple tic tac toe game against a computer
"""

import random
lst=["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
robo=[]
user=[]

while len(lst)>0:
    print("The remaining values are:",lst)
    x=input("Enter a row(a,b,c) and a column(1,2,3)=  ").lower()
    
    if x=="a1":    
        lst.remove("a1")
        user.append(x)
    elif x=="a2":
        lst.remove("a2")
        user.append(x)
    elif x=="a3":
        lst.remove("a3")
        user.append(x)
    elif x=="b1":
        lst.remove("b1")
        user.append(x)
    elif x=="b2":
        lst.remove("b2")
        user.append(x)
    elif x=="b3":
        lst.remove("b3")
        user.append(x)
    elif x=="c1":
        lst.remove("c1")
        user.append(x)
    elif x=="c2":
        lst.remove("c2")
        user.append(x)
    elif x=="c3":
        lst.remove("c3")
        user.append(x)
    else:
        print("Wrong input")
        break
    
    robot = random.choices(lst)

    if robot==["a1"]:
        print("The robot chose a1")
        lst.remove("a1")
        robo.append(robot)
    elif robot==["a2"]:
        print("The robot chose a2")
        lst.remove("a2")
        robo.append(robot)
    elif robot==["a3"]:
        print("The robot chose a3")
        lst.remove("a3")
        robo.append(robot)
    elif robot==["b1"]:
        print("The robot chose b1")
        lst.remove("b1")
        robo.append(robot)
    elif robot==["b2"]:
        print("The robot chose b2")
        lst.remove("b2")
        robo.append(robot)
    elif robot==["b3"]:
        print("The robot chose b3")
        lst.remove("b3")
        robo.append(robot)
    elif robot==["c1"]:
        print("The robot chose c1")
        lst.remove("c1")
        robo.append(robot)
    elif robot==["c2"]:
        print("The robot chose c2")
        lst.remove("c2")
        robo.append(robot)
    elif robot==["c3"]:
        print("The robot chose c3")
        lst.remove("c3")
        robo.append(robot)
    
    if ("a1" in user and "a2" in user and "a3" in user):
        print("YOU WIN!!!!!!!")
        print("You chose a1 a2 and a3 to win")
        break

    elif ("b1" in user and "b2" in user and "b3" in user):
        print("YOU WIN!!!!!!!")
        print("You chose b1 b2 and b3 to win")
        break

    elif ("c1" in user and "c2" in user and "c3" in user):
        print("YOU WIN!!!!!!!")
        print("You chose c1 c2 and c3 to win")
        break

    elif ("a1" in user and "b1" in user and "c1" in user):
        print("YOU WIN!!!!!!!")
        print("You chose a1 b1 and c1 to win")
        break

    elif ("a2" in user and "b2" in user and "c2" in user):
        print("YOU WIN!!!!!!!")
        print("You chose a2 b2 and c2 to win")
        break
    elif ("a3" in user and "b3" in user and "c3" in user):
        print("YOU WIN!!!!!!!")
        print("You chose a3 b3 and c3 to win")
        break
    elif ("a1" in user and "b2" in user and "c3" in user):
        print("YOU WIN!!!!!!!")
        print("You chose a1 b2 and c3 to win")
        break

    elif ("a3" in user and "b2" in user and "c1" in user):
        print("YOU WIN!!!!!!!")
        print("You chose a3 b2 and c1 to win")
        break
    
    elif (["a1"] in robo and ["a2"] in robo and ["a3"] in robo):
        print("you loose!!! Better luck next time")
        break

    elif (["b1"] in robo and ["b2"] in robo and ["b3"] in robo):
        print("you loose!!! Better luck next time")
        break

    elif (["c1"] in robo and ["c2"] in robo and ["c3"] in robo):
        print("you loose!!! Better luck next time")
        break

    elif (["a1"] in robo and ["b1"] in robo and ["c1"] in robo):
        print("you loose!!! Better luck next time")
        break

    elif (["a2"] in robo and ["b2"] in robo and ["c2"] in robo):
        print("you loose!!! Better luck next time")
        break
    elif (["a3"] in robo and ["b3"] in robo and ["c3"] in robo):
        print("you loose!!! Better luck next time")
        break
    elif (["a1"] in robo and ["b2"] in robo and ["c3"] in robo):
        print("you loose!!! Better luck next time")
        break

    elif (["a3"] in robo and ["b2"] in robo and ["c1"] in robo):
        print("you loose!!! Better luck next time")
        break
    elif len(lst)<1:
        print("ITS A DRAW")
        break
        

    print("\nUser Chose:",user,"\n")
    print("\n \nRobot chose:",robo,"\n")