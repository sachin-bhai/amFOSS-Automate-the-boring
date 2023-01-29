import PyPDF2

password = open('Chapter 15/dictionary.txt')
password = password.read()
password=password.split('\n') # new line split

pdf = open('Chapter 15/encrypted.pdf', 'rb')
pdfread = PyPDF2.PdfFileReader(pdf)
n=0
for i in password:
    crack_low=pdfread.decrypt(i.lower())
    crack_high=pdfread.decrypt(i.upper())

    if crack_low==1 or crack_high==1:
        print(f'The password is {i}')
        n+=1
        break

if n==0:
    print('Could not find the password')      

    

    
