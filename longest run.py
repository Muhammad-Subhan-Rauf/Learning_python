"""
This file prints the longest repeated number in a list of numbers.
"""

def run(lost):
    last_seen=lost[0]
    lst=[]
    fnlst=[]
    for i in lost:
        if i==last_seen:
            lst+=[i]
            
        else:
            if len(lst)>len(fnlst):
                fnlst=lst.copy()
                lst=[i]
            elif len(lst)==len(fnlst):
                fnlst=lst.copy()
                lst=[i]
            else:
                lst=[i]
        
        last_seen=i
    if len(lst)>len(fnlst):
        fnlst=lst.copy()
    print(fnlst)
run([1,2,2,3,3,3,3,4,4,4])
