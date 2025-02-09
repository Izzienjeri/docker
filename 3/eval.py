"""Unit tests for the AddressBook class."""

import unittest

from solution import AddressBook


class TestAddressBook(unittest.TestCase):
    """Test cases for the AddressBook class."""

    def setUp(self):
        """Set up for each test case."""
        self.address_book = AddressBook()

    def test_add_new_record(self):
        """Test adding a new record."""
        self.address_book.insert(
            "John Doe", "123-456-7890", "john.doe@example.com", "123 Main St"
        )
        expected = {
            "John Doe": {
                "phone": "123-456-7890",
                "email": "john.doe@example.com",
                "address": "123 Main St",
            }
        }
        self.assertEqual(self.address_book.get(), expected)

    def test_update_existing_record(self):
        """Test updating an existing record."""
        self.address_book.insert(
            "John Doe", "123-456-7890", "john.doe@example.com", "123 Main St"
        )
        self.address_book.insert(
            "John Doe",
            "987-654-3210",
            "john.doe@newexample.com",
            "456 Oak Ave",
        )
        expected = {
            "John Doe": {
                "phone": "987-654-3210",
                "email": "john.doe@newexample.com",
                "address": "456 Oak Ave",
            }
        }
        self.assertEqual(self.address_book.get(), expected)

    def test_delete_existing_record(self):
        """Test deleting an existing record."""
        self.address_book.insert(
            "John Doe", "123-456-7890", "john.doe@example.com", "123 Main St"
        )
        self.address_book.delete("John Doe")
        self.assertEqual(self.address_book.get(), {})

    def test_delete_non_existent_record(self):
        """Test deleting a non-existent record."""
        with self.assertRaises(KeyError):
            self.address_book.delete("Jane Doe")

    def test_retrieve_all_records(self):
        """Test retrieving all records."""
        self.address_book.insert(
            "John Doe", "123-456-7890", "john.doe@example.com", "123 Main St"
        )
        self.address_book.insert(
            "Jane Doe", "098-765-4321", "jane.doe@example.com", "456 Elm St"
        )
        expected = {
            "John Doe": {
                "phone": "123-456-7890",
                "email": "john.doe@example.com",
                "address": "123 Main St",
            },
            "Jane Doe": {
                "phone": "098-765-4321",
                "email": "jane.doe@example.com",
                "address": "456 Elm St",
            },
        }
        self.assertEqual(self.address_book.get(), expected)

    def test_retrieve_from_empty_address_book(self):
        """Test retrieving from an empty address book."""
        self.assertEqual(self.address_book.get(), {})

    def test_insert_empty_name(self):
        """Test inserting record with empty name."""
        with self.assertRaises(ValueError):
            self.address_book.insert(
                "", "123-456-7890", "john.doe@example.com", "123 Main St"
            )

    def test_insert_empty_address(self):
        """Test inserting record with empty address."""
        with self.assertRaises(ValueError):
            self.address_book.insert(
                "John Doe", "123-456-7890", "john.doe@example.com", ""
            )

    def test_insert_none_name(self):
        """Test inserting record with None for name."""
        with self.assertRaises(ValueError):
            self.address_book.insert(
                None, "123-456-7890", "john.doe@example.com", "123 Main St"
            )

    def test_insert_none_address(self):
        """Test inserting record with None for address."""
        with self.assertRaises(ValueError):
            self.address_book.insert(
                "John Doe", "123-456-7890", "john.doe@example.com", None
            )


if __name__ == "__main__":
    unittest.main()
