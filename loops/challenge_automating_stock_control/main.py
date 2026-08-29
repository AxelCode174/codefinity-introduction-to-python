# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

for item in inventory:
    current_stock, minimum_stock, restock_quantity, on_sale = inventory[item]
    while current_stock < minimum_stock:
        current_stock += restock_quantity
        inventory[item][0] = current_stock
    if current_stock > discount_threshold and not on_sale:
        inventory[item][3] = True
        



    
