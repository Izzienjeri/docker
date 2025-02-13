def parse_and_convert(input_str):
    """
    Parses a string of numbers and returns a list of integer pairs.
    
    Args:
        input_str: A string containing numbers where pairs are separated by spaces,
                  and newlines start a new pair.
    
    Returns:
        A list of tuples, where each tuple contains two integers.
    
    Examples:
        >>> parse_and_convert("1 2\n3 4")
        [(1, 2), (3, 4)]
        >>> parse_and_convert("1 2 3 4")
        [(1, 2), (3, 4)]
        >>> parse_and_convert("")
        []
    """
    # Handle empty string
    if not input_str.strip():
        return []
    
    result = []
    # Split into lines and handle trailing newline
    lines = input_str.strip().split('\n')
    
    current_numbers = []
    
    for line in lines:
        # Split the line into numbers, handling extra spaces
        numbers = [int(num) for num in line.strip().split()]
        
        # Process numbers from previous line
        while len(current_numbers) >= 2:
            result.append((current_numbers[0], current_numbers[1]))
            current_numbers = current_numbers[2:]
            
        # Add numbers from current line
        current_numbers.extend(numbers)
        
        # Process pairs from current line
        while len(current_numbers) >= 2:
            result.append((current_numbers[0], current_numbers[1]))
            current_numbers = current_numbers[2:]
    
    return result