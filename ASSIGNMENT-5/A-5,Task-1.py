# Task 1: Create a Dictionary of Student Marks

# Creating a dictionary of students and their marks
student_marks = {
    "Aman": 85,
    "Suhani": 92,
    "Riya": 78,
    "Karan": 88,
    "Meera": 90
}

# Asking user for student name
name = input("Enter the student's name: ")

# Checking and displaying marks
if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print("Student not found in the record.")
