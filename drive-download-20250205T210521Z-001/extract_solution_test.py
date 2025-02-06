import os

from extract_solution import extract_solution

llm_response = '''

Let me help you complete this function. I'll implement the logic to classify integers according to the specified conditions:

```python
def classify_integer(num: int) -> str | None:
    """
    Classifies an integer based on the following conditions:
    - If the integer is greater than 100, return "Greater than 100".
    - If the integer is between 50 and 100 (inclusive), return "Between 50 and 100".
    - If the integer is less than 50, return "Less than 50".
    """
    if num > 100:
        return "Greater than 100"
    elif 50 <= num <= 100:
        return "Between 50 and 100"
    else:
        return "Less than 50"
```

This implementation:

1. Takes an integer parameter `num`
2. Uses if-elif-else statements to check the conditions in order
3. Returns the appropriate string based on the value of `num`

The function will classify any integer input according to the specified ranges. Note that all possible integer inputs are covered by these conditions, so the function will always return one of the three specified strings.

You can test it with values like:
- `classify_integer(150)` returns "Greater than 100"
- `classify_integer(75)` returns "Between 50 and 100"
- `classify_integer(25)` returns "Less than 50"
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