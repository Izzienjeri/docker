import unittest
from solution import color_code_manipulation

class Test(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(
            color_code_manipulation("rgbywb", 2, 0, 1), '1'
        )

    def test_invalid_index_str(self):
        self.assertEqual(
            color_code_manipulation("rgbywb", 10, 0, 1), 'Invalid'
        )

    def test_invalid_index_hex(self):
        self.assertEqual(
            color_code_manipulation("rgbywb", 2, 10, 1), 'Invalid'
        )

    def test_invalid_color_char(self):
        self.assertEqual(
            color_code_manipulation("rgxywb", 2, 0, 1), 'Invalid'
        )

    def test_valid_input_red(self):
        self.assertEqual(
            color_code_manipulation("rr", 0, 0, 1), 'G'
        )

    def test_valid_input_green(self):
        self.assertEqual(
            color_code_manipulation("gg", 0, 0, 1), '1'
        )

    def test_valid_input_yellow(self):
        self.assertEqual(
            color_code_manipulation("yy", 0, 0, 1), 'G'
        )

    def test_valid_input_white(self):
        self.assertEqual(
            color_code_manipulation("ww", 0, 0, 1), 'G'
        )

    def test_valid_input_blue(self):
        self.assertEqual(
            color_code_manipulation("bb", 0, 0, 1), '1'
        )

    def test_increment_wrap_around(self):
        self.assertEqual(
            color_code_manipulation("rgbywb", 2, 0, 256), chr(ord('0')+256)
        )

    def test_empty_color_string(self):
        self.assertEqual(
            color_code_manipulation("", 0, 0, 1), 'Invalid'
        )

    def test_negative_index_str(self):
        self.assertEqual(
            color_code_manipulation("rgbywb", -1, 0, 1), 'Invalid'
        )

    def test_negative_index_hex(self):
        self.assertEqual(
            color_code_manipulation("rgbywb", 2, -1, 1), 'Invalid'
        )

    def test_zero_increment(self):
        self.assertEqual(
            color_code_manipulation("rgbywb", 2, 0, 0), '0'
        )

    def test_large_increment(self):
        self.assertEqual(
            color_code_manipulation("rgbywb", 2, 0, 1000), chr(ord('0')+1000)
        )

    def test_negative_increment(self):
        self.assertEqual(
            color_code_manipulation("rgbywb", 2, 0, -1), '/' 
        )

    def test_multiple_invalid_params(self):
        self.assertEqual(
            color_code_manipulation("rxgbywb", 10, 0, 1), 'Invalid'
        )    