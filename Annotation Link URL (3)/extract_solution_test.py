import os
from extract_solution import extract_solution

llm_response = '''
```python
from datetime import date

def binary_search_year(dates: list[date], year: int) -> tuple[bool, int]:
    """Searches for a date within a given year in a sorted list of dates.

    Args:
        dates: A list of Date instances.
        year: The year to search for.

    Returns:
        A tuple containing:
        - True if a date within the year is found, False otherwise.
        - The number of recursive calls made.
    """
    dates.sort(key=lambda date: date.year)
    
    def _binary_search_year(dates, year, low, high, count):
        if low > high:
            return False, count
        
        mid = (low + high) // 2
        mid_year = dates[mid].year
        
        if mid_year == year:
            return True, count + 1
        elif mid_year < year:
            return _binary_search_year(dates, year, mid + 1, high, count + 1)
        else:
            return _binary_search_year(dates, year, low, mid - 1, count + 1)

    if not dates:
        return False, 0  # Handle empty list case

    return _binary_search_year(dates, year, 0, len(dates) - 1, 0)
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
        break

except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")

except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")
