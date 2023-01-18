import time
questions=[
    '0X0','1X1','2X2','3X3','4X4',
    '5X5','6X6','7X7','8X8','9X9'
]
answers=[0,1,4,9,16,25,36,49,64,81]
tries=3
q=0

while q!=9:
    t0=time.time()
    print("\n",questions[q],"\n")
    user_ans=input(">")
    t1=time.time()-t0
    if tries==0:
        q=q+1
        tries=3
    if t1>8:
        print("Time has run out!")
        break
    
    if int(user_ans)==answers[q]:
        print("Correct")
        time.sleep(1)
        q+=1
        tries=3
    else:
        print("Nope, try again\n")
        tries-=1
