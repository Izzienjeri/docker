import unittest
from solution import parse_delimited_numbers

class Test(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(parse_delimited_numbers(""), [])

    def test_example_input(self):
        self.assertEqual(parse_delimited_numbers("3162433224558"), ["3", "6", "4", "322", "58"])

    def test_no_valid_split(self):
        self.assertEqual(parse_delimited_numbers("123456789"), [])

    def test_single_digit_numbers(self):
        self.assertEqual(parse_delimited_numbers("51223449441"), ["5", "2", "3", "49441"])

    def test_multi_digit_numbers(self):
        self.assertEqual(parse_delimited_numbers("1231456212124313"), ["123", "456", "121243"])

    def test_multi_digit_delimiter(self):
        self.assertEqual(parse_delimited_numbers("123156710789116512"), ["123", "567", "789", "65"])

    def test_delimiter_at_end(self):
        self.assertEqual(parse_delimited_numbers("12314562"), ["123", "456", ""])

    def test_long_input(self):
        self.assertEqual(parse_delimited_numbers("71529934567455888645671012345678911"), ["7", "5", "99", "4", "567", "5", "88864567", "123456789", ""])

    def test_invalid_delimiter(self):
        self.assertEqual(parse_delimited_numbers("123105679"), ["123", "05679"])