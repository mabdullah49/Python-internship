def is_valid_email(email):
    return '@' in email and '.' in email

def add_contact(contact_book):
    name = input("Enter contact name: ").title()
    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    if not is_valid_email(email):
        print("Invalid email format.")
        return
    contact_book[name] = {"phone": phone, "email": email}
    print(f"{name} added successfully.")

def update_contact(contact_book):
    name = input("Enter the name of the contact to update: ").title()
    if name not in contact_book:
        print("Contact not found.")
        return
    print("Leave field empty if no change.")
    phone = input("New phone number: ")
    email = input("New email address: ")
    if phone:
        contact_book[name]["phone"] = phone
    if email:
        if not is_valid_email(email):
            print("Invalid email format.")
            return
        contact_book[name]["email"] = email
    print(f"{name}'s contact updated.")

def retrieve_contact(contact_book):
    name = input("Enter contact name to retrieve: ").title()
    if name in contact_book:
        print(f"{name} - Phone: {contact_book[name]['phone']}, Email: {contact_book[name]['email']}")
    else:
        print("Contact not found.")

def view_all_contacts(contact_book):
    if not contact_book:
        print("Contact book is empty.")
        return
    print("\n📒 Contact Book:")
    for name, info in contact_book.items():
        print(f"{name} - Phone: {info['phone']}, Email: {info['email']}")
    print()

def contact_book_manager():
    contact_book = {
        "Ali": {"phone": "123", "email": "ali@email.com"},
        "Sara": {"phone": "999", "email": "sara@email.com"}
    }

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Retrieve Contact")
        print("4. View All Contacts")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            update_contact(contact_book)
        elif choice == '3':
            retrieve_contact(contact_book)
        elif choice == '4':
            view_all_contacts(contact_book)
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

contact_book_manager()
