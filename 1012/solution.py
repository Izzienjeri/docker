"""This module provides a function to find the number of LIS in an array."""


def find_number_of_lis(nums: list[int]) -> int:
    """
    Given integer array nums, return number of longest increasing subsequences.

    Args:
        nums (list[int]): The input array of integers.

    Returns:
        int: The number of longest increasing subsequences.
    """
    if not nums:
        return 0

    n = len(nums)
    lengths = [1] * n
    counts = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]

    longest = max(lengths)
    return sum(counts[i] for i in range(n) if lengths[i] == longest)


# Example usage
if __name__ == "__main__":
    print(find_number_of_lis([1, 3, 5, 4, 7]))
    print(find_number_of_lis([2, 2, 2, 2, 2]))
    print(find_number_of_lis([5, 4, 3, 2, 1]))
