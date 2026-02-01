import os

FILE_NAME = "contacts.txt"

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip().split(",") for line in file]
    
def get_valid_phone():
    while True:
        phone = input("Enter phone number: ")
        if phone.isdigit():
            return phone
        else:
            print("Phone number must contain only digits. Try again.")

def get_valid_email():
    while True:
        email = input("Enter email: ")
        if email.endswith("@gmail.com"):
            return email
        else:
            print("Email must end with @gmail.com. Try again.")



def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, phone, email in contacts:
            file.write(f"{name},{phone},{email}\n")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = get_valid_phone()
    email = get_valid_email()
    contacts.append([name, phone, email])
    save_contacts(contacts)
    print("Contact added!\n")



def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nName\tPhone\tEmail")
    print("---------------------------------")
    for name, phone, email in contacts:
        print(f"{name}\t{phone}\t{email}")
    print()

def search_contact(contacts):
    name = input("Enter name to search: ").lower()
    for contact in contacts:
        if contact[0].lower() == name:
            print(f"Found: {contact[0]} - {contact[1]} - {contact[2]}\n")
            return
    print("Contact not found.\n")

def delete_contact(contacts):
    name = input("Enter name to delete: ").lower()
    contacts = [c for c in contacts if c[0].lower() != name]
    save_contacts(contacts)
    print("Contact deleted if it existed.\n")

def edit_contact(contacts):
    name = input("Enter name to edit: ").lower()
    for contact in contacts:
        if contact[0].lower() == name:
            contact[1] = get_valid_phone()
            contact[2] = get_valid_email()
            save_contacts(contacts)
            print("Contact updated!\n")
            return
    print("Contact not found.\n")



def main():
    while True:
        contacts = load_contacts()
        print("=== CONTACT BOOK ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Edit Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            edit_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
