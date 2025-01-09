def process_string(input_string: str, target_letter: str) -> dict:
    """
    Arranges words in a string alphabetically, then returns a dictionary where keys are words 
    starting with a given letter and values are lists of indices where these words appear in 
    the sorted list of words.
    
    Args:
        input_string: String containing words separated by spaces
        target_letter: Letter to search for at the beginning of words
        
    Returns:
        Dictionary with words as keys and lists of indices as values
    """
    # Split the string into words and sort them alphabetically (case-insensitive)
    words = input_string.split()
    sorted_words = sorted(words, key=str.lower)
    
    # Create dictionary to store results
    result = {}
    
    # Iterate through the sorted words
    for i, word in enumerate(sorted_words):
        # Check if word starts with target letter (case-insensitive)
        if word.lower().startswith(target_letter.lower()):
            # Add word to dictionary if not present
            if word not in result:
                result[word] = []
            # Append index to the word's list
            result[word].append(i)
    
    return result
