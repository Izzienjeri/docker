import unittest
import os
from unittest.mock import patch
from io import StringIO
from solution import save_message_to_file

class Test(unittest.TestCase):
    @patch('builtins.input', side_effect=['This is a test message.', 'test_message.txt'])
    def test_save_message_to_file_new_file(self, mock_input):
        save_message_to_file()
        self.assertTrue(os.path.exists('test_message.txt'))
        with open('test_message.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'This is a test message.')
        os.remove('test_message.txt')

    @patch('builtins.input', side_effect=['Overwriting message.', 'test_overwrite.txt'])
    def test_save_message_to_file_overwrite(self, mock_input):
        with open('test_overwrite.txt', 'w') as f:
            f.write('Original message.')
        save_message_to_file()
        self.assertTrue(os.path.exists('test_overwrite.txt'))
        with open('test_overwrite.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'Overwriting message.')
        os.remove('test_overwrite.txt')

    @patch('builtins.input', side_effect=['Message with special chars.', 'file with spaces.txt'])
    def test_save_message_to_file_invalid_filename(self, mock_input):
        save_message_to_file()
        self.assertTrue(os.path.exists('file with spaces.txt'))
        with open('file with spaces.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'Message with special chars.')
        os.remove('file with spaces.txt')

    @patch('builtins.input', side_effect=['', 'empty_message.txt'])
    def test_save_message_to_file_empty_message(self, mock_input):
      save_message_to_file()
      self.assertTrue(os.path.exists('empty_message.txt'))
      with open('empty_message.txt', 'r') as f:
          content = f.read()
      self.assertEqual(content, '')
      os.remove('empty_message.txt')

    @patch('builtins.input', side_effect=['Some message.', ''])
    @patch('sys.stdout', new_callable=StringIO)
    def test_save_message_to_file_empty_filename(self, mock_stdout, mock_input):
        save_message_to_file()
        self.assertFalse(os.path.exists(''))
        self.assertTrue(mock_stdout.getvalue().startswith('Error saving message to file:'))