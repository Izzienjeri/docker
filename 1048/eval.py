"""Unit tests for the find_middle_person function."""

import unittest
from solution import find_middle_person


class TestFindMiddlePerson(unittest.TestCase):
    """Tests to verify the functionality of find_middle_person."""

    def test_valid_case_1(self):
        """Test where the middle person is B with all '<' signs."""
        self.assertEqual(find_middle_person("<", "<", "<"), "B")

    def test_valid_case_2(self):
        """Test where the middle person is C with signs '<', '<', '>'."""
        self.assertEqual(find_middle_person("<", "<", ">"), "C")

    def test_valid_case_3(self):
        """Test where the middle person is A with signs '<', '>', '>'."""
        self.assertEqual(find_middle_person("<", ">", ">"), "A")

    def test_valid_case_4(self):
        """Test where the middle person is A with signs '>', '<', '<'."""
        self.assertEqual(find_middle_person(">", "<", "<"), "A")

    def test_valid_case_5(self):
        """Test where the middle person is B with all '>' signs."""
        self.assertEqual(find_middle_person(">", ">", ">"), "B")

    def test_valid_case_6(self):
        """Test where the middle person is C with signs '>', '>', '<'."""
        self.assertEqual(find_middle_person(">", ">", "<"), "C")

    def test_invalid_case_1(self):
        """Test case where inputs are '<', '>', '<' leading to no middle."""
        self.assertIsNone(find_middle_person("<", ">", "<"))

    def test_invalid_case_2(self):
        """Test case where inputs are '>', '<', '>' leading to no middle."""
        self.assertIsNone(find_middle_person(">", "<", ">"))


if __name__ == '__main__':
    unittest.main()



