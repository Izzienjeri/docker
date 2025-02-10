import unittest

from solution import *


class TestDiceRollSimulation(unittest.TestCase):

    def test_simulate_dice_rolls_basic(self):
        # 1: `simulate_dice_rolls`: Basic Simulation
        A = {2, 4, 6}
        B = {1, 2, 3, 4}
        sides = 6
        num_trials = 1000
        freq_A, freq_B, freq_A_intersect_B = simulate_dice_rolls(A, B, sides, num_trials)
        self.assertAlmostEqual(freq_A, 0.5, delta=0.1)
        self.assertAlmostEqual(freq_B, 0.666, delta=0.1)
        self.assertAlmostEqual(freq_A_intersect_B, 0.333, delta=0.1)

    def test_simulate_dice_rolls_large_trials(self):
        # 2: `simulate_dice_rolls`: Large Number of Trials
        A = {2, 4, 6}
        B = {1, 2, 3, 4}
        sides = 6
        num_trials = 100000
        freq_A, freq_B, freq_A_intersect_B = simulate_dice_rolls(A, B, sides, num_trials)
        self.assertAlmostEqual(freq_A, 0.5, delta=0.05)
        self.assertAlmostEqual(freq_B, 0.666, delta=0.05)
        self.assertAlmostEqual(freq_A_intersect_B, 0.333, delta=0.05)

    def test_simulate_dice_rolls_different_sides(self):
        # 3: `simulate_dice_rolls`: Different Number of Sides
        A = {1, 3, 5}
        B = {2, 4, 6}
        sides = 8
        num_trials = 1000
        freq_A, freq_B, freq_A_intersect_B = simulate_dice_rolls(A, B, sides, num_trials)
        self.assertAlmostEqual(freq_A, 0.375, delta=0.1)
        self.assertAlmostEqual(freq_B, 0.375, delta=0.1)
        self.assertEqual(freq_A_intersect_B, 0.0)

    def test_simulate_dice_rolls_empty_set(self):
        # 4: `simulate_dice_rolls`: Empty Set for A or B
        A = set()
        B = {1, 2, 3}
        sides = 6
        num_trials = 1000
        freq_A, freq_B, freq_A_intersect_B = simulate_dice_rolls(A, B, sides, num_trials)
        self.assertEqual(freq_A, 0.0)
        self.assertAlmostEqual(freq_B, 0.5, delta=0.1)
        self.assertEqual(freq_A_intersect_B, 0.0)

    def test_simulate_dice_rolls_same_set(self):
        # 5: `simulate_dice_rolls`: A and B are the same set
        A = {1, 2}
        B = {1, 2}
        sides = 4
        num_trials = 1000
        freq_A, freq_B, freq_A_intersect_B = simulate_dice_rolls(A, B, sides, num_trials)
        self.assertAlmostEqual(freq_A, 0.5, delta=0.1)
        self.assertAlmostEqual(freq_B, 0.5, delta=0.1)
        self.assertAlmostEqual(freq_A_intersect_B, 0.5, delta=0.1)

    def test_theoretical_probability_basic(self):
        # 6: `theoretical_probability`: Basic Probabilities
        A = {2, 4, 6}
        B = {1, 2, 3, 4}
        sides = 6
        prob_A, prob_B, prob_A_intersect_B = theoretical_probability(A, B, sides)
        self.assertEqual(prob_A, 0.5)
        self.assertEqual(prob_B, 0.6666666666666666)
        self.assertEqual(prob_A_intersect_B, 0.3333333333333333)

    def test_theoretical_probability_empty_set(self):
        # 7: `theoretical_probability`: Empty Set
        A = set()
        B = {1, 2, 3}
        sides = 6
        prob_A, prob_B, prob_A_intersect_B = theoretical_probability(A, B, sides)
        self.assertEqual(prob_A, 0.0)
        self.assertEqual(prob_B, 0.5)
        self.assertEqual(prob_A_intersect_B, 0.0)

    def test_theoretical_probability_all_outcomes(self):
        # 8: `theoretical_probability`: All Possible Outcomes
        A = {1, 2, 3, 4, 5, 6}
        B = {1, 2, 3, 4, 5, 6, 7, 8}
        sides = 8
        prob_A, prob_B, prob_A_intersect_B = theoretical_probability(A, B, sides)
        self.assertEqual(prob_A, 0.75)
        self.assertEqual(prob_B, 1.0)
        self.assertEqual(prob_A_intersect_B, 0.75)

    def test_are_events_independent_independent(self):
        # 9: `are_events_independent`: Independent Events
        freq_A = 0.5
        freq_B = 0.6
        freq_A_intersect_B = 0.3
        self.assertTrue(are_events_independent(freq_A, freq_B, freq_A_intersect_B))

    def test_are_events_independent_dependent(self):
        # 10: `are_events_independent`: Dependent Events
        freq_A = 0.5
        freq_B = 0.6
        freq_A_intersect_B = 0.4
        self.assertFalse(are_events_independent(freq_A, freq_B, freq_A_intersect_B))

    def test_are_events_independent_tolerance(self):
        # 11: `are_events_independent`: Tolerance Test
        freq_A = 0.5
        freq_B = 0.6
        freq_A_intersect_B = 0.31
        tolerance = 0.05
        self.assertTrue(are_events_independent(freq_A, freq_B, freq_A_intersect_B, tolerance))

    def test_are_events_independent_zero_probability(self):
        # 12: `are_events_independent`: Zero Probability
        freq_A = 0.0
        freq_B = 0.5
        freq_A_intersect_B = 0.0
        self.assertTrue(are_events_independent(freq_A, freq_B, freq_A_intersect_B))

    def test_theoretical_independence_check(self):
        # 13: Theoretical Independence Check
        A = {2, 4, 6}
        B = {1, 2, 3, 4}
        sides = 6
        prob_A, prob_B, prob_A_intersect_B = theoretical_probability(A, B, sides)
        self.assertTrue(are_events_independent(prob_A, prob_B, prob_A_intersect_B))


if __name__ == '__main__':
    unittest.main()
