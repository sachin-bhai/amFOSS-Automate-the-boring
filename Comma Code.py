def comma(hah):
    L=len(hah)
    for i in range(L-2):
        print(hah[i],",",end="")
        
    print(hah[-2],"and",hah[-1])


lst=list(input("> ").split())
comma(lst)