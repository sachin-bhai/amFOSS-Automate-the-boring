#! python3
# mcb.py - A multi-clipboard program.

import pyperclip, sys, shelve

mcbShelf = shelve.open('mcb')


if len(sys.argv) == 3 and sys.argv[1].lower() == 'save': # checking if there are three arguments and if its present take the second index element and make it lower and check if its equal to save
    mcbShelf[sys.argv[2]] = pyperclip.paste() #if true paste it
    print("done")


elif len(sys.argv) == 2: #if there are only two arguments
    
    
    if sys.argv[1].lower() == 'list': #if there are only two arguments take the second index element and make it lower and check if its equal to list 
        pyperclip.copy(str(list(mcbShelf.keys()))) # if true copy all the keys from mcshelve and make it a list and make that element a string
        print("listed")
    
    elif sys.argv[1] in mcbShelf: # if the second index argument is not equal to list 
        pyperclip.copy(mcbShelf[sys.argv[1]])

    if sys.argv[1].lower() == 'delete':
        pyperclip.copy('')
        print('deleted')
mcbShelf.close()


sachin.shreekumar@gmail.com If you recieve this in your mail, your bot is a success.