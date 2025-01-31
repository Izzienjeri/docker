# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 18:56:16 2025

@author: wolfk
"""

import os
from extract_solution import extract_solution

llm_response = '''
```python
class data_reconstructor(gr.sync_block):
    """Corrected Mock Data Reconstructor Block"""

    def __init__(self):
        """Initialize the block with two inputs and one output"""
        gr.sync_block.__init__(
            self,
            name='Data Reconstructor',
            in_sig=[np.uint8, np.uint8],
            out_sig=[np.uint8]
        )

    def work(self, input_items, output_items):
        """Merge two input channels into a single output channel"""
        ch1_in = input_items[0]
        ch2_in = input_items[1]
        data_out = output_items[0]

        min_len = min(len(ch1_in), len(ch2_in))
        
        # Interleave elements up to the length of the shorter input
        data_out[:min_len*2] = np.column_stack((ch1_in[:min_len], ch2_in[:min_len])).ravel()

        # Append remaining elements from the longer input
        if len(ch1_in) > min_len:
            data_out[min_len*2:len(ch1_in) + min_len] = ch1_in[min_len:]
        elif len(ch2_in) > min_len:
            data_out[min_len*2:len(ch2_in) + min_len] = ch2_in[min_len:]

        # Calculate the actual return length
        return_len = len(ch1_in) + len(ch2_in)

        # Resize the output_items[0] array to store only valid data
        output_items[0] = data_out[:return_len].copy()

        return return_len
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