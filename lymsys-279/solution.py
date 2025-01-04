
def color_code_manipulation(color_string: str, index_str: int, index_hex: int, increment: int) -> str:
    """Perform a manipulation on a string composed of color characters.

    Take a string composed of 'r', 'g', 'y', 'w' and 'b' characters
    and perform a manipulation based on the given parameters.

    Args:
        color_string: The input string made up of color characters.
        index_str: The index for manipulation in the color string.
        index_hex: The index for extraction from the hex string.
        increment: The value by which to increment the index
                   for further manipulation.

    Returns:
        A single character after the manipulation.
    """
    # Hexadecimal representations of the colors
    color_to_hex = {
        'r': 'FF0000',  # Red
        'g': '00FF00',  # Green
        'y': 'FFFF00',  # Yellow
        'w': 'FFFFFF',  # White
        'b': '0000FF',  # Blue
    }
    
    # Validate the input string
    if not color_string or index_str < 0 or index_hex < 0 or increment < 0:
        return 'Invalid'
    if index_str >= len(color_string):
        return 'Invalid'
    
    # Extract the nth letter
    extracted_char = color_string[index_str]
    
    # Check if the character is valid
    if extracted_char not in color_to_hex:
        return 'Invalid'
    
    # Find the hexadecimal representation of the color
    hex_value = color_to_hex[extracted_char]
    
    # Validate index_hex
    if index_hex >= len(hex_value):
        return 'Invalid'
    
    # Extract the character from the hex string
    hex_char = hex_value[index_hex]
    
    # Increment the ASCII code of the character
    new_ascii = ord(hex_char) + increment
    
    # Get the new character
    new_char = chr(new_ascii)
    
    return new_char