import os
from extract_solution import extract_solution

llm_response = '''
```python
def p(arr: list[int]) -> list[int]:
    """
    Given an array arr of integers, find all the elements that occur more than once in the array.
    Return the result in ascending order. If no element repeats, return an empty array.

    For example:
    find_duplicates([1, 2, 3, 1, 2, 4, 5]) == [1, 2]
    find_duplicates([1, 2, 3, 4, 5]) == []
    find_duplicates([1, 1, 1, 2, 2, 3]) == [1, 2]
    """
    counts = {}
    duplicates = set()

    for num in arr:
        if num in counts:
            duplicates.add(num)
        else:
            counts[num] = 1

    return sorted(list(duplicates))
```
'''

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


