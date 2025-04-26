students = []

def add_student():
    name = input("Enter the name : ")
    roll_no = input("Enter roll number : ")
    subjects = input("Enter subjects (comma seprated) : ").split(',')
    std_class = input("Enter the class :")
    marks = list(map(int,input("Enter marks (space seprated) : ").split()))

    subj_marks = dict(zip(subjects, marks))

    student = {
        'name' : name,
        'roll_no' : roll_no,
        'class' : std_class,
        'subjects' : subj_marks,

    }

    students.append(student)
    print("Student add successfully. ")
def search_student():
    roll_no = input("Enter the roll_no for search : ")
    for student in students:
        if student['roll_no'] == roll_no:
            display_student(student)
            return
    print("Student not found. ")
def delete_student():
    roll_no = input("Enter the roll_no to delete : ")
    for i, student in enumerate(students):
        if students['roll_no'] == roll_no:
            del students[i]
            print("Students successfully deleted. ")
            return
    
    print("Students not found : ")

def display_student(student):
    print(f"\nName: {student['name']}")
    print(f"Roll Number: {student['roll_no']}")
    print(f"Class: {student['class']}")
    print("Subjects and Marks:")
    for subject, mark in student['subjects'].items():
        print(f"  {subject.strip()} : {mark}")
    total_marks = sum(student['subjects'].values())
    avg_marks = total_marks / len(student['subjects'])
    grade = calculate_grade(avg_marks)
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {avg_marks:.2f}")
    print(f"Grade: {grade}\n")

def show_all_students():
    if not students:
        print("No students found. ")
        return
    for student in students:
        display_student(student)
        print("-" * 30)

def calculate_grade(avg):
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
    

def main():

    while True:
        print("===== Students Management System =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            show_all_students()
        elif choice == '5':
            print("Exiting system. Goodbye! ")
            break
        else:
            print("Invalid choice. Please select from 1-5. ")

if __name__ == "__main__":
    main()



