import numpy as np

student_scores = np.array([
    [80, 75, 90, 85],
    [70, 85, 80, 75],
    [90, 80, 85, 90],
    [85, 90, 95, 80]
])

subjects = ["Math", "Science", "English", "History"]

# Calculate average of each subject
averages = np.mean(student_scores, axis=0)

# Display averages
for i in range(4):
    print(subjects[i], "Average =", averages[i])

# Find subject with highest average
highest_index = np.argmax(averages)

print("\nSubject with highest average:", subjects[highest_index])
print("Highest average score:", averages[highest_index])
