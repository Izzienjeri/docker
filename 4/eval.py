import unittest
import cv2
import cv2.aruco as aruco
import os
from solution import generate_aruco_marker
from pyfakefs import fake_filesystem_unittest
import glob
import numpy as np

class TestGenerateArucoMarker(fake_filesystem_unittest.TestCase):

    def setUp(self):
        
        self.setUpPyfakefs()
        self.output_folder = "test_aruco_markers"
        os.makedirs(self.output_folder)
        self.original_imwrite = cv2.imwrite
        self.original_imread = cv2.imread

        
        def fake_imwrite(filename, img):
            
            success, buffer = cv2.imencode('.png', img)
            if success:
                with open(filename, 'wb') as f:
                    f.write(buffer.tobytes())
                return True
            return False

        
        def fake_imread(filename, flags=cv2.IMREAD_COLOR):
            with open(filename, 'rb') as f:
                data = f.read()
            arr = np.frombuffer(data, dtype=np.uint8)
            return cv2.imdecode(arr, flags)

        cv2.imwrite = fake_imwrite
        cv2.imread = fake_imread

    def tearDown(self):
        cv2.imwrite = self.original_imwrite
        cv2.imread = self.original_imread

    def get_first_file_in_folder(self, folder_path):
        """Helper function to get the first file in a folder."""
        files = glob.glob(os.path.join(folder_path, '*'))
        files = [f for f in files if os.path.isfile(f)]
        return files[0] if files else None

    def test_generate_aruco_marker(self):
        marker_id = 1
        dictionary_id = aruco.DICT_4X4_50
        marker_size = 200
        generate_aruco_marker(marker_id, dictionary_id, self.output_folder, marker_size)

        first_file = self.get_first_file_in_folder(self.output_folder)
        self.assertTrue(os.path.exists(first_file))

        img = cv2.imread(first_file)
        self.assertEqual(img.shape, (marker_size, marker_size, 3))

    def test_correct_return_type(self):
        marker_id = 1
        dictionary_id = aruco.DICT_4X4_50
        marker_size = 200
        result = generate_aruco_marker(marker_id, dictionary_id, self.output_folder, marker_size)
        self.assertIsNone(result)  

    def test_populated_output_folder(self):
        marker_id = 1
        dictionary_id = aruco.DICT_4X4_50
        marker_size = 200

        generate_aruco_marker(marker_id, dictionary_id, self.output_folder, marker_size)
        first_file = self.get_first_file_in_folder(self.output_folder)

        self.assertTrue(os.path.exists(self.output_folder))
        self.assertTrue(len(os.listdir(self.output_folder)) > 0)  
        self.assertTrue(os.path.exists(first_file))

if __name__ == '__main__':
    unittest.main()


