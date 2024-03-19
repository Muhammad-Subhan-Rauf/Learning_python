"""
This is a timetable creator specific to my university. Might make a universal one later.
"""

import xlsxwriter
workbook=xlsxwriter.Workbook("write.xlsx")
worksheet=workbook.add_worksheet()
subject1=input("Enter subject 1:    ")
print("Enter date for",subject1,":\t",end="")
date1=input("").lower()
print("Enter Time for",subject1,":\t",end="")
time1=input("")
if date1=="monday":
    worksheet.write("B3",time1)
    worksheet.write("B5",time1)
    worksheet.write("B7",time1)
elif date1=="tuesday":
    worksheet.write("B4",time1)
    worksheet.write("B6",time1)

    


subject2=input("Enter subject 2:    ")
print("Enter date for",subject2,":\t",end="")
date2=input("").lower()
print("Enter Time for",subject2,":\t",end="")
time2=input("")
if date2=="monday":
    worksheet.write("C3",time2)
    worksheet.write("C5",time2)
    worksheet.write("C7",time2)
elif date2=="tuesday":
    worksheet.write("C4",time2)
    worksheet.write("C6",time2)



subject3=input("Enter subject 3:    ")
print("Enter date for",subject3,":\t",end="")
date3=input("").lower()
print("Enter Time for",subject3,":\t",end="")
time3=input("")
if date3=="monday":
    worksheet.write("D3",time1)
    worksheet.write("D5",time1)
    worksheet.write("D7",time1)
elif date3=="tuesday":
    worksheet.write("D4",time1)
    worksheet.write("D6",time1)




subject4=input("Enter subject 4:    ")
print("Enter date for",subject1,":\t",end="")
date1=input("").lower()
print("Enter Time for",subject1,":\t",end="")
time1=input("")
if date1=="monday":
    worksheet.write("B3",time1)
    worksheet.write("B5",time1)
    worksheet.write("B7",time1)
elif date1=="tuesday":
    worksheet.write("B4",time1)
    worksheet.write("B6",time1)



    
subject5=input("Enter subject 5:    ")


worksheet.write("A3","Monday")
worksheet.write("A4","Tuesday")
worksheet.write("A5","Wednesday")
worksheet.write("A6","Thursday")
worksheet.write("A7","Friday")
worksheet.write("B2",subject1)
worksheet.write("C2",subject2)
worksheet.write("D2",subject3)
worksheet.write("E2",subject4)
worksheet.write("F2",subject5)
workbook.close()



