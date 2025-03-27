import glob
import unittest
import cv2
import cv2.aruco as aruco
import os
import shutil
from solution import generate_aruco_marker  # Assuming ResponseA.py contains your function

class TestGenerateArucoMarker(unittest.TestCase):

    def setUp(self):
        self.output_folder = "test_aruco_markers"

    def tearDown(self):
        if os.path.exists(self.output_folder):
            shutil.rmtree(self.output_folder)

    def get_first_file_in_folder(self, folder_path):
        """Helper function to get the first file in a folder."""
        files = glob.glob(os.path.join(folder_path, '*'))
        files = [f for f in files if os.path.isfile(f)]  # Filter out directories
        if files:
            return files[0]
        else:
            return None

    def test_generate_aruco_marker(self):
        marker_id = 1
        dictionary_id = aruco.DICT_4X4_50
        marker_size = 200

        # Generate the marker (should not raise an exception)
        generate_aruco_marker(marker_id, dictionary_id, self.output_folder, marker_size)

        # Get the first file in the output folder
        first_file = self.get_first_file_in_folder(self.output_folder)

        self.assertTrue(os.path.exists(first_file))

        # Check if the generated image has the correct dimensions
        img = cv2.imread(first_file)
        self.assertEqual(img.shape, (marker_size, marker_size, 3))

    def test_invalid_dictionary_id(self):
        marker_id = 1
        dictionary_id = -1  # Invalid dictionary ID
        marker_size = 200

        with self.assertRaises(TypeError):  # Expect a TypeError
            generate_aruco_marker(marker_id, dictionary_id, self.output_folder, marker_size)
        # Folder should be empty
        self.assertEqual(len(os.listdir(self.output_folder)), 0)

    def test_invalid_marker_id(self):
        marker_id = -1  # Invalid marker ID
        dictionary_id = aruco.DICT_4X4_50
        marker_size = 200

        with self.assertRaises(ValueError):  # Expect a ValueError
            generate_aruco_marker(marker_id, dictionary_id, self.output_folder, marker_size)
        # Folder should be empty
        self.assertEqual(len(os.listdir(self.output_folder)), 0)

    def test_invalid_output_folder(self):
        marker_id = 1
        dictionary_id = aruco.DICT_4X4_50
        marker_size = 200
        invalid_output_folder = ""  # Invalid output folder

        with self.assertRaises(ValueError):  # Expect a ValueError
            generate_aruco_marker(marker_id, dictionary_id, invalid_output_folder, marker_size)

    def test_invalid_marker_size(self):
        marker_id = 1
        dictionary_id = aruco.DICT_4X4_50
        marker_size = -200  # Invalid marker size

        with self.assertRaises(ValueError):  # Expect a ValueError
            generate_aruco_marker(marker_id, dictionary_id, self.output_folder, marker_size)
        # Folder should be empty
        self.assertEqual(len(os.listdir(self.output_folder)), 0)

    def test_correct_return_type(self):
        marker_id = 1
        dictionary_id = aruco.DICT_4X4_50
        marker_size = 200

        # Should not raise an exception
        result = generate_aruco_marker(marker_id, dictionary_id, self.output_folder, marker_size)
        self.assertIsNone(result)  # Should return None

    def test_populated_output_folder(self):
        marker_id = 1
        dictionary_id = aruco.DICT_4X4_50
        marker_size = 200

        # Should not raise an exception
        generate_aruco_marker(marker_id, dictionary_id, self.output_folder, marker_size)
        first_file = self.get_first_file_in_folder(self.output_folder)

        self.assertTrue(os.path.exists(self.output_folder))
        self.assertTrue(len(os.listdir(self.output_folder)) > 0)  # Folder should not be empty
        self.assertTrue(os.path.exists(first_file))

if __name__ == '__main__':
    unittest.main()