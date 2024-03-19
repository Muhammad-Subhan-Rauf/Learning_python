"""
This file helps create VBA prank files that never close unless the 
computer is shut down and restarted. In some cases closing the file 
from task manager might work but not on all devices.
"""


from telnetlib import DO


x=input("Do you want to create a prank file?(Y/N) ").lower()
if x=="y":
    subhan=open("subhan.vbs",("w+"))

    subhan.write("Do")
    subhan.write("\n")
    u=0
    while x!="":
        x=input("Enter the prank message:  ")
        if x=="":
            break
        u+=1
        
        y=input("Enter the title of the prank message:  ")
        subhan.write("msg"+str(u)+"=msgbox(\"")
        subhan.write(x)
        subhan.write("\",o,\"")
        subhan.write(y+"\")")
        subhan.write("\n")
        subhan.write("Loop")

    
