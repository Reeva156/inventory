
student = []
   
def creat():
        r =int(input("How many students you want:"))
        for p in range(r):
            name = input(f"\nName {p+1}: ")
            age = int(input(f"\nAge {p+1}: "))
            grade = str(input(f"\nGrade {p+1}: "))
            Birth = str(input(f"\nDate of Birth (YYYY-MM-DD)  {p+1}: "))
            subject = str(input(f"\nSubjects (comma-separated) {p+1}: "))
        student.append({
           "id": str(len(student)+1),
           "name": name,
           "age": age,
           "grade": grade,
           "Birth": Birth,
           "subject": subject,
        })
        print("\nStudents added successfully!\n")

def read(): 
    if not student:
        print("\nNo student records found.\n")
        return
    for s in student:
        for key, value in s.items():
            print(key, ":", value)
        print()
    
def update():
    id=input("\nEnter student Id to update")
    found = False
    for s in student:
        if s["id"] == id:
            s["name"] = input("Enter new name: ")
            s["age"] = input("Enter new age: ")
            s["grade"] = input("Enter new grade:")
            s["Birth"] = input("Enter new Birth Date:")
            s["subject"] = input("Enter new subject:")
            print("\nStudent updated successfully!\n")
            found = True
            break
        if not found:
            print("\nStudent ID not found.\n")


def delete():
    id = input("\nEnter Student ID to remove")
    global student
    real = len(student)
    student = [s for s in student if s["id"] != id]
    if len(student) < real:
        print("\nStudent Removed Successfully!!")
    else:
        print("\nStudent ID is not available")

while True:
    print("\nWelcome to the Student Data Organizer");


    print("\nSelect an Option")
    print("1. Add Students")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Exits")
    option = input("Enter Your Choice:")
    
    if option == '1':
        creat()
    elif option == '2':
        read()
    elif option == '3':
        update()
    elif option == '4':
        delete()
    elif option =='6':
         print("----Exited------Goodbyee-----")
    else:
        print("Your Choice is not available")

    


