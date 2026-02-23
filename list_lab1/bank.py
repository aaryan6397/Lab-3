# ---------------------------------------------------------
# File: bank.py
# Program: Bank Transaction Analyzer
# ---------------------------------------------------------

transactions = [20000, -5000, 15000, -2000, 8000]

# Total balance
balance = sum(transactions)

# Largest withdrawal
withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals) if withdrawals else 0

# Deposits > 10000
big_deposits = len([t for t in transactions if t > 10000])

print("Total Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > 10000:", big_deposits)

'''output:
Total Balance: 36000
Largest Withdrawal: -5000
Deposits > 10000: 2