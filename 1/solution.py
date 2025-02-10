"""Module for get_current_time function."""

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
    if not isinstance(timezone_offset, int):
        raise ValueError("Timezone offset must be an integer.")
    if not -24 <= timezone_offset <= 24:
        raise ValueError("Timezone offset must be between -24 and +24.")

    utc_now = datetime.now(timezone.utc)
    offset = timedelta(hours=timezone_offset)
    tz_aware_time = utc_now + offset

    return tz_aware_time.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    print(get_current_time(8))
    print(get_current_time(-5))
    print(get_current_time(0))
    print(get_current_time(12))
    print(get_current_time(24))
    print(get_current_time(-24))
    try:
        print(get_current_time("invalid"))
    except ValueError as e:
        print(e)
    try:
        print(get_current_time(25))
    except ValueError as e:
        print(e)
    try:
        print(get_current_time(-25))
    except ValueError as e:
        print(e)
