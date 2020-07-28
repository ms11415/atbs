# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItem):
    for item in addedItem:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory


print('---Displaying STUFF')
displayInventory(stuff)
inv = {'gold coin': 42, 'rope': 1}
print('---Displaying INV')
displayInventory(inv)
print('---Adding dragonLoot to INV and displaying updated INV')
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)