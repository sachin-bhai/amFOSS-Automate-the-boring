import pyinputplus as pyip

print("What kind of sandwich do you want?")
breadtype=pyip.inputMenu(['wheat','white','sourdough'])

print("\nWhat kind of protien do you want?")
proteintype=pyip.inputMenu(['chicken','turkey','ham','tofu'])

print("\nDo you need cheese?")
cheese=pyip.inputYesNo()
print(cheese)
if cheese.lower()=='yes':
        print("\nWhaa kind of cheese?")
        cheese=pyip.inputMenu(['Cheddar','Swiss','Mozzarella'])

print("\nDo you want mayo,mustard,lettuce or tomato?")
mayo=pyip.inputYesNo()
if mayo=='yes':
    print("\nWhich?")
    mayo=pyip.inputChoice(["mayo","mustard","lettuce","tomato"])

print("\nHow many sandwiches do you need?")
number=pyip.inputInt(min=1)

prices={'white':10,'wheat':20,'sourdough':30,
        'chicken':50,'turkey':60,'ham':40,'tofu':30,
        'yes':20,'mayo':10,'mustard':10,"lettuce":10,
        'tomato':15,'no':0,'Cheddar':15,'Mozarella':20,'Swiss':30}
        


cost=prices[breadtype]+prices[proteintype]+prices[cheese]+prices[mayo]
cost=cost*number
print(f'\nThe total cost is {cost}.')