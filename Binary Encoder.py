"""
This file asks user for a message in english, and it then converts it to binary (if readable)
"""

from datetime import date
from datetime import datetime


def TextToBinary(x):
    lst=[]
    emp=""
    x=x+" "
    for i in x:
        if i!=" ":
            emp+=i
        if i==" ":
            lst+=[emp+" "]
            emp=""
    fnlst=[]
    for j in lst:
        for h in j:
            g=ord(h)
            fnlst+=[g]
    print(fnlst)
    empty_string=""
    remain=""
    for q in fnlst:
        remain+=str(bin(q).replace("0b",""))
        remain+=" "
    return remain


x=input("Enter Text for Encoding:   ")    
print(TextToBinary(x))
f=input("Do you want to create a text File Y/N:   ").lower()
if f=="y":
    
    Now = datetime.now()
    current_time = Now.strftime("%H:%M:%S")
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    text="This File was Created on"+" "+str(d2)+" "+"at"+" "+str(current_time)
    File=open("BinaryEncodedFile.txt","w+")
    
    File.write(text)
    File.write("\n")
    File.write("\n")
    File.write(TextToBinary(x))
    File.write("\n")
    File.write("\n")
    File.write("\n")
    File.close()
input("press enter to continue")