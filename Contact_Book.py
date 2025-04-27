contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {"phone": phone, "email": email}

def search_contact(name):
    return contacts.get(name)

def delete_contact(name):
    if name in contacts:
        del contacts[name]

def edit_contact(name, new_phone=None, new_email=None):
    if name in contacts:
        if new_phone:
            contacts[name]['phone'] = new_phone
        if new_email:
            contacts[name]['email'] = new_email

def show_contact(name):
    person = search_contact(name)
    if person:
        print(f"\nName: {name}")
        print(f"Phone: {person['phone']}")
        print(f"Email: {person['email']}")
    else:
        print("Contact not found.")

def show_all_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for name in contacts:
        show_contact(name)
        print("-" * 20)

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Show All Contacts")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)

        elif choice == '2':
            name = input("Enter name to search: ")
            show_contact(name)

        elif choice == '3':
            name = input("Enter name to edit: ")
            new_phone = input("Enter new phone (leave empty to skip): ")
            new_email = input("Enter new email (leave empty to skip): ")
            new_phone = new_phone if new_phone else None
            new_email = new_email if new_email else None
            edit_contact(name, new_phone, new_email)

        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == '5':
            show_all_contacts()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
