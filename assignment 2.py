import random



lst=[]
for i in range(5):
   lst.append(random.randint(1,6))



sum1=lst.count(1)
sum1s=1*sum1
sum2=lst.count(2)
sum2s=2*sum2
sum3=lst.count(3)
sum3s=3*sum3
sum4=lst.count(4)
sum4s=4*sum4
sum5=lst.count(5)
sum5s=5*sum5
sum6=lst.count(6)
sum6s=6*sum6
threeofkind=0
SameThree=0
if sum1== 3 or sum2==3 or sum3==3 or sum4==3 or sum5==3 or sum6==3:
    SameThree=1
    for i in lst:
        threeofkind+=i
fourofkind=0
if sum1== 4 or sum2==4 or sum3==4 or sum4==4 or sum5==4 or sum6==4:
    fourofkind=10
    for i in lst:
        fourofkind+=i
fiveofkind=0
SameTwo=0
if sum1== 5 or sum2==5 or sum3==5 or sum4==5 or sum5==5 or sum6==5:
    fiveofkind=50
    for i in lst:
        fiveofkind+=i

if sum1== 2 or sum2==2 or sum3==2 or sum4==2 or sum5==2 or sum6==2:
    SameTwo=1
FullHouse=0
if SameThree==1 and SameTwo==1:
    FullHouse=25
    for i in lst:
        FullHouse+=i

if sum1s==max(sum1s,sum2s,sum3s,sum4s,sum5s,sum6s,threeofkind,fourofkind,fiveofkind,FullHouse):
    print(lst,"Best is sum1's with a score of",sum1s)
elif sum2s==max(sum2s,sum1s,sum3s,sum4s,sum5s,sum6s,threeofkind,fourofkind,fiveofkind,FullHouse):
    print(lst,"Best is sum2's with a score of",sum2s)
elif sum3s==max(sum3s,sum2s,sum1s,sum4s,sum5s,sum6s,threeofkind,fourofkind,fiveofkind,FullHouse):
    print(lst,"Best is sum3's with a score of",sum3s)
elif sum4s==max(sum4s,sum2s,sum3s,sum1s,sum5s,sum6s,threeofkind,fourofkind,fiveofkind,FullHouse):
    print(lst,"Best is sum4's with a score of",sum4s)
elif sum5s==max(sum5s,sum2s,sum3s,sum4s,sum1s,sum6s,threeofkind,fourofkind,fiveofkind,FullHouse):
    print(lst,"Best is sum5's with a score of",sum5s)
elif sum6s==max(sum6s,sum2s,sum3s,sum4s,sum5s,sum1s,threeofkind,fourofkind,fiveofkind,FullHouse):
    print(lst,"Best is sum6's with a score of",sum6s)
elif threeofkind==max(sum1s,sum2s,sum3s,sum4s,sum5s,sum6s,threeofkind,fourofkind,fiveofkind,FullHouse):
    print(lst,"Best is three of kind with a score of",threeofkind)
elif fourofkind==max(sum1s,sum2s,sum3s,sum4s,sum5s,sum6s,threeofkind,fourofkind,fiveofkind,FullHouse):
    print(lst,"Best is four of kind with a score of",fourofkind)
elif fiveofkind==max(sum1s,sum2s,sum3s,sum4s,sum5s,sum6s,threeofkind,fourofkind,fiveofkind,FullHouse):
    print(lst,"Best is five of kind with a score of",fiveofkind)
elif FullHouse==max(fourofkind,sum2s,sum3s,sum4s,sum5s,sum6s,threeofkind,fourofkind,fiveofkind,FullHouse):
    print(lst,"Best is Full House with a score of",FullHouse)


