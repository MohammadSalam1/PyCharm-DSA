students = {}

def add_student(name, age):
    students[name] = {"age": age, "grades": {}}

def add_grade(name, subject, grade):
    if name in students:
        students[name]["grades"][subject] = grade
    else:
        print("Student not found!")

def delete_student(name):
    if name in students:
        del students[name]
    else:
        print("Student not found!")

def view_all():
    for name, info in students.items():
        print(f"{name} is ({info['age']} years): {info['grades']}")

def top_student():
    top_name = None
    top_avg = 0
    for name, info in students.items():
        grades = info["grades"].values()
        if grades:
            avg = sum(grades)/len(grades)
            if avg > top_avg:
                top_avg = avg
                top_name = name
    print(f"Top student: {top_name}, ({top_avg: 0.1f})")

if __name__ == '__main__':
    add_student("Alice", 17)
    add_student("Bob", 18)
    add_grade("Alice", "Math", 90)
    add_grade("Alice", "CS", 95)
    add_grade("Bob", "Math", 75)
    add_grade("Bob", "CS", 88)

    view_all()
    top_student()
