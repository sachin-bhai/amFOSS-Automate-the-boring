import pyperclip

text = pyperclip.paste()

points=text.split("\n")
print(type(points))
for i in range(len(points)):
    points[i] = "* " + points[i]

text='\n'.join(points)

pyperclip.copy(text)
print("Done")