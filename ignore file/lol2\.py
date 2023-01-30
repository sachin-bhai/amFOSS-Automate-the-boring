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


sachin.shreekumar@gmail.com
The write() method takes a regular File object that has been opened in write-binary mode. You can get such a File object by calling Python’s open() function with two arguments: the string of what you want the PDF’s filename to be and 'wb' to indicate the file should be opened in write-binary mode.

If this sounds a little confusing, don’t worry—you’ll see how this works in the following code examples.

