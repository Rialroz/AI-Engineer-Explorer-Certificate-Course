student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eve": 95,
    "Frank": 82,
    "Grace": 90,
    "Hannah": 76,}

# Print the original dictionary
print("Original student grades:")
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

# Calculate the average grade
average_grade = sum(student_grades.values()) / len(student_grades)
print(f"\nAverage grade: {average_grade}")



