"""
This File asks user for two input words and prints them in 
alphabetical order without the use of sort function
"""

def random(asd):
    asd=asd.lower()
    
    return 27-(ord(asd)-96)

def alphabets(a,b):
    x=len(a)
    y=len(b)
    for i in range(min(x,y)):
        if random(a[i])>random(b[i]):
            print(a)
            print(b)
            break
        elif random(a[i])<random(b[i]):
            print(b)
            print(a)
            break
        else:
            if i==min(x,y)-1:
                print(a)
                print(b)
            
            continue




x=input("Enter a word: ")
y=input("Enter a word: ")
alphabets(x,y)
