# ---------------------------------------------------------
# File: rating.py
# Program: Movie Rating System
# ---------------------------------------------------------

ratings = [5, 4, 3, 6, 2, 5, -1]

# Remove invalid ratings (1-5)
ratings = [r for r in ratings if 1 <= r <= 5]

# Average rating
average = sum(ratings) / len(ratings)

# Count 5-star ratings
five_star = ratings.count(5)

# Sort ascending
ratings.sort()

print("Ratings:", ratings)
print("Average:", average)
print("5-Star Count:", five_star)


'''output:
Ratings: [2, 3, 4, 5, 5]
Average: 3.8
5-Star Count: 2