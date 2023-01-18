import re

def stripre(text):
    met=re.compile(r'[(\w)*]')
    mo=met.findall(text)
    print(mo)
    text=''
    for i in mo:
        text=text+i
    print(text)


lol=input("> ")
stripre(lol)