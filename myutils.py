def create_student(line):
    parts = line.split(",")
    name = parts[0]
    age = int(parts[1])
    marks = list(map(int, parts[2].split()))
    new_student = {
        "name": name,
        "age": age,
        "marks": marks
    }
    return new_student

def print_arr(arr):
    for i in arr:
        print(i)