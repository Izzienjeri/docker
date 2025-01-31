def p(arr: list[int]) -> list[int]:
    """
    Given an array arr of integers, find all the elements that occur more than once in the array.
    Return the result in ascending order. If no element repeats, return an empty array.

    For example:
    find_duplicates([1, 2, 3, 1, 2, 4, 5]) == [1, 2]
    find_duplicates([1, 2, 3, 4, 5]) == []
    find_duplicates([1, 1, 1, 2, 2, 3]) == [1, 2]
    """
    counts = {}
    duplicates = set()

    for num in arr:
        if num in counts:
            duplicates.add(num)
        else:
            counts[num] = 1

    return sorted(list(duplicates))