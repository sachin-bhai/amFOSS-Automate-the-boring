import openpyxl,sys
from openpyxl.styles import Font

if len(sys.argv)>1:
    val=int(sys.argv[1])
else:
    print('Try again')
    val=input("> ")

wb=openpyxl.Workbook()

wb.create_sheet(index=0,title='Multipilcation tables')
del wb['Sheet']
sheet=wb.active

fontObj1 = Font(name='Times New Roman', bold=True)

collumns=['A','B','C','D','E','F','G','H','I','J','K','L','M']
x=1
for i in range(2,int(val)+2):
    r1='A'+str(i)
    c1=collumns[i-1]+'1'
    sheet[r1].value=x
    sheet[c1].value=x
    sheet[r1].font=fontObj1
    sheet[c1].font=fontObj1
    x+=1
numberlist=[]
for a in range(1,int(val)+1):
    numberlist.append(a)
y=0
for m in range(2,int(val)+2):
    for k in range(2,int(val)+2):
        r2=collumns[m-1]+str(k)
        sheet[r2].value=numberlist[y]
        y+=1
    y=0
wb.save('hehe.xlsx')









