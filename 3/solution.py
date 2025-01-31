import spacy
from spacy.tokens import Span
nlp = spacy.load("en_core_web_lg")
unit_normalization = {
    'g': 'gram', 'gram': 'gram', 'grams': 'gram',
    'kg': 'kilogram', 'kilogram': 'kilogram', 'kgs': 'kilogram',
    'mg': 'milligram', 'milligram': 'milligram', 'ml': 'milliliter', 'liter': 'liter', 'liters': 'liter',
    'cm': 'centimeter', 'centimeter': 'centimeter', 'centimeters': 'centimeter',
    'm': 'meter', 'meter': 'meter', 'meters': 'meter',
    'mm': 'millimeter', 'millimeter': 'millimeter', 'oz': 'ounce', 'ounces': 'ounce',
    'lb': 'pound', 'pounds': 'pound',
    'v': 'volt', 'volts': 'volt',  # Added lowercase 'v'
    'w': 'watt', 'watts': 'watt'
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
def extract_entity_with_spacy(text: str, entity_name: str, entity_unit_map: dict) -> str:
    """
    Extracts entity values and units from the text using spaCy NER.
    Args:
        text: The input text.
        entity_name: The name of the entity to extract.
        entity_unit_map: A dictionary mapping entity names to valid units.
    Returns:
        A string representing the extracted entity value and unit, or None if not found.
    """
    doc = nlp(text)
    for token in doc:
        if token.like_num:
            value = token.text
            if '-' in value:  # Handle ranges
                value = value.split('-')[-1] # Get max value
            next_token = token.nbor(1) if token.i + 1 < len(doc) else None
            if next_token:
                normalized_unit = unit_normalization.get(next_token.text.lower(), next_token.text.lower())
                if normalized_unit in entity_unit_map.get(entity_name, []):
                    return f'{value} {normalized_unit}'
    return None
