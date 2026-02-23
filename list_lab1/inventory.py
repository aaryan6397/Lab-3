# ---------------------------------------------------------
# File: inventory.py
# Program: Inventory Management
# ---------------------------------------------------------

stock = [0, 5, 20, 8, 50, 0]

# Remove items with 0 stock
stock = [s for s in stock if s > 0]

# Restock items below 10
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

# Total inventory
total_stock = sum(stock)

print("Updated Stock:", stock)
print("Total Inventory:", total_stock)


'''output:
Updated Stock: [55, 25, 58, 50]
Total Inventory: 188