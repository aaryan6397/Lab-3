# ---------------------------------------------------------
# File: temp.py
# Program: Temperature Monitoring System
# ---------------------------------------------------------

temps = [35, 42, 46, 39, 41, 48, 30]

# Hottest & Coldest
print("Hottest:", max(temps))
print("Coldest:", min(temps))

# Replace temp >45 with "Heat Alert"
for i in range(len(temps)):
    if temps[i] > 45:
        temps[i] = "Heat Alert"

# Count extreme days (>40)
extreme_days = len([t for t in temps if t != "Heat Alert" and t > 40])

print("Updated Temps:", temps)
print("Extreme Days:", extreme_days)

'''output:
Hottest: 48
Coldest: 30
Updated Temps: [35, 42, 'Heat Alert', 39, 41, 'Heat Alert', 30]
Extreme Days: 2
