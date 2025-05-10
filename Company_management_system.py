import json

company = []

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    employee = {
        "ID": emp_id,
        "Name": name,
        "Department": department,
        "Salary": salary
    }
    company.append(employee)
    print("Employee added successfully.\n")

def remove_employee():
    emp_id = input("Enter Employee ID to remove: ")
    for emp in company:
        if emp["ID"] == emp_id:
            company.remove(emp)
            print("Employee removed successfully.\n")
            return
    print("Employee not found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    for emp in company:
        if emp["ID"] == emp_id:
            print("1. Update Name\n2. Update Department\n3. Update Salary")
            choice = input("Enter choice: ")
            if choice == "1":
                emp["Name"] = input("Enter new name: ")
            elif choice == "2":
                emp["Department"] = input("Enter new department: ")
            elif choice == "3":
                emp["Salary"] = float(input("Enter new salary: "))
            else:
                print("Invalid choice.")
            print("Employee updated successfully.\n")
            return
    print("Employee not found.\n")

def view_all_employees():
    if not company:
        print("No employees found.\n")
        return
    for emp in company:
        print(emp)
    print()

def search_by_id():
    emp_id = input("Enter ID to search: ")
    for emp in company:
        if emp["ID"] == emp_id:
            print(emp)
            return
    print("Employee not found.\n")

def search_by_name():
    name = input("Enter Name to search: ")
    for emp in company:
        if emp["Name"].lower() == name.lower():
            print(emp)
            return
    print("Employee not found.\n")

def sort_employees():
    print("Sort by:\n1. Name\n2. Salary\n3. Department")
    choice = input("Enter choice: ")
    if choice == "1":
        sorted_list = sorted(company, key=lambda x: x["Name"])
    elif choice == "2":
        sorted_list = sorted(company, key=lambda x: x["Salary"])
    elif choice == "3":
        sorted_list = sorted(company, key=lambda x: x["Department"])
    else:
        print("Invalid choice.")
        return
    for emp in sorted_list:
        print(emp)
    print()

def view_statistics():
    if not company:
        print("No employees to analyze.\n")
        return
    total_salary = sum(emp["Salary"] for emp in company)
    average_salary = total_salary / len(company)
    max_salary = max(company, key=lambda x: x["Salary"])
    print(f"Total Employees: {len(company)}")
    print(f"Average Salary: {average_salary}")
    print(f"Highest Paid Employee: {max_salary['Name']} with Salary: {max_salary['Salary']}\n")

def save_to_file():
    with open("employees.json", "w") as file:
        json.dump(company, file)
    print("Data saved to file.\n")

def load_from_file():
    global company
    try:
        with open("employees.json", "r") as file:
            company = json.load(file)
        print("Data loaded from file.\n")
    except FileNotFoundError:
        print("No saved data found.\n")

def menu():
    while True:
        print("\n=== Company Management Menu ===")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. View All Employees")
        print("5. Search by ID")
        print("6. Search by Name")
        print("7. Sort Employees")
        print("8. View Salary Statistics")
        print("9. Save to File")
        print("10. Load from File")
        print("11. Exit")
        
        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            view_all_employees()
        elif choice == "5":
            search_by_id()
        elif choice == "6":
            search_by_name()
        elif choice == "7":
            sort_employees()
        elif choice == "8":
            view_statistics()
        elif choice == "9":
            save_to_file()
        elif choice == "10":
            load_from_file()
        elif choice == "11":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
