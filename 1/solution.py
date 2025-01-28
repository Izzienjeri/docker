def bubble_sort(arr: list[int]) -> list[int]:
    """ Sorts a list of integers in ascending order using the Bubble Sort algorithm.
    Args:
        arr: The list of integers to be sorted.
    Returns:
        A list containing the sorted integers.
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize the algorithm - if no swaps occur, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap them if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred in this pass, array is already sorted
        if not swapped:
            break
            
    return arr