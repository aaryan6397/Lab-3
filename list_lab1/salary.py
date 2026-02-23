# ---------------------------------------------------------
# File: salary.py
# Program: Salary Processing System
# ---------------------------------------------------------

salaries = [25000, 60000, 45000, 80000, 15000]

minimum_wage = 20000

# Remove salaries below minimum wage
salaries = [s for s in salaries if s >= minimum_wage]

# Add 5% bonus for salary > 50000
for i in range(len(salaries)):
    if salaries[i] > 50000:
        salaries[i] *= 1.05

# Sort descending
salaries.sort(reverse=True)

print("Top 3 Salaries:", salaries[:3])


'''output:  
Top 3 Salaries: [84000.0, 47250.0, 25000]
'''