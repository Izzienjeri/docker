import os
from extract_solution import extract_solution

llm_response = '''
```python
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
```
'''

try:
    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):
        raise ValueError(
            "Expected response to be a list of (file_name, code) tuples."
        )

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Check if the file itself exists
        if not os.path.isfile(file_name):
            raise FileNotFoundError(
                f"The file '{file_name}' does not exist. "
                "Please check the path."
            )

        # Proceed to write only if the file already exists
        with open(file_name, "w") as file:
            file.write(code)

        print(f"File '{file_name}' written successfully.")


except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")

except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")
