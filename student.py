student = []

def create_student():
    n = int(input("How many students? "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        age = int(input(f"Enter age of student {i+1}: "))
        student.append({
            "id": str(len(student) + 1),
            "name": name,
            "age": age
        })
    print("Students added successfully!\n")

def read_students():
    if not student:
        print("No student records found.\n")
        return
    for s in student:
        for key, value in s.items():
            print(key, ":", value)
        print()

def update_student():
    uid = input("Enter student ID to update: ")
    found = False
    for s in student:
        if s["id"] == uid:
            s["name"] = input("Enter new name: ")
            s["age"] = int(input("Enter new age: "))
            print("Student updated successfully!\n")
            found = True
            break
    if not found:
        print("Student ID not found.\n")

def delete_student():
    uid = input("Enter student ID to delete: ")
    global student
    original_len = len(student)
    student = [s for s in student if s["id"] != uid]
    if len(student) < original_len:
        print("Student deleted successfully!\n")
    else:
        print("Student ID not found.\n")


while True:
    print("🔹 Student CRUD Menu")
    print("1. Create Student")
    print("2. Read All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        create_student()
    elif choice == '2':
        read_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, please select 1–5.\n")