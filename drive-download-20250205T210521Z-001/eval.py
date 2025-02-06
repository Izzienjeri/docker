import unittest

from solution import classify_integer


class TestClassifyInteger(unittest.TestCase):

    def test_boundary_above_100(self):
        self.assertEqual(classify_integer(101), "Greater than 100")

    def test_integer_equal_100(self):
        self.assertEqual(classify_integer(100), "Between 50 and 100")

    def test_integer_equal_50(self):
        self.assertEqual(classify_integer(50), "Between 50 and 100")

    def test_integer_between_50_and_100(self):
        self.assertEqual(classify_integer(75), "Between 50 and 100")

    def test_boundary_below_50(self):
        self.assertEqual(classify_integer(49), "Less than 50")

    def test_integer_equal_0(self):
        self.assertEqual(classify_integer(0), "Less than 50")

    def test_negative_integer(self):
        self.assertEqual(classify_integer(-10), "Less than 50")


if __name__ == '__main__':
    unittest.main()
