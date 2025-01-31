import unittest
from solution import extract_entity_with_spacy, entity_unit_map

class TestExtractEntityWithSpacy(unittest.TestCase):

    def test_empty_text(self):
        """
        Test Case 1: Empty Text
        Input: ""
        Expected Output: None
        Requirements Covered: 6
        """
        self.assertIsNone(extract_entity_with_spacy("", "voltage", entity_unit_map))

    def test_no_entity(self):
        """
        Test Case 2: No Entity
        Input: "This is a test sentence."
        Expected Output: None
        Requirements Covered: 1, 6
        """
        self.assertIsNone(extract_entity_with_spacy("This is a test sentence.", "voltage", entity_unit_map))

    def test_entity_without_unit(self):
        """
        Test Case 3: Entity Without Unit
        Input: "The voltage is 220."
        Expected Output: None
        Requirements Covered: 3, 6
        """
        self.assertIsNone(extract_entity_with_spacy("The voltage is 220.", "voltage", entity_unit_map))

    def test_entity_with_invalid_unit(self):
        """
        Test Case 4: Entity With Invalid Unit
        Input: "The weight is 10 apples."
        Expected Output: None
        Requirements Covered: 3, 6
        """
        self.assertIsNone(extract_entity_with_spacy("The weight is 10 apples.", "item_weight", entity_unit_map))

    def test_valid_entity_and_unit(self):
        """
        Test Case 5: Valid Entity and Unit
        Input: "The voltage is 220 volts."
        Expected Output: "220 volt"
        Requirements Covered: 1, 2, 3, 4, 5
        """
        self.assertEqual(extract_entity_with_spacy("The voltage is 220 volts.", "voltage", entity_unit_map), "220 volt")

    def test_unit_normalization(self):
        """
        Test Case 6: Unit Normalization
        Input: "The weight is 5 kgs."
        Expected Output: "5 kilogram"
        Requirements Covered: 4, 5
        """
        self.assertEqual(extract_entity_with_spacy("The weight is 5 kgs.", "item_weight", entity_unit_map), "5 kilogram")

    def test_different_entity_name(self):
        """
        Test Case 7: Different Entity Name
        Input: "The width is 10 cm."
        Expected Output: "10 centimeter"
        Requirements Covered: 2, 3, 4, 5
        """
        self.assertEqual(extract_entity_with_spacy("The width is 10 cm.", "width", entity_unit_map), "10 centimeter")

    def test_multiple_entities(self):
        """
        Test Case 8: Multiple Entities (Returns only the first)
        Input: "Voltage is 120V and weight is 2 lbs."
        Expected Output: "120 volt"
        Requirements Covered: 1, 5
        """
        self.assertEqual(extract_entity_with_spacy("Voltage is 120V and weight is 2 lbs.", "voltage", entity_unit_map), "120 volt")

    def test_range_value(self):
        """
        Test Case 9: Handling Range Values
        Input: "Black Red Green 208-240V 16A 60Hz L1 L2 GND Black White Green"
        Expected Output: "240 volt"
        Requirements Covered: 7, 5
        """
        self.assertEqual(extract_entity_with_spacy("Black Red Green 208-240V 16A 60Hz L1 L2 GND Black White Green", "voltage", entity_unit_map), "240 volt")

    def test_numerical_token_without_unit(self):
        """
        Test Case 10: Numerical token without unit
        Input: "The product code is 12345."
        Expected Output: None
        Requirements Covered: 3, 6
        """
        self.assertIsNone(extract_entity_with_spacy("The product code is 12345.", "voltage", entity_unit_map))

if __name__ == '__main__':
    unittest.main()