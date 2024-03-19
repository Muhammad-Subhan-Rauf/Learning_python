"""
One of three Time table creators i created while learning python
"""

def compute_rows(text, width):
    if len(text) < width:
        return 1
    phrases = text.replace('\r', '').split('\n')

    rows = 0
    for phrase in phrases:
        if len(phrase) < width:
            rows = rows + 1
        else:
            words = phrase.split(' ')
            temp = ''
            for idx, word in enumerate(words):
                temp = temp + word + ' '
                # check if column width exceeded
                if len(temp) > width:
                    rows = rows + 1
                    temp = '' + word + ' '
                # check if it is not the last word
                if idx == len(words) - 1 and len(temp) > 0:
                    rows = rows + 1
    return rows



import time
def NumToAlph(x):
    x=int(x)    
    x=x+64
    return chr(x)
letter=2
import os
letser=3
secs=3
import xlsxwriter
sublst=[]
datelst=[]
timelst=[]
x=1
name=input("What should the title of the file be (without the file extension)?    ")
name=name+".xlsx"
print("this will create an excel file")
print("with your timetable\t")


workbook=xlsxwriter.Workbook(name)
worksheet=workbook.add_worksheet()
worksheet.set_default_row(20)
worksheet.set_default_row(hide_unused_rows=True)

u=int(input("How many subjects do you have? "))
for i in range(u):
    print("\nEnter Subject",x,end="   ")
    sublst+=[input("")]
    
    print("Enter first date (monday/tuesday) for Subject",x,"only:",end="   ")
    datelst+=[input("")]
    
    print("Enter time for Subject",x,end="   ")
    timelst+=[input("")]
    bold = workbook.add_format({'bold': True})

    worksheet.write(str(NumToAlph(letter))+str(letser-1),sublst[i],bold)
    if datelst[i]=="monday":
        worksheet.write(str(NumToAlph(letter))+str(letser),timelst[i])
        worksheet.write(str(NumToAlph(letter))+str(letser+2),timelst[i])
        worksheet.write(str(NumToAlph(letter))+str(letser+4),timelst[i])
    elif datelst[i]=="tuesday":
        worksheet.write(str(NumToAlph(letter))+str(letser+1),timelst[i])
        worksheet.write(str(NumToAlph(letter))+str(letser+3),timelst[i])
    x+=1
    letter+=1
worksheet.set_column(0,u,20)    

worksheet.write("A3","Monday",bold)
worksheet.write("A4","Tuesday",bold)
worksheet.write("A5","Wednesday",bold)
worksheet.write("A6","Thursday",bold)
worksheet.write("A7","Friday",bold)

workbook.close()