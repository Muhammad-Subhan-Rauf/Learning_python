"""
This file asks user for a message in binary, and it then converts it to text (if readable)
"""

from datetime import date
from datetime import datetime
TextToTranslate=input("Enter a binary coded message:  ")


emp=""
lst=[]
TextToTranslate=TextToTranslate+" "
for i in TextToTranslate:
    if i=="0" or i=="1":
        emp+=i
    if i==" " :
        lst+=[emp]
        emp=""

def binaryToDecimal(x):
    res=0
    for i in str(x):
        if i!="0" and i!="1":
            return False
    for i in range(len(str(x))):
        ans=x%10
        res+=ans*(2**i)
        x=x//10
    return res

answer=[]
lst.pop(-1)
for j in lst:
    
    j=int(j)
    answer+=[binaryToDecimal(j)]
print(answer)
ugly=""
for h in answer:
    print(chr(h),end="")
    ugly+=chr(h)
f=input("Do you want to create a text File Y/N:   ").lower()
if f=="y":
    Now = datetime.now()
    current_time = Now.strftime("%H:%M:%S")
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    File=open("BinaryDecodedFile.txt","a+")
    File.write(f"This File was Created on {d2} at {current_time}")
    File.write(ugly)
    
    File.close()
input("\npress enter to continue")



