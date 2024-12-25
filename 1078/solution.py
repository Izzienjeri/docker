

from typing import List

def can_transform(arrayOne, arrayTwo):
 
    n = len(arrayOne)
    diff = [arrayTwo[i] - arrayOne[i] for i in range(n)]

    for a in range(n):
        for b in range(a, n):
            value = 0
            if a < b:
                value = diff[a] if diff[a] == diff[b] else 0
            elif a == b and diff[a] >=0:
                value = diff[a]

            temp_arrayOne = arrayOne[:]
            for i in range(a, b + 1):
                temp_arrayOne[i] += value

            if temp_arrayOne == arrayTwo:
                return f"YES {value}"

    common_elements = set(arrayOne) & set(arrayTwo)
    return f"NO {len(common_elements)}"
