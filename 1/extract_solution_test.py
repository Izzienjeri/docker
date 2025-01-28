import os

from extract_solution import extract_solution

llm_response = '''

```python
def bubble_sort(arr: list[int]) -> list[int]:
  """
  Sorts a list of integers in ascending order using the Bubble Sort algorithm.

  Args:
    arr: The list of integers to be sorted.

  Returns:
    A list containing the sorted integers.
  """
  n = len(arr)
  for i in range(n):
    # Last i elements are already in place, so we don't need to iterate through them.
    for j in range(0, n - i - 1):
      # Swap if the element found is greater than the next element.
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr
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

