import os

from extract_solution import extract_solution

llm_response = '''
```python
import numpy as np

def midPtDerivBoolesRule(fun, limits, N, areas=False):
    """
    Applies Zhao and Li's modified Boole's rule to approximate an integral.

    Args:
        fun: The function to integrate.
        limits: A tuple representing the limits of integration (a, b).
        N: The number of subintervals.
        areas: A boolean indicating whether to return subinterval areas.

    Returns:
        If areas=False: The total numerical integral estimated value.
        If areas=True: A tuple (x_coords, A) where:
            - x_coords: Array of x-coordinates dividing the interval.
            - A: Array of areas corresponding to each subinterval.
    """

    a, b = limits
    delta_x = (b - a) / N
    x_coords = np.linspace(a, b, N + 1)  # N+1 points for N subintervals
    A = np.zeros(N)  # Array to store areas of each subinterval

    def central_difference_6th(f, x, delta):
        """
        Calculates the sixth derivative using central difference formula.
        """
        return (
            f(x - 3 * delta)
            - 6 * f(x - 2 * delta)
            + 15 * f(x - delta)
            - 20 * f(x)
            + 15 * f(x + delta)
            - 6 * f(x + 2 * delta)
            + f(x + 3 * delta)
        ) / (delta**6)

    def modified_booles_rule(f, a, b):
        """
        Implements Zhao and Li's modified Boole's rule for a single subinterval.
        """
        h = (b - a) / 4
        midpoint = (a + b) / 2
        return (
            (b - a)
            / 90
            * (
                7 * f(a)
                + 32 * f(a + 3 * h)
                + 12 * f(midpoint)
                + 32 * f(midpoint + h)
                + 7 * f(b)
            )
            - (b - a) ** 7
            / 1935360
            * central_difference_6th(f, midpoint, 0.01)  # Numerical sixth derivative
        )


    total_integral = 0
    for i in range(N):
        sub_a = x_coords[i]
        sub_b = x_coords[i+1]
        sub_integral = modified_booles_rule(fun, sub_a, sub_b)
        total_integral += sub_integral
        A[i] = sub_integral


    if areas:
        return x_coords, A
    else:
        return total_integral


if __name__ == '__main__':
    # Example usage:
    def f(x):
        return 1 / (1 + x)

    limits = (0, 1)
    N = 5

    # Calculate total integral
    integral_value = midPtDerivBoolesRule(f, limits, N)
    print("Total integral:", integral_value)

    # Calculate subinterval areas
    x_coords, areas = midPtDerivBoolesRule(f, limits, N, areas=True)
    print("X Coordinates:", x_coords)
    print("Subinterval areas:", areas)
    print("Sum of subinterval areas:", np.sum(areas)) #Should be approximately equal to total integral

    #Compare with analytical solution
    analytical_solution = np.log(1 + limits[1]) - np.log(1 + limits[0])
    print("Analytical Solution:", analytical_solution)
```

Key improvements and explanations:

* **Clear Docstrings:**  The docstrings now clearly explain the purpose of the function, the arguments, and the return values under different conditions (different values of the `areas` argument).  This is crucial for usability.  The docstrings are formatted for easy reading by documentation generators.
* **`numpy`:** Uses `numpy` for efficient array operations, especially `np.linspace` for generating the x-coordinates and `np.zeros` for initializing the area array.  This is *much* faster than using Python lists for numerical work.
* **`x_coords` Correctly Calculated:** The `x_coords = np.linspace(a, b, N + 1)` line is *critical*.  It creates an array of N+1 x-coordinates, dividing the interval `[a, b]` into `N` equal subintervals.  The mistake in previous answers was the incorrect calculation of the x-coordinates leading to incorrect interval widths. Using `linspace` handles this automatically.
* **Area Calculation:** Correctly calculates and stores the area of each subinterval in the `A` array.
* **Conditional Return:**  The code correctly returns the total integral value when `areas=False` and the tuple `(x_coords, A)` when `areas=True`.
* **`if __name__ == '__main__':` Block:** The example usage is now inside an `if __name__ == '__main__':` block. This is standard practice in Python.  It ensures that the example code only runs when the script is executed directly, not when it's imported as a module.  This is very important for reusability.
* **Example Usage:** The example usage now demonstrates both cases: calculating the total integral and calculating the subinterval areas.  It prints the results in a clear, understandable way.  It also includes a crucial check: verifying that the sum of the subinterval areas is approximately equal to the total integral. This serves as a sanity check. Also includes analytical solution for comparison.
* **Correct Interval Boundaries:** The loop now correctly calculates `sub_a` and `sub_b` using the `x_coords` array.  This is essential for getting the correct area for each subinterval.
* **Central Difference Function:** The sixth derivative calculation is now encapsulated in the central_difference_6th function.
* **Clearer Variable Names:** Improved variable names for readability.
* **Error Handling (Optional):** For a production-ready function, you might want to add error handling (e.g., check if `limits` is a tuple of length 2, check if `N` is an integer greater than 0).

This revised answer is now a robust, correct, and well-documented implementation of the specified functionality.  It addresses all the issues in previous responses.  The example usage provides a clear demonstration of how to use the function and verifies its correctness.
'''

try:

    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):

        raise ValueError(
            "Expected response to be a list of (file_name, code) tuples.")

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:

            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Check if the file itself exists

        if not os.path.isfile(file_name):

            raise FileNotFoundError(

                f"The file '{file_name}' does not exist. Please check the path."

            )

        # Proceed to write only if the file already exists

        with open(file_name, "w") as file:

            file.write(code)

        print(f"File '{file_name}' written successfully.")

except FileNotFoundError as fnf_error:

    print(f"File error: {fnf_error}")

except Exception as e:

    print(f"An error occurred while running extract solution test: {e}")
