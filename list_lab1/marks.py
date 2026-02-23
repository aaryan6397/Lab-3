# ---------------------------------------------------------
# File: marks.py
# Program: Student Marks Analyzer
# ---------------------------------------------------------

# Given list of marks
marks = [95, 88, 102, -5, 76, 89, 95]

# Remove invalid marks (0-100 allowed)
marks = [m for m in marks if 0 <= m <= 100]

# Calculate average
average = sum(marks) / len(marks)

# Find topper(s)
top_score = max(marks)
toppers = [m for m in marks if m == top_score]

# Assign grade based on average
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "D"

print("Valid Marks:", marks)
print("Average:", average)
print("Topper Marks:", toppers)
print("Grade:", grade)