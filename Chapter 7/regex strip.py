import re

def stripre(text):
    met=re.compile(r'[(\w)*]')
    mo=met.findall(text)
    text=''
    for i in mo:
        text=text+i
    print(text)


lol=input("> ")
stripre(lol)