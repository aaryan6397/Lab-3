# ---------------------------------------------------------
# File: exam.py
# Program: Online Exam Result Processor
# ---------------------------------------------------------

scores = [25, 30, 35, 40, 50, 60, 20]

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

# Add grace marks (5) to scores between 30–35
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Count passed students (>=40)
passed = len([s for s in scores if s >= 40])

print("Updated Scores:", scores)
print("Students Passed:", passed)

'''output:
Updated Scores: [35, 40, 45, 50, 60]
Students Passed: 4