import unittest

from solution import process_string


class TestProcessString(unittest.TestCase):

    def test_basic_functionality_with_mixed_case(self):
        input_string = "Apple Zebra banana apple ant"
        target_letter = "a"
        expected_output = {"ant": [0], "apple": [1, 2]}
        self.assertEqual(expected_output, process_string(input_string, target_letter))

    def test_empty_input_string(self):
        input_string = ""
        target_letter = "a"
        expected_output = {}
        self.assertEqual(expected_output, process_string(input_string, target_letter))

    def test_no_matching_words(self):
        input_string = "Banana Cat Dog"
        target_letter = "z"
        expected_output = {}
        self.assertEqual(expected_output, process_string(input_string, target_letter))

    def test_all_words_start_with_target_letter(self):
        input_string = "apple ant apricot"
        target_letter = "a"
        expected_output = {"ant": [0], "apple": [1], "apricot": [2]}
        self.assertEqual(expected_output, process_string(input_string, target_letter))

    def test_case_insensitive_target_letter(self):
        input_string = "Apple Zebra banana apple ant"
        target_letter = "A"
        expected_output = {"ant": [0], "apple": [1, 2]}
        self.assertEqual(expected_output, process_string(input_string, target_letter))

    def test_input_string_with_multiple_spaces(self):
        input_string = "  apple   Zebra   banana  apple    ant "
        target_letter = "a"
        expected_output = {"ant": [0], "apple": [1, 2]}
        self.assertEqual(expected_output, process_string(input_string, target_letter))

    def test_single_character_input_string(self):
       input_string = "a"
       target_letter = "a"
       expected_output = {"a": [0]}
       self.assertEqual(expected_output, process_string(input_string, target_letter))

    def test_invalid_input_string_type(self):
       input_string = 123
       target_letter = "a"
       with self.assertRaises(TypeError):
         process_string(input_string, target_letter)

    def test_invalid_target_letter_type(self):
       input_string = "apple ant banana"
       target_letter = 123
       with self.assertRaises(TypeError):
         process_string(input_string, target_letter)


if __name__ == '__main__':
    unittest.main()

    