import shelve, pyperclip, sys
mcb = shelve.open('mcb')



if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb[sys.argv[2]] = pyperclip.paste()


elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    pyperclip.copy("")
    try:
        del mcb[sys.argv[2]]
    except:
        print('Invalid')


elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'delete':
        pyperclip.copy("")
        mcb.clear()

    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb.keys())))

    elif sys.argv[1] in mcb:
        pyperclip.copy(mcb[sys.argv[1]])


mcb.close()