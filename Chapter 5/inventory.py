# Practice Project - Fantasy Game Inventory


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(str(item), 0)
        inventory[item] += 1

    return inventory


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0

    for k, v in inventory.items():
        item_total += v
        print(str(v) + " " + str(k))

    print("Total number of items: " + str(item_total))


stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
displayInventory(stuff)

inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
