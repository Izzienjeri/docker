# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:38:14 2025

@author: wolfk
"""
import unittest
import numpy as np
from solution import data_reconstructor, blk

class TestDataReconstructor(unittest.TestCase):

    def setUp(self):
        self.block = data_reconstructor()

    def test_basic_data_reconstruction(self):
        # Test Case 1
        ch1_output = np.array([2, 4, 6], dtype=np.uint8)
        ch2_output = np.array([1, 3, 5], dtype=np.uint8)
        expected_output = np.array([2, 1, 4, 3, 6, 5], dtype=np.uint8)
        output_items = [np.zeros(len(expected_output), dtype=np.uint8)]
        
        self.block.work([ch1_output, ch2_output], output_items)
        self.assertTrue(np.array_equal(output_items[0], expected_output))

    def test_unequal_input_lengths(self):
        # Test Case 2
        ch1_output = np.array([2, 4, 6, 8], dtype=np.uint8)
        ch2_output = np.array([1, 3, 5], dtype=np.uint8)
        expected_output = np.array([2, 1, 4, 3, 6, 5, 8], dtype=np.uint8)
        output_items = [np.zeros(len(expected_output), dtype=np.uint8)]
        
        self.block.work([ch1_output, ch2_output], output_items)
        self.assertTrue(np.array_equal(output_items[0], expected_output))

    def test_empty_input_channels(self):
        # Test Case 3
        ch1_output = np.array([], dtype=np.uint8)
        ch2_output = np.array([], dtype=np.uint8)
        expected_output = np.array([], dtype=np.uint8)
        output_items = [np.zeros(len(expected_output), dtype=np.uint8)]

        self.block.work([ch1_output, ch2_output], output_items)
        self.assertTrue(np.array_equal(output_items[0], expected_output))

    def test_single_element_in_each_channel(self):
        # Test Case 4
        ch1_output = np.array([2], dtype=np.uint8)
        ch2_output = np.array([1], dtype=np.uint8)
        expected_output = np.array([2, 1], dtype=np.uint8)
        output_items = [np.zeros(len(expected_output), dtype=np.uint8)]

        self.block.work([ch1_output, ch2_output], output_items)
        self.assertTrue(np.array_equal(output_items[0], expected_output))
    
    def test_longer_odd_input(self):
        # Test Case 5
        ch1_output = np.array([2, 4, 6], dtype=np.uint8)
        ch2_output = np.array([1, 3, 5, 7], dtype=np.uint8)
        expected_output = np.array([2, 1, 4, 3, 6, 5, 7], dtype=np.uint8)
        output_items = [np.zeros(len(expected_output), dtype=np.uint8)]
       
        self.block.work([ch1_output, ch2_output], output_items)
        self.assertTrue(np.array_equal(output_items[0], expected_output))

    def test_data_splitter_to_data_reconstructor_flow(self):
        # Test Case 6 
        original_data = np.array([10, 20, 30, 40, 50, 60], dtype=np.uint8)
        expected_output = original_data

        # Create splitter (blk) and reconstructor blocks
        splitter = blk()  # Corrected to use blk
        reconstructor = data_reconstructor()

        # Prepare input and output buffers
        input_items_splitter = [original_data]
        output_items_splitter = [np.zeros(len(original_data) // 2 + (len(original_data) % 2 != 0), dtype=np.uint8),
                                 np.zeros(len(original_data) // 2, dtype=np.uint8)]

        # Run the splitter (blk)
        splitter.work(input_items_splitter, output_items_splitter)

        # Prepare input and output buffers for the reconstructor
        input_items_reconstructor = output_items_splitter
        output_items_reconstructor = [np.zeros(len(original_data), dtype=np.uint8)]

        # Run the reconstructor
        reconstructor.work(input_items_reconstructor, output_items_reconstructor)
        # Assert that the output matches the original data
        self.assertTrue(np.array_equal(output_items_reconstructor[0], expected_output))

if __name__ == '__main__':
    unittest.main()