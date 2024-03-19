"""
This file will calculate your GPA for the semester
"""
def gradeconvert(L):
    if L=="A" or L=="A+" or L=="a" or L=="a+":
        return 4.0
    elif L=="A-" or L=="a-":
        return 3.7
    elif L=="B+" or L=="b+":
        return 3.3
    elif L=="B" or L=="b":
        return 3.0
    elif L=="B-" or L=="b-":
        return 2.7
    elif L=="C+" or L=="c+":
        return 2.3
    elif L=="C" or L=="c":
        return 2.0
    elif L=="C-" or L=="c-":
        return 1.7
    elif L=="D+" or L=="d+":
        return 1.3
    elif L=="D" or L=="d":
        return 1.0
    elif L=="F" or L=="f":
        return 0.0
    else:
        print("Invalid Grade given")
    

    
def calculator():
    subs=int(input("how many subjects do you have= "))
    lst=[]
    gradelst=[]
    credlst=[]
    numblst=[]
    final=[]
    g=0
    hi=0
    som=0
    sumcred=0
    sumres=[]
    for i in range(1,subs+1):
        print("Enter subject Name",i,"= ",end="")
        x=input("")
        lst=lst+[x]
    for z in lst:
        print("Enter Grade for",z,"=  ",end="")
        x1=input("")
        gradelst=gradelst+[x1]
    for u in lst:
        print("Enter Credit hours for",u,"= ",end="")
        x2=float(input(""))
        credlst=credlst+[x2]
    for q in gradelst:
        numblst=numblst+[gradeconvert(q)]



    while som<len(credlst):
        sumcred=sumcred+(credlst[som])
        som=som+1
    while hi<len(gradelst):
        sumres=sumres+[numblst[hi]*credlst[hi]]
        hi=hi+1
    lastres=0
    for S in sumres:
        lastres=lastres+S
    res=lastres/sumcred
    print("Your CGPA is ",res)    
        
    input("Press enter to continue") 


calculator()




















