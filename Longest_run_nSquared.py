"""
This one finds the longest run in a time complexity of O(n^2)
For some reason i built two of these but you are welcome to check both
"""


def longest_run(lst):
    same=[]
    same2=[]
    discard=[]
    i=0
    x=2
    u=0
    while i<len(lst):
        while x==2:
        
            if lst[i]==lst[i+1]:
                same=same+[lst[i]]
                i=i+1
            elif lst[i]==lst[i-1]:
                same=same+[lst[i]]
                i=i+1
            if lst[i]!=lst[i-1]:
                x=x+1
        if lst[i]!=lst[i-1]:
            same2=same2+[lst[i]]
            i=i+1
        elif lst[i]==lst[i+1]:
            same2=same2+[lst[i]]
            i=i+1
        elif lst[i] in same2:
            i=i+1
            
                
        elif lst[i] not in same2:
            if len(same)>len(same2):
                same2=[]
            else:
                same=[]
            i=i+1
        

    return same
lst=[1,1,1,1,2,2,2,3,3,4]
print(longest_run(lst))
        
            
            
