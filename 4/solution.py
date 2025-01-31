import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """Data Splitter Block - Splits input data into two channels"""
    def __init__(self):
        """Initialize the block with one input and two outputs"""
        gr.sync_block.__init__(
            self,
            name='Data Splitter',
            in_sig=[np.uint8],  
            out_sig=[np.uint8, np.uint8]
        )
    def work(self, input_items, output_items):
        """Split input data into two channels"""
        data_in = input_items[0]
        ch1_out = output_items[0]
        ch2_out = output_items[1]
        ch1_data = data_in[::2]
        ch2_data = data_in[1::2]
        ch1_out[:len(ch1_data)] = ch1_data
        ch2_out[:len(ch2_data)] = ch2_data
        return len(ch1_data)

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