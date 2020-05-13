from myutils import *

students = []
student1 = create_student("TIMUR,26,3 4 5 3")
student2 = create_student("DIMUR,62,3 4 3 3")
students.append(student1)
students.append(student2)

def list_students():
    print_arr(students)

def add_student():
    name = input("ENTER NAME: ")
    age = input("ENTER AGE: ")
    marks = input("ENTER MARKS: ")
    line = f"{name},{age},{marks}"
    new_student = create_student(data)
    students.append(new_student)

def delete_student():
    print_arr(students)
    line = input("ENTER STUDENT NAME: ")
    del_index = -1

    for i in range(len(students)):
        if students[i]["name"] == line:
            del_index = i

    if del_index == -1:
        print("STUDENT NOT FOUND")
    else:
        students.pop(del_index)

def update_student():
    print_arr(students)
    line = input("ENTER STUDENT NAME: ")
    upd_index = -1

    for i in range(len(students)):
        if students[i]["name"] == line:
            upd_index = i

    if upd_index == -1:
        print("STUDENT NOT FOUND")
    else:
        print("ENTER NEW DATA")
        name = input("ENTER NAME: ")
        age = int(input("ENTER AGE: "))
        marks = list(map(int, input("ENTER MARKS: ").split()))
        students[upd_index] = {
            "name": name,
            "age": age,
            "marks": marks
        }

def main():
    print("[1] LIST STUDENTS")
    print("[2] ADD STUDENTS")
    print("[3] DELETE STUDENT")
    print("[4] UPDATE STUDENT")
    print("[5] EXIT")
    num = input()
    if num == "1":
        list_students()
    elif num == "2":
        add_student()
    elif num == "3":
        delete_student()
    else:
        exit()

main()