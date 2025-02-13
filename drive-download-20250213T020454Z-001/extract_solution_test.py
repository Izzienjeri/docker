import os
from extract_solution import extract_solution

llm_response = '''
```python
def parse_and_convert(input_str):
    """
    Parses a string of numbers and returns a list of integer pairs.

    Args:
        input_str: A string containing numbers separated by spaces and newlines.

    Returns:
        A list of tuples, where each tuple contains two integers.
    """
    numbers = []
    for line in input_str.splitlines():
        for num_str in line.split():
            try:
                numbers.append(int(num_str))
            except ValueError:
                print(f"Warning: Could not parse '{num_str}' as an integer. Ignoring it.")

    pairs = []
    i = 0
    while i < len(numbers) - 1:
        pairs.append((numbers[i], numbers[i+1]))
        i += 2

    return pairs
```

'''

try:
    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):
        raise ValueError("Expected response to be a list of"
                         "(file_name, code) tuples.")

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Check if the file itself exists
        if not os.path.isfile(file_name):
            raise FileNotFoundError(
                f"The file '{file_name}' does not exist."
                f"Please check the path."
            )

        # Proceed to write only if the file already exists
        with open(file_name, "w") as file:
            file.write(code)

        print(f"File '{file_name}' written successfully.")

except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")

except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")
