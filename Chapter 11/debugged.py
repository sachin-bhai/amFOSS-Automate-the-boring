import random
for i in range(2):
    print('Guess the coin toss! Enter heads or tails:')
    guess=input("> ")
    if guess=='tails':
        guess=0
    else:
        guess=1
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    if toss == guess:
        print('You got it!')
        break
    else:
        
        if i==1:
            print('You"re really bad at this game')
        else:
            print('Nope! Guess again!')
            