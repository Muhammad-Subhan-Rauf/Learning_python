"""
One of three Time table creators i created while learning python
"""

def NumToAlph(x):
    x=int(x)    
    x=x+64
    return chr(x)
letter=2
letser=3
import xlsxwriter
sublst=[]
datelst=[]
timelst=[]
x=1
name=input("What should the title of the file be (without the file extension)?    ")
name=name+".xlsx"
workbook=xlsxwriter.Workbook(name)
worksheet=workbook.add_worksheet()
u=int(input("How many subjects do you have? "))
for i in range(u):
    print("\nEnter Subject",x,end="   ")
    sublst+=[input("")]
    
    print("Enter first date (monday/tuesday) for Subject",x,"only:",end="   ")
    datelst+=[input("")]
    
    print("Enter time for Subject",x,end="   ")
    timelst+=[input("")]

    worksheet.write(str(NumToAlph(letter))+str(letser-1),sublst[i])
    if datelst[i]=="monday":
        worksheet.write(str(NumToAlph(letter))+str(letser),timelst[i])
        worksheet.write(str(NumToAlph(letter))+str(letser+2),timelst[i])
        worksheet.write(str(NumToAlph(letter))+str(letser+4),timelst[i])
    elif datelst[i]=="tuesday":
        worksheet.write(str(NumToAlph(letter))+str(letser+1),timelst[i])
        worksheet.write(str(NumToAlph(letter))+str(letser+3),timelst[i])
    x+=1
    letter+=1
    

worksheet.write("A3","Monday")
worksheet.write("A4","Tuesday")
worksheet.write("A5","Wednesday")
worksheet.write("A6","Thursday")
worksheet.write("A7","Friday")

workbook.close()
    
