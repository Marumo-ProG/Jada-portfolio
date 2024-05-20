'''
    this project is meant to demonstrate the use of loops and functions
    by solving the problem of repetition in school
    that the teachers had at Longevity school with printing sheets for the kids
'''

def get_student_info():
    name = input("Name of Student:")
    course = input("Course of Student:")
    grade = input("Student Grade:")
    print("======School Name=============")
    print("Name:", name)
    print("Course:", course)
    print("Grade:", grade)
    print("===============================")

number_students = int(input("Number of students:"))


for i in range(number_students):
    get_student_info()
