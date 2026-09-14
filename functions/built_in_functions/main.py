# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}

total_sales_list = []
for item in products:
    price, quantity = products[item]
    price_converted = float(price)
    products[item][0] = price_converted
    quantity_converted = int(quantity)
    products[item][1] = quantity_converted
    total_sales = price_converted * quantity_converted
    print(f"Total sales for {item}: ${total_sales}")
    total_sales_list.append(total_sales)
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
print(f"Total sum of all sales: ${total_sum} \nMinimum sales: ${min_sales} \nMaximum sales: ${max_sales}")
