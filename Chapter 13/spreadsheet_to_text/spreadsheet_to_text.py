import openpyxl
from openpyxl.utils import get_column_letter



lists=['file.txt','file2.txt']
wb=openpyxl.load_workbook('Chapter 13/example.xlsx')

sheet=wb.active

r=sheet.max_row
c=sheet.max_column
text1=[]
text2=[]
texts=[text1,text2]
for i in range(1,c+1):
    for k in range(1,r+1):
        info=get_column_letter(i)+str(k)
        text=sheet[info].value
        texts[i-1].append(text)

for l in range(len(lists)):
    f= open(lists[l],"w")
    for i in texts:
        for k in i:
            f.write(str(k))
        f.close




