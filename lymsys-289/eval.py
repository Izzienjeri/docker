import unittest
from solution import con
class Test(unittest.TestCase):
    def test_hex_to_decimal(self):
        self.assertEqual(convert_hex_to_required('0xa', 'decimal'), '10')
        self.assertEqual(convert_hex_to_required('0x1f', 'decimal'), '31')

    def test_hex_to_binary(self):
        self.assertEqual(convert_hex_to_required('0xa', 'binary'), '1010')
        self.assertEqual(convert_hex_to_required('0x1f', 'binary'), '11111')

    def test_hex_to_octal(self):
        self.assertEqual(convert_hex_to_required('0xa', 'octal'), '12')
        self.assertEqual(convert_hex_to_required('0x1f', 'octal'), '37')

    def test_invalid_hex_input(self):
        with self.assertRaises(ValueError):
            convert_hex_to_required('0xz', 'decimal')

    def test_invalid_conversion_type(self):
        with self.assertRaises(ValueError):
            convert_hex_to_required('0xa', 'invalid')

    def test_uppercase_hex(self):
      self.assertEqual(convert_hex_to_required('0xA', 'decimal'), '10')
      self.assertEqual(convert_hex_to_required('0xA', 'binary'), '1010')
      self.assertEqual(convert_hex_to_required('0xA', 'octal'), '12')

    def test_without_prefix(self):
      self.assertEqual(convert_hex_to_required('a', 'decimal'), '10')
      self.assertEqual(convert_hex_to_required('A', 'decimal'), '10')
      self.assertEqual(convert_hex_to_required('1f', 'decimal'), '31')
      self.assertEqual(convert_hex_to_required('a', 'binary'), '1010')
      self.assertEqual(convert_hex_to_required('1f', 'binary'), '11111')
      self.assertEqual(convert_hex_to_required('a', 'octal'), '12')
      self.assertEqual(convert_hex_to_required('1f', 'octal'), '37')