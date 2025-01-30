def evaluate_string(a: str) -> bool:
    """
    Evaluates a 2-digit string based on the following conditions:
    1.  Returns True if all digits are greater than 4.
    2.  Returns True if the first digit is 6.
    3.  Returns False for invalid strings (not 2 digits, non-numeric).
    4.  Returns False otherwise.
    """
    if not (len(a) == 2 and a.isdigit()):
        return False
    c = int(a[0]) > 4
    d = int(a[1]) > 4
    f = int(a[0]) == 6
    return (c and d) or f
# Test cases
print(evaluate_string("56"))  # True (both digits > 4)
print(evaluate_string("61"))  # True (first digit is 6)
print(evaluate_string("45"))  # False
print(evaluate_string("73"))  # False
print(evaluate_string("123")) # False (invalid length)
print(evaluate_string("a7"))  # False (non-numeric)
print(evaluate_string(""))   # False (invalid length)