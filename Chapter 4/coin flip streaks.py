import random
n=0
toss=[]
for i in range(10000):
    m=random.randint(0,1)
    if i<=100:
        toss.append(m)
    if i>100:
        toss.append(m)

L=len(toss)
for j in range(L-5):
    if toss[j]==toss[j+1]==toss[j+2]==toss[j+3]==toss[j+4]==toss[j+5]:
        n=n+1
print("The percentage of streaks is",n/100,"%.")

