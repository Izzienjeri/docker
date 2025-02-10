import os
from extract_solution import extract_solution

llm_response = '''
Here is the implementation for the function `get_current_time`: 

```python
from datetime import datetime, timedelta, timezone

def get_current_time(timezone_offset: int) -> str:
    """Return the current date and time for the specified timezone offset.

    Args:
        timezone_offset (int): The offset from UTC in hours.

    Raises:
        ValueError: If `timezone_offset` is not an integer or is out of the 
            valid range (-24 to +24).

    Returns:
        str: A string containing the current date and time formatted
        as "YYYY-MM-DD HH:MM:SS".
    """
    if not isinstance(timezone_offset, int) or not -24 <= timezone_offset <= 24:
        raise ValueError("Timezone offset must be an integer between -24 and +24.")

    # Create a timezone object with the specified offset
    tz = timezone(timedelta(hours=timezone_offset))
    
    # Get the current time in the specified timezone
    current_time = datetime.now(tz)

    # Format and return the date and time as a string
    return current_time.strftime("%Y-%m-%d %H:%M:%S")

# Example usage:
try:
    print(get_current_time(5))  # For UTC+5
    print(get_current_time(-3))  # For UTC-3
except ValueError as e:
    print(e)
```

### Explanation:
1. **Input Validation**:
   - Ensures the `timezone_offset` is an integer within the valid range (-24 to +24). Raises a `ValueError` if it's not.

2. **Timezone Creation**:
   - Uses `timedelta(hours=timezone_offset)` to create a `timezone` object representing the offset from UTC.

3. **Current Time**:
   - Fetches the current time adjusted to the specified timezone using `datetime.now(tz)`.

4. **Formatting**:
   - Formats the datetime into a string in the format "YYYY-MM-DD HH:MM:SS" using `strftime`. 

This function is robust for general use and will handle invalid inputs appropriately.
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
