# Dictionary for a grocery store inventory
inventory = {
    "Apples": 30,
    "Oranges": 18,
    "Bananas": 45
}

# Get the count of Oranges
print("Count of Oranges:", inventory.get("Oranges"))

# Update inventory by adding a new item
inventory.update({"Mangoes": 20})
inventory.update({"Bananas": 30})
print("Updated Inventory:", inventory)

# You can also add a new item to the end of the dictionary like this
inventory["Pineapples"] = 15
print("Updated Inventory:", inventory)

# Remove Bananas from the inventory
removed_item = inventory.pop("Bananas")
print("Removed Item:", removed_item)
print("Current Inventory:", inventory)