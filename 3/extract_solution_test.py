import os

from extract_solution import extract_solution

llm_response = r'''
```python
import numpy as np


def simulate_dice_rolls(A: set, B: set, sides: int, num_trials: int) -> tuple[float, float, float]:
    """
    Simulates rolling a fair multi-sided die for a specified number of trials.
    Calculates the frequencies of events A, B, and their intersection (A ∩ B).

    Args:
        A: The definition of A
        B: The definition of B
        sides: The number of sides on the die
        num_trials: The number of times to simulate rolling the die.

    Returns:
        A tuple containing:
        - The frequency of event A.
        - The frequency of event B.
        - The frequency of the intersection of A and B .
    """
    rolls = np.random.randint(1, sides + 1, num_trials)
    freq_A = np.sum(np.isin(rolls, list(A))) / num_trials
    freq_B = np.sum(np.isin(rolls, list(B))) / num_trials
    freq_A_intersect_B = np.sum(np.isin(rolls, list(A & B))) / num_trials
    return freq_A, freq_B, freq_A_intersect_B


def theoretical_probability(A: set, B: set, sides: int) -> tuple[float, float, float]:
    """
    Calculates the theoretical probability of event A.
    Calculates the theoretical probability of event B.
    Calculates the theoretical probability of the intersection of events A and B.

    Args:
        A: The definition of A
        B: The definition of B
        sides: The number of sides on the die

    Returns:
        The theoretical probability of event A.
        The theoretical probability of event B.
        The theoretical probability of A intersect B.
    """
    prob_A = len(A) / sides
    prob_B = len(B) / sides
    prob_A_intersect_B = len(A & B) / sides
    return prob_A, prob_B, prob_A_intersect_B


def are_events_independent(freq_A: float, freq_B: float, freq_A_intersect_B: float, tolerance: float = 0.01) -> bool:
    """
    Checks if two events are independent based on their frequencies/probabilities.

    Args:
      freq_A: The frequency/probability of event A.
      freq_B: The frequency/probability of event B.
      freq_A_intersect_B: The frequency/probability of the intersection of A and B.
      tolerance: The tolerance level for comparing frequencies/probabilities.

    Returns:
      True if the events are considered independent within the given tolerance,
      False otherwise.
    """
    return abs(freq_A * freq_B - freq_A_intersect_B) < tolerance


# Define events A and B
A = {2, 4, 6}
B = {1, 2, 3, 4}
sides = 6

# Calculate theoretical probabilities
prob_A, prob_B, prob_A_intersect_B = theoretical_probability(A, B, sides)

# Check for independence
are_independent = are_events_independent(prob_A, prob_B, prob_A_intersect_B)

# Print results
print(f"Probability of A: {prob_A}")
print(f"Probability of B: {prob_B}")
print(f"Probability of A intersect B: {prob_A_intersect_B}")
print(f"Are events A and B theoretically independent? {are_independent}")


# Simulate dice rolls (optional, for comparison)
num_trials = 10000
freq_A, freq_B, freq_A_intersect_B = simulate_dice_rolls(A, B, sides, num_trials)

# Check independence based on simulation
are_independent_sim = are_events_independent(freq_A, freq_B, freq_A_intersect_B)

#Print simulation results
print(f"\nSimulation Results (num_trials={num_trials}):")
print(f"Frequency of A: {freq_A}")
print(f"Frequency of B: {freq_B}")
print(f"Frequency of A intersect B: {freq_A_intersect_B}")
print(f"Are A and B independent based on simulation? {are_independent_sim}")
```
'''

try:

    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):
        raise ValueError("Expected response to be a list of (file_name, code) tuples.")

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
