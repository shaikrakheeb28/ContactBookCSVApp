# test_contact_book_csv.py

import unittest
import os
import csv
from contact_book_csv import ContactBookCSV

class TestContactBookCSV(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_contacts.csv"
        with open(self.test_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])
        self.book = ContactBookCSV(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_contact(self):
        result = self.book.add_contact("Alice", "123", "alice@example.com")
        self.assertEqual(result, "Contact added successfully.")
        self.assertTrue(self.book.contact_exists("Alice"))

    def test_view_contact(self):
        self.book.add_contact("Bob", "456", "bob@example.com")
        contact = self.book.view_contact("Bob")
        self.assertEqual(contact["Phone"], "456")

    def test_update_contact(self):
        self.book.add_contact("Charlie", "789", "charlie@example.com")
        result = self.book.update_contact("Charlie", phone="000")
        self.assertEqual(result, "Contact updated successfully.")
        contact = self.book.view_contact("Charlie")
        self.assertEqual(contact["Phone"], "000")

    def test_delete_contact(self):
        self.book.add_contact("David", "111", "david@example.com")
        result = self.book.delete_contact("David")
        self.assertEqual(result, "Contact deleted successfully.")
        self.assertEqual(self.book.view_contact("David"), "Contact not found.")

if __name__ == "__main__":
    unittest.main()
