def color_code_manipulation(
    color_string: str,
    index_str: int,
    index_hex: int,
    increment: int
) -> str:
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

    color_map = {
        'r': 'FF0000',
        'g': '008000',
        'y': 'FFFF00',
        'w': 'FFFFFF',
        'b': '0000FF'
    }

    try:
        # 1. Extract the nth letter specified by the user from the given string
        if not (0 <= index_str < len(color_string)):
            return "Invalid"
        color_char = color_string[index_str]

        # 2. Find the hexadecimal representation of this color
        if color_char not in color_map:
            return "Invalid"
        hex_color = color_map[color_char]

        # 3. Take the character as per the index given by the user from this
        if not (0 <= index_hex < len(hex_color)):
            return "Invalid"
        hex_char = hex_color[index_hex]

        # 4. Increment the ASCII code of this character by number specified by the user
        ascii_val = ord(hex_char)
        incremented_ascii = ascii_val + increment

        # 5. Return the new character corresponding to the incremented ASCII code
        return chr(incremented_ascii)

    except Exception:
        return "Invalid"