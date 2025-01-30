import os

from extract_solution import extract_solution

llm_response = '''

There are a few issues in the original code: one logic error (duplicate line) and no input validation. Here's the corrected version as a function:

```python
def evaluate_string(a: str) -> bool:
    # Check if input is valid (2 digits)
    if not (len(a) == 2 and a.isdigit()):
        return False
    
    # Convert conditions to boolean values
    c = int(a[0]) > 4
    d = int(a[1]) > 4
    f = int(a[0]) == 6
    
    # Return the result of the logical expression
    return (c and d) or f
```

Key changes made:
1. Removed the duplicate line `e=int(a[1]>4)` since it was redundant
2. Added input validation to check if the string has exactly 2 characters and they're both digits
3. Converted the logic to use boolean values directly instead of converting to int
4. Added proper type hints for input and output
5. Fixed the typo in the type hint (`string` should be `str`)

The function will:
- Return False for invalid inputs (non-digits or wrong length)
- Return True if either:
  - The first digit is greater than 4 AND the second digit is greater than 4
  - OR if the first digit is 6
- Return False otherwise '''

try:

    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):

        raise ValueError("Expected response to be a list of (file_name, code) tuples.")

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:

            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Check if the file itself exists

        if not os.path.isfile(file_name):

            raise FileNotFoundError(

                f"The file '{file_name}' does not exist. Please check the path."

            )

        # Proceed to write only if the file already exists

        with open(file_name, "w") as file:

            file.write(code)

        print(f"File '{file_name}' written successfully.")

except FileNotFoundError as fnf_error:

    print(f"File error: {fnf_error}")

except Exception as e:

    print(f"An error occurred while running extract solution test: {e}")