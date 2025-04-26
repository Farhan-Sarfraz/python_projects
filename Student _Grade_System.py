students = {}

def add_student(name,marks):
    students[name] = marks

def search_student(name):
    return students.get(name,None)

def delete_students(name):
    if name in students:
        del students[name]

def calc_avg(marks):
    return sum(marks)/len(marks)

def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def display_student(name):
    marks = search_student(name)
    if marks is None:
        print("Student not found : ")
        return
    
    avg = calc_avg(marks)
    grade = get_grade(avg)

    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")

def show_all_students():
    if not students:
        print("No students record : ")
        return
    
    for name in students:
        display_student(name)
        print("-" * 20)

def main ():
    while True:
        print("\nStudents Grade Management System. ")
        print("1. Add Student : ")
        print("2. Search student : ")
        print("3. Delete student : ")
        print("4. Display student : ")
        print("5. Show all student : ")
        print("6. Exit : ")

        choice = input("Enter choice : ")

        if choice == '1':
            name = input("Enter the student name : ").strip()
            marks = list(map(int,input("Enter marks seprated by the space : " ).split()))
            add_student(name,marks)
        
        elif choice == '2':
            name = input("Enter name to search : ").strip()
            if search_student(name) is not None:
                print("Students found. ")
            else:
                print("Not found. ")

        elif choice == '3':
            name = input("Enter name for delete : ").strip()
            delete_students(name)

        elif choice == '4':
            name = input("Enter the name for data display : ").strip()
            display_student(name)
        
        elif choice == '5':
            show_all_students()
        
        elif choice == '6':
            break

        else:
            print("Invalid choice. ")

if __name__  == "__main__":
    main()

        

