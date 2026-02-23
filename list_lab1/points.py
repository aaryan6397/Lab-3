# ---------------------------------------------------------
# File: points.py
# Program: Sports Tournament Points Table
# ---------------------------------------------------------

points = [10, -5, 25, 18, 30]

# Replace negative points with 0
points = [p if p >= 0 else 0 for p in points]

# Sort leaderboard descending
points.sort(reverse=True)

# Winner & runner-up
winner = points[0]
runner_up = points[1]

print("Leaderboard:", points)
print("Winner Points:", winner)
print("Runner-up Points:", runner_up)


'''output:
Leaderboard: [30, 25, 18, 10, 0]
Winner Points: 30
Runner-up Points: 25