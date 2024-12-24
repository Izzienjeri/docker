class AddressBook:
    """Class to implement Address Book."""

    def __init__(self):
        """Initialize an empty address book."""
        self.records = {}

    def get(self):
        """Get all records in the address book.

        Returns:
            A dictionary of all the records in the address book.
            Returns empty dictionary if the address book is empty.
        """
        return self.records

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
            raise ValueError("Name and address cannot be empty or None.")

        self.records[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }

    def delete(self, name):
        """Delete a record from the address book.

        Args:
            name (str): The name of the contact to delete.

        Raises:
            KeyError: If the record does not exist in the address book.
        """
        if name not in self.records:
            raise KeyError(f"No record found for {name}.")

        del self.records[name]
