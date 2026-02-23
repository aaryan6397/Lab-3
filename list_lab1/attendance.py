# ---------------------------------------------------------
# File: attendance.py
# Program: Attendance Tracker
# ---------------------------------------------------------

attendance = [1,1,0,0,1,0,1,1,0,0]

# Calculate attendance percentage
percentage = (sum(attendance) / len(attendance)) * 100

# Identify below 75%
if percentage < 75:
    print("Attendance below 75%")

# Replace consecutive absences with warning flag (-1)
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = -1
        attendance[i+1] = -1

print("Updated Attendance:", attendance)
print("Attendance %:", percentage)


'''output:
Updated Attendance: [1, 1, -1, -1, 1, 0, 1, 1, 0, 0]
Attendance %: 50.0
Attendance below 75%