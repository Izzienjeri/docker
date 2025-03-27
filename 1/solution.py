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