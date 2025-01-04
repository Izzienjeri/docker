import re

def reformat_date(date_str: str) -> str:
    """Convert a date string to 'dd-mm-yyyy' format.
    Args:
        date_str: It can be in any format with any type of delimiters usage.
    Returns:
        The reformatted date string in 'dd-mm-yyyy' format.
    Raises:
        ValueError: If the date string is invalid or doesn't meet the requirements.
    """
    if not date_str or not isinstance(date_str, str):
        raise ValueError("Input must be a non-empty string")
    
    # Remove leading, trailing, and extra spaces within the string
    date_str = re.sub(r'\s+', ' ', date_str.strip())
    
    # Regular expression to match the date components
    # Matches: year (1-4 digits) followed by optional delimiters,
    # month (1-2 digits) followed by optional delimiters,
    # day (1-2 digits)
    pattern = r'^(\d{1,4})\s*[-./\\\ ]*\s*(\d{1,2})\s*[-./\\\ ]*\s*(\d{1,2})$'
    
    match = re.match(pattern, date_str)
    if not match:
        raise ValueError("Invalid date format")
    
    year, month, day = match.groups()
    
    # Convert to integers for validation
    try:
        year = int(year)
        month = int(month)
        day = int(day)
    except ValueError:
        raise ValueError("Invalid numeric values")
    
    # Validate year range (1950 exclusive to 2050 inclusive)
    if not (1950 < year <= 2050):
        # Handle 2-digit year
        if len(str(year)) <= 2:
            year = 2000 + year if year <= 50 else 1900 + year
            if not (1950 < year <= 2050):
                raise ValueError("Year must be between 1950 (exclusive) and 2050 (inclusive)")
        else:
            raise ValueError("Year must be between 1950 (exclusive) and 2050 (inclusive)")
    
    # Validate month and day
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    # Get maximum days for the given month
    days_in_month = {
        1: 31, 2: 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28,
        3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    if not (1 <= day <= days_in_month[month]):
        raise ValueError(f"Invalid day for month {month}")
    
    # Format the date in dd-mm-yyyy format
    return f"{day:02d}-{month:02d}-{year:04d}"
