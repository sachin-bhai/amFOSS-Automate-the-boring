

file1 = open('Chapter 9/text.txt', 'r')

content = file1.read()
print(content)

list_strings = content.split()

for i in range(len(list_strings)):

    if "ADJECTIVE" in list_strings[i]:
        adj = input("Enter an adjective\n")
        list_strings[i] = list_strings[i].replace("ADJECTIVE", adj)
    
    elif "NOUN" in list_strings[i]:
        noun = input("Enter a noun\n")
        list_strings[i] = list_strings[i].replace("NOUN", noun)
    
    elif "VERB" in list_strings[i]:
        verb = input("Enter a verb\n")
        list_strings[i] = list_strings[i].replace("VERB", verb)


file2 = open('results.txt', 'w')
for i in list_strings:
    file2.write(i)
    file2.write(' ')
file2.close()
