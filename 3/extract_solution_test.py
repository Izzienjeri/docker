import os

from extract_solution import extract_solution

llm_response = '''
```python
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
    'v': 'volt', 'volts': 'volt',  # added lowercase 'v'
    'w': 'watt', 'watts': 'watt'  # added lowercase 'w'
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
    doc = nlp(text)
    for ent in doc.ents:
        value = None
        for token in ent:
          if "-" in token.text and token.text[0].isdigit():
            value = token.text.split("-")[-1]
            break
          elif token.like_num:
            value = token.text
            
        if value:
            unit = None
            for token in ent:
                next_token = token.nbor(1) if token.i + 1 < len(doc) else None
                if next_token:
                    normalized_unit = unit_normalization.get(next_token.text.lower(), next_token.text.lower())
                    if normalized_unit in entity_unit_map.get(entity_name, []):
                        unit = normalized_unit
                        break
            if unit:
                return f'{value} {unit}'
    return None
```'''

try:

    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):

        raise ValueError("Expected response to be a list of (file_name, code) tuples.")

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:

            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Check if the file itself exists

        if not os.path.isfile(file_name):

            raise FileNotFoundError(

                f"The file '{file_name}' does not exist. Please check the path."

            )

        # Proceed to write only if the file already exists

        with open(file_name, "w") as file:

            file.write(code)

        print(f"File '{file_name}' written successfully.")

except FileNotFoundError as fnf_error:

    print(f"File error: {fnf_error}")

except Exception as e:

    print(f"An error occurred while running extract solution test: {e}")