def collatz(number):
        number=int(number)
        if number%2==0:
            return number//2
        else:
            return 3*number+1
    
try:
    l=input("Enter a number ")
    while l!=1:
        l=collatz(l)
        print(l)
except ValueError:
    print("\n\nEnter an integer\n\n")




