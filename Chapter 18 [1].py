import ezgmail,random
email=['niranjansreejayan@gmail.com','aryajith@gmail.com','sachinshreekumarquora@gmail.com']
chores=['Wash Clothes','Sweeping','Dishes']

variety_check={'niranjansreejayan@gmail.com':'Wash Clothes','aryajith@gmail.com':'Sweeping','sachinshreekumarquora@gmail.com':'Dishes'}

for i in range(len(email)):
    randomchore=random.choice(chores)
    chores.remove(randomchore)
    ezgmail.send(email[i],'This is to inform you about your chore',f'Your chore for the week is {randomchore}')
    variety_check.setdefault(email[i],randomchore)


