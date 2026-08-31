# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
} 
restock_threshold = 30
discount_stock = 100
for item in inventory:
    current_stock, regular_price, discounted_price = inventory[item]
    if current_stock <  restock_threshold:
        print(f"{item} need restocking.")
    elif current_stock > discount_stock:
        print(f"{item} should be sold at the discounted price of {discounted_price}.")
    if current_stock > restock_threshold and current_stock < discount_stock:
        print(f"{item} should be sold at the regular price of {regular_price}.")
        
 