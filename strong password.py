import re
def password(enter):
    list=[]
    low=re.compile(r'[a-z]')
    up=re.compile(r'[A-Z]')
    num=re.compile(r'\d')
    n=len(enter)
    if n>=7:
        if low.search(enter)==True:
            if up.search(enter)==True:
                if num.search(enter)==True:
                    print("valid")
                else:
                    print("invalid")
            else:
                print("invalid")
        else:
            print("invalid")
    else:
        print("invalid")   
pas=input("> ")
password(pas)