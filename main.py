from myutils import *

students = []

n = int(input("ENTER NUMBER OF STUDENTS: "))
for i in range(n):
    line_input = input("ENTER STUDENT DATA: ")
    new_student = create_student(line_input)
    students.append(new_student)

print(students)