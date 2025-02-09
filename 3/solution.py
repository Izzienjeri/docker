"""A Simple Address Book Implementation."""


class AddressBook:
    """Class to implement Address Book."""

    def __init__(self):
        """Initialize an empty address book."""
        self.address_book = {}

    def get(self):
        """Get all records in the address book.

        Returns:
            A dictionary of all the records in the address book.
            Returns empty dictionary if the address book is empty.
        """
        return self.address_book

    def insert(self, name, phone, email, address):
        """Add a new record to the address book.

        Add a new record to the address book. Updates the existing fields if
        the record exists.

        Args:
            name (str): The name of the contact.
            phone (str): The phone number of the contact.
            email (str): The email address of the contact.
            address (str): The address of the contact.

        Raises:
            ValueError: If the value associated with the name or address
                is empty or None.
        """
        if not name or not address:
            raise ValueError("Name and address cannot be empty or None")

        self.address_book[name] = {
            "phone": phone,
            "email": email,
            "address": address,
        }

    def delete(self, name):
        """Delete a record from the address book.

        Args:
            name (str): The name of the contact to delete.

        Raises:
            KeyError: If the record does not exist in the address book.
        """
        if name not in self.address_book:
            raise KeyError(f"Record for {name} does not exist")

        del self.address_book[name]


if __name__ == "__main__":
    address_book = AddressBook()

    # Sample data for insertion
    valid_data = [
        ("John Doe", "123-456-7890", "john.doe@example.com", "123 Main St"),
        (
            "Jane Smith",
            "987-654-3210",
            "jane.smith@example.com",
            "456 Oak Ave",
        ),
        (
            "Peter Jones",
            "555-123-4567",
            "peter.jones@example.com",
            "789 Pine Ln",
        ),
    ]

    # Insert valid data
    for name, phone, email, address in valid_data:
        address_book.insert(name, phone, email, address)

    # Test get() method
    print(address_book.get())

    # Expected output (order might vary):
    # {'John Doe': {'phone': '123-456-7890', 'email': 'john.doe@example.com',
    # 'address': '123 Main St'},
    #  'Jane Smith': {'phone': '987-654-3210', 'email': '
    # jane.smith@example.com', 'address': '456 Oak Ave'},
    #  'Peter Jones': {'phone': '555-123-4567', 'email':
    # 'peter.jones@example.com', 'address': '789 Pine Ln'}}

    # Test delete() method
    address_book.delete("Jane Smith")
    print(address_book.get())
    # Expected output (order might vary):
    # {'John Doe': {'phone': '123-456-7890', 'email': 'john.doe@example.com',
    # 'address': '123 Main St'},
    #  'Peter Jones': {'phone': '555-123-4567', 'email':
    # 'peter.jones@example.com', 'address': '789 Pine Ln'}}

    address_book = AddressBook()

    # Empty name
    try:
        address_book.insert(
            "", "123-456-7890", "john.doe@example.com", "123 Main St"
        )
    except ValueError as e:
        print(f"Caught expected ValueError: {e}")

    # Empty address
    try:
        address_book.insert(
            "John Doe", "123-456-7890", "john.doe@example.com", ""
        )
    except ValueError as e:
        print(f"Caught expected ValueError: {e}")

    # Delete non-existent record
    try:
        address_book.delete("NonExistent")
    except KeyError as e:
        print(f"Caught expected KeyError: {e}")

    # Insert with None values for optional fields
    address_book.insert("John Doe", None, None, "123 Main St")
    print(address_book.get())
    # Expected output (order might vary):
    # {'John Doe': {'phone': None, 'email': None, 'address': '123 Main St'}}
