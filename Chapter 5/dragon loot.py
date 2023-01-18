def displayInventory(inventory,extra):
    for k in extra:
        if k in inventory.keys():
            inventory[k]=inventory[k]+1
    s=0
    print("Invetory:")
    for i in inventory.keys():
        print(inventory[i],i)
    for j in inventory.values():
        s=s+j
    print("Total number of items:",s)
    

invt={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
add=['gold coin', 'dagger', 'gold coin', 'gold coin','torch']
# Edit the above lists
displayInventory(invt,add)