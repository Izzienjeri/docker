import spacy
from spacy.tokens import Span

# Load spaCy's pretrained model
nlp = spacy.load("en_core_web_lg")

# Update unit normalization mapping if necessary
unit_normalization = {
    'g': 'gram', 'gram': 'gram', 'grams': 'gram',
    'kg': 'kilogram', 'kilogram': 'kilogram', 'kgs': 'kilogram',
    'mg': 'milligram', 'milligram': 'milligram', 'ml': 'milliliter', 'liter': 'liter', 'liters': 'liter',
    'cm': 'centimeter', 'centimeter': 'centimeter', 'centimeters': 'centimeter',
    'm': 'meter', 'meter': 'meter', 'meters': 'meter',
    'mm': 'millimeter', 'millimeter': 'millimeter', 'oz': 'ounce', 'ounces': 'ounce',
    'lb': 'pound', 'pounds': 'pound',
    'V': 'volt', 'volts': 'volt',
    'W': 'watt', 'watts': 'watt'
}

entity_unit_map = {
    'width': {'centimeter', 'foot', 'inch', 'meter', 'millimeter', 'yard'},
    'depth': {'centimeter', 'foot', 'inch', 'meter', 'millimeter', 'yard'},
    'height': {'centimeter', 'foot', 'inch', 'meter', 'millimeter', 'yard'},
    'item_weight': {'gram', 'kilogram', 'microgram', 'milligram', 'ounce', 'pound', 'ton'},
    'maximum_weight_recommendation': {'gram', 'kilogram', 'microgram', 'milligram', 'ounce', 'pound', 'ton'},
    'voltage': {'kilovolt', 'millivolt', 'volt'},
    'wattage': {'kilowatt', 'watt'},
    'item_volume': {'centiliter', 'cubic foot', 'cubic inch', 'cup', 'deciliter', 'fluid ounce', 'gallon',
                    'imperial gallon', 'liter', 'microliter', 'milliliter', 'pint', 'quart'}
}


# Custom function for extracting values and units using spaCy
def extract_entity_with_spacy(text, entity_name, entity_unit_map):
    """
    Extracts entity values and units from the text using spaCy NER.
    """
    doc = nlp(text)

    # Store the extracted entities
    extracted_entities = []

    for ent in doc.ents:
        # Only extract the numeric part as the value
        value = ''.join([token.text for token in ent if token.like_num])

        # Look ahead in the text for any valid unit associated with this entity
        unit = None
        for token in ent:
            next_token = token.nbor(1) if token.i + 1 < len(doc) else None
            if next_token:
                # Normalize the unit before checking against entity_unit_map
                normalized_unit = unit_normalization.get(next_token.text.lower(), next_token.text.lower())

                if normalized_unit in entity_unit_map.get(entity_name, []):
                    unit = normalized_unit
                    break

        # If a valid unit is found, append to results
        if value and unit:
            extracted_entities.append(f'{value} {unit}')

    # If we found any entity values, return the largest value
    if extracted_entities:
        # Convert to numbers for comparison, handling potential errors
        def to_number(s):
            try:
                return int(s.split()[0])  # Get the numeric part and convert to int
            except ValueError:
                return 0  # Default to 0 if conversion fails

        # Sort by numeric value in descending order and return the largest
        extracted_entities.sort(key=to_number, reverse=True)
        return extracted_entities[0]

    return None

# Example usage with one row of text and entity_name
text = "Black Red Green 208-240V 16A 60Hz L1 L2 GND Black White Green"
entity_name = 'voltage'

result = extract_entity_with_spacy(text, entity_name, entity_unit_map)
print(f"Extracted entity: {result}")