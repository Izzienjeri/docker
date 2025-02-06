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
    """Data Reconstructor Block - Merges two input channels into a single output channel"""
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
        in0 = input_items[0]
        in1 = input_items[1]
        out = output_items[0]
        min_len = min(len(in0), len(in1))
        data_out = np.empty(min_len * 2, dtype=np.uint8)
        data_out[::2] = in0[:min_len]
        data_out[1::2] = in1[:min_len]
        if len(in0) > len(in1):
            data_out = np.append(data_out, in0[min_len:])
        elif len(in1) > len(in0):
            data_out = np.append(data_out, in1[min_len:])
        out[:len(data_out)] = data_out
        return len(data_out)