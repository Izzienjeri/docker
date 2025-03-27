import unittest
import numpy as np
from solution import midPtDerivBoolesRule


class TestMidPtDerivBoolesRule(unittest.TestCase):

    def setUp(self):
        self.f = lambda x: 1 / (1 + x)
        self.g = lambda x: x**2
        self.h = np.sin
        self.n = 1000

    def test_case_1(self):
        result = midPtDerivBoolesRule(self.f, (0, 1), self.n)
        expected = 0.6931471805599454
        self.assertAlmostEqual(result, expected, places=3)

    def test_case_2(self):
        x_coords, areas = midPtDerivBoolesRule(
            self.f, (0, 1), self.n, areas=True)
        expected_areas_sum = 0.6931471805599454
        expected_array_length = self.n + 1
        self.assertEquals(len(x_coords), expected_array_length)
        self.assertAlmostEqual(np.sum(areas), expected_areas_sum, places=3)

    def test_case_3(self):
        result = midPtDerivBoolesRule(self.f, (1, 3), self.n)
        expected = np.log(4) - np.log(2)
        self.assertAlmostEqual(result, expected, places=3)

    def test_case_4(self):
        x_coords, areas = midPtDerivBoolesRule(
            self.f, (1, 3), self.n, areas=True)
        expected_array_length = self.n + 1
        expected_areas_sum = np.log(4) - np.log(2)
        np.testing.assert_allclose(len(x_coords), expected_array_length)
        self.assertAlmostEqual(np.sum(areas), expected_areas_sum, places=3)


if __name__ == "__main__":
    unittest.main()
