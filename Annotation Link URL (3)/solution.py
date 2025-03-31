"""Binary search implementation for finding years in a list of dates."""
from datetime import date


def binary_search_year(dates: list[date], year: int) -> tuple[bool, int]:
    """
    Perform binary search to find a specific year in a list of dates.

    Args:
        dates: List of date objects to search through
        year: Target year to find

    Returns:
        tuple[bool, int]: (Found/not found, Number of recursive calls made)
    """
    # Handle empty list case explicitly
    if not dates:
        return False, 0

    # Sort dates by year in ascending order
    dates.sort(key=lambda date: date.year)

    # Calculate midpoint
    mid_index = len(dates) // 2
    mid_year = dates[mid_index].year

    # Base case: found the year
    if mid_year == year:
        return True, 1

    # Recursive cases
    if mid_year < year:
        # Search right half
        found, calls = binary_search_year(dates[mid_index + 1:], year)
    else:
        # Search left half
        found, calls = binary_search_year(dates[:mid_index], year)

    # Return result and increment call counter
    return found, calls + 1