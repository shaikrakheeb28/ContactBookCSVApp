# contact_book_csv.py

import csv
import os

class ContactBookCSV:
    def __init__(self, filename="contacts.csv"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone", "Email"])

    def add_contact(self, name, phone, email):
        if self.contact_exists(name):
            return "Contact already exists."
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, email])
        return "Contact added successfully."

    def contact_exists(self, name):
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Name"] == name:
                    return True
        return False

    def view_contact(self, name):
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Name"] == name:
                    return row
        return "Contact not found."

    def view_all_contacts(self):
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)
            return contacts if contacts else "No contacts available."

    def update_contact(self, name, phone=None, email=None):
        updated = False
        contacts = []
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Name"] == name:
                    if phone:
                        row["Phone"] = phone
                    if email:
                        row["Email"] = email
                    updated = True
                contacts.append(row)

        if not updated:
            return "Contact not found."

        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email"])
            writer.writeheader()
            writer.writerows(contacts)
        return "Contact updated successfully."

    def delete_contact(self, name):
        deleted = False
        contacts = []
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Name"] == name:
                    deleted = True
                else:
                    contacts.append(row)

        if not deleted:
            return "Contact not found."

        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email"])
            writer.writeheader()
            writer.writerows(contacts)
        return "Contact deleted successfully."

def main():
    book = ContactBookCSV()
    while True:
        print("\n=== Contact Book (CSV) Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. View All Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            print(book.add_contact(name, phone, email))

        elif choice == "2":
            name = input("Enter name to view: ")
            result = book.view_contact(name)
            print(result)

        elif choice == "3":
            contacts = book.view_all_contacts()
            if isinstance(contacts, str):
                print(contacts)
            else:
                for contact in contacts:
                    print(f"{contact['Name']} - Phone: {contact['Phone']}, Email: {contact['Email']}")

        elif choice == "4":
            name = input("Name to update: ")
            phone = input("New phone (leave blank to keep current): ")
            email = input("New email (leave blank to keep current): ")
            phone = phone if phone else None
            email = email if email else None
            print(book.update_contact(name, phone, email))

        elif choice == "5":
            name = input("Name to delete: ")
            print(book.delete_contact(name))

        elif choice == "6":
            print("Exiting Contact Book.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
