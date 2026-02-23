# ---------------------------------------------------------
# File: cart.py
# Program: E-Commerce Cart System
# ---------------------------------------------------------

cart = [1200, 1500, 1200, 3000, 800]

# Remove duplicate prices
cart = list(set(cart))

total = sum(cart)

# Apply 10% discount if total > 5000
if total > 5000:
    total *= 0.90

# Add GST 18%
total *= 1.18

print("Final Payable Amount:", total)