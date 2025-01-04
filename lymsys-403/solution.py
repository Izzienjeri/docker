def efficient_sort(arr):
    """
    Determine the most efficient sorting algorithm for the input array.
    Args:
    arr (list): The list of integers to be analyzed.
    Raises:
    TypeError: If the input is not a list.
    ValueError: If the list is empty or element in list is not an integer.
    Returns:
    str: The name of the most efficient sorting algorithm.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not arr:
        raise ValueError("Input list cannot be empty")
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")

    # Helper functions
    def is_small_dataset(arr):
        """Check if the dataset is small (n < 20)."""
        return len(arr) < 20

    def is_nearly_sorted(arr):
        """
        Check if the list is nearly sorted by counting inversions.
        A list is considered nearly sorted if less than 10% of adjacent 
        elements are out of order.
        """
        inversions = sum(1 for i in range(len(arr)-1) if arr[i] > arr[i+1])
        return inversions <= len(arr) * 0.1

    def has_significant_duplicates(arr):
        """
        Check if the list has significant duplicates (>20% duplicate ratio).
        """
        unique_count = len(set(arr))
        total_count = len(arr)
        duplicate_ratio = 1 - (unique_count / total_count)
        return duplicate_ratio > 0.2

    # Decision logic with priority structure
    # 1. Check for small dataset (highest priority)
    if is_small_dataset(arr):
        return "Insertion Sort"
    
    # 2. Check for nearly sorted data (second priority)
    if is_nearly_sorted(arr):
        return "Insertion Sort"
    
    # 3. Check for significant duplicates in larger datasets
    if has_significant_duplicates(arr):
        return "3-way Quick sort"
    
    # 4. Default case: large dataset with no special characteristics
    return "Quick sort"
