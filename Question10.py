import numpy as np
# Generate marks for 10 students and 5 subjects
marks = np.random.randint(30, 101, (10,5))
print("Student Marks:")
print(marks)
# Total marks of each student
total = marks.sum(axis=1)
print("Total Marks:")
print(total)
# Average marks of each student
average = marks.mean(axis=1)
print("Average Marks:")
print(average)
# Student with highest total
highest = np.argmax(total)
print("Highest Total Student:", highest)
print("Total:", total[highest])
# Student with lowest total
lowest = np.argmin(total)
print("Lowest Total Student:", lowest)
print("Total:", total[lowest])
# Overall class statistics
print("Class Mean:", marks.mean())
print("Class Standard Deviation:", marks.std())
# Find top 3 students
top3 = np.argsort(total)[-3:]
print("Top 3 Student Indexes:")
print(top3)
# Display marks of top 3 students
print("Marks of Top 3 Students:")
print(marks[top3])