import os
from extract_solution import extract_solution

llm_response = '''
I'll help you create a function that parses number pairs while handling newlines and ignoring unpaired numbers.



```python
def parse_and_convert(input_str):
    """
    Parses a string of numbers and returns a list of integer pairs.

    Args:
        input_str: A string containing numbers separated by spaces and newlines.

    Returns:
        A list of tuples, where each tuple contains two integers.
    """
    # Split the input string by newlines to handle each line separately
    lines = input_str.strip().split('\n')
    result = []
    
    for line in lines:
        # Split each line into numbers and convert to integers
        # Filter out any non-numeric values
        numbers = []
        for num in line.split():
            try:
                numbers.append(int(num))
            except ValueError:
                continue
        
        # Process pairs in the current line
        for i in range(0, len(numbers) - 1, 2):
            result.append((numbers[i], numbers[i + 1]))
    
    return result


# Test cases
def test_parse_and_convert():
    # Test case 1: Basic pairs
    assert parse_and_convert("1 2 3 4") == [(1, 2), (3, 4)]
    
    # Test case 2: Multiple lines
    assert parse_and_convert("1 2\n3 4\n5 6") == [(1, 2), (3, 4), (5, 6)]
    
    # Test case 3: Ignore unpaired numbers
    assert parse_and_convert("1 2 3") == [(1, 2)]
    
    # Test case 4: Empty string
    assert parse_and_convert("") == []
    
    # Test case 5: Mixed format
    assert parse_and_convert("1 2\n3 4 5\n6 7") == [(1, 2), (3, 4), (6, 7)]
    
    # Test case 6: Extra whitespace
    assert parse_and_convert("  1   2  \n  3    4  ") == [(1, 2), (3, 4)]
    
    print("All test cases passed!")

# Run the tests
test_parse_and_convert()

```

I've implemented the function with the following features:

1. Handles multiple lines by splitting on newlines
2. Processes each line separately to ensure pairs don't cross line boundaries
3. Converts strings to integers and handles invalid input gracefully
4. Ignores unpaired numbers at the end of lines
5. Handles extra whitespace
6. Includes comprehensive test cases

You can use it like this:

```python
# Example usage
input_string = """1 2
3 4 5
6 7"""

result = parse_and_convert(input_string)
print(result)  # Output: [(1, 2), (3, 4), (6, 7)]
```

The function will:
- Parse pairs (1,2) from the first line
- Parse pairs (3,4) from the second line, ignoring the unpaired 5
- Parse pairs (6,7) from the third line

Would you like me to add any additional features or edge cases to handle?
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
