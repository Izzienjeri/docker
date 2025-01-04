
def fibonacci_sequence(n):
    """
    Computes the nth Fibonacci number efficiently.

    Args:
        The position of the desired Fibonacci number in the sequence.

    Returns:
       The nth Fibonacci number or none.
    
    """
    if not isinstance(n, int) or n < 0:
        return None

    if n == 0:
        return "The 0th Fibonacci number is: 0"
    elif n == 1:
        return "The 1st Fibonacci number is: 1"
    else:
        a = 0
        b = 1
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return f"The {n}th Fibonacci number is: {b}"
