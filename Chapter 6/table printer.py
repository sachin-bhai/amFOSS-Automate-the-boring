def printTable(table):
    E=0
    for i in table:
        for a in i:
            if len(a)>E:
                E=len(a)
    E+=2
    L=0
    F=len(table)
    for k in table:
        M=len(k)
        if M>L:
            L=M
    for i in range(L):
        for j in range(F):
            print(table[j][i]+(E-len(table[j][i]))*" ",end="")
        print("")


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


printTable(tableData)        