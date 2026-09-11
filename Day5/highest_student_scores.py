student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
highest_score = 0
for score in student_scores:
    if highest_score > score:
        highest_score = highest_score
    else:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")