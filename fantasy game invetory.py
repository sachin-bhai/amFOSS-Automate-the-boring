def displayInventory(inventory):
    s=0
    print("Invetory:")
    for i in inventory.keys():
        print(inventory[i],i)
    for j in inventory.values():
        s=s+j
    print("Total number of items:",s)
    

invt={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# Edit the above list
displayInventory(invt)
