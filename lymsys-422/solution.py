import datetime


def generate_leap_years() -> list[int]:
    """Generate a list of the next 20 leap years from the current year."""
    current_year = datetime.datetime.now().year
    leap_years = []
    year = current_year + 1  # Start from the next year

    while len(leap_years) < 20:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            leap_years.append(year)
        year += 1

    return leap_years