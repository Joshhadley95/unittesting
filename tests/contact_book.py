def manage_contacts():
    manage_contacts = {}
    while True:
        choice = input("Enter 'add' to add a contact, 'view' to view contacts, 'delete' to delete a contact, or 'exit' to quit: ").lower()
        if choice == 'add':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            manage_contacts[name] = phone
            print(f"Contact '{name}' added successfully.")
        elif choice == 'view':
            if not manage_contacts:
                print("No contacts found.")
            else:
                print("\nContacts:")
                for name, phone in manage_contacts.items():
                    print(f"Name: {name}, Phone: {phone}")
        elif choice == 'delete':
            name = input("Enter the name of the contact to delete: ")
            if name in manage_contacts:
                del manage_contacts[name]
                print(f"Contact '{name}' deleted successfully.")
            else:
                print(f"Contact '{name}' not found.")
        elif choice == 'exit':
            print("Exiting Contact Book Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
        return "Contact book management system is under development."

manage_contacts()


