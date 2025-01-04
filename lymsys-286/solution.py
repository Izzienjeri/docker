
def convert_hex_to_required(hex_value: str, conversion_type: str) -> str:
    """
    Convert a hexadecimal string to a specified format.
    Args:
        hex_value (str): Hexadecimal string (e.g., '0xa').
        conversion_type (str): Target format ('decimal', 'binary', or 'octal').
    Returns:
        str: Converted value.
    Raises:
        ValueError: If the hex value or conversion type is invalid.
    """
    # Validate conversion type
    valid_types = {'decimal', 'binary', 'octal'}
    if conversion_type.lower() not in valid_types:
        raise ValueError("Invalid conversion type. Must be 'decimal', 'binary', or 'octal'")
    
    # Convert hex string to integer
    try:
        # Convert hex to integer, handling both '0xa' and 'a' formats
        hex_value = hex_value.lower()
        if not hex_value.startswith('0x'):
            hex_value = '0x' + hex_value
        decimal_value = int(hex_value, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal value")
    
    # Convert to required format
    conversion_type = conversion_type.lower()
    if conversion_type == 'decimal':
        return str(decimal_value)
    elif conversion_type == 'binary':
        # Remove '0b' prefix from binary string
        return bin(decimal_value)[2:]
    else:  # octal
        # Remove '0o' prefix from octal string
        return oct(decimal_value)[2:]
