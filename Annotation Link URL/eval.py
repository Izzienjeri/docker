"""Test suite for tokenize_and_align_labels function."""
import unittest
from solution import tokenize_and_align_labels


class TestTokenizeAndAlignLabels(unittest.TestCase):
    """Test tokenization and label alignment functionality."""

    def test_word_index_exceeding_label_length(self):
        """Verify handling of word_idx exceeding label length."""
        texts = [["This", "is", "a", "very", "long",
                  "sentence", "that", "will", "be", "tokenized"]]
        labels = [[1, 2, 3, 4, 5]]  # Intentionally short labels
        original_length = len(labels[0])
        result = tokenize_and_align_labels(texts, labels)
        self.assertGreater(len(result['labels'][0]), original_length)
        self.assertTrue(all(label in [-100, 1, 2, 3, 4, 5]
                            for label in result['labels'][0]))

    def test_simple_alignment(self):
        """Verify basic text and label alignment works."""
        result = tokenize_and_align_labels([["hello", "world"]], [[0, 1]])
        self.assertIn('labels', result)
        self.assertTrue(
            all(label in [-100, 0, 1] for label in result['labels'][0]))

    def test_empty_input(self):
        """Verify empty input handling."""
        result = tokenize_and_align_labels([[]], [[]])
        self.assertIn('labels', result)
        self.assertTrue(
            all(label == -100 for label in result['labels'][0]))

    def test_exceeding_max_length(self):
        """Verify truncation of long sequences."""
        max_length = 512
        result = tokenize_and_align_labels(
            [["word"] * 600], [[0] * 600], max_length)
        self.assertEqual(len(result['labels'][0]), max_length)

    def test_subword_handling(self):
        """Verify subword token handling for single and multiple words."""
        # Single word with subwords
        result1 = tokenize_and_align_labels([["unbelievable"]], [[1]])
        # Find first non-special token label
        labels = result1['labels'][0]
        non_special_label = next(label for label in labels if label != -100)
        self.assertEqual(non_special_label, 1)
        # Only verify that we have some -100s for subword tokens
        self.assertTrue(
            any(label == -100 for label in result1['labels'][0]))

        # Multiple words with subwords
        result2 = tokenize_and_align_labels(
            [["preprocessing", "reestablishing"]], [[1, 2]])
        self.assertTrue(
            all(label in [-100, 1, 2] for label in result2['labels'][0]))

    def test_special_tokens(self):
        """Verify special token handling."""
        result = tokenize_and_align_labels(
            [["[CLS]", "hello", "[SEP]"]], [[0, 1, 0]])
        self.assertTrue(
            all(label in [-100, 0, 1] for label in result['labels'][0]))

    def test_multiple_sequences_with_padding(self):
        """Verify handling of multiple sequences with different lengths."""
        texts = [
            ["short"],
            ["very", "long", "sequence", "needs", "padding"]
        ]
        labels = [[0], [1, 1, 1, 1, 1]]
        result = tokenize_and_align_labels(texts, labels)
        self.assertEqual(len(result['labels']), 2)
        self.assertEqual(len(result['labels'][0]), len(result['labels'][1]))

    def test_maximum_context(self):
        """Verify handling of maximum context window."""
        max_length = 512
        result = tokenize_and_align_labels(
            [["word"] * 512], [[0] * 512], max_length
        )
        self.assertEqual(len(result['labels'][0]), max_length)

    def test_mismatched_inputs(self):
        """Verify handling of mismatched texts and labels."""
        result = tokenize_and_align_labels([["hello", "world"]], [[0]])
        self.assertTrue(
            all(label in [-100, 0] for label in result['labels'][0]))

    def test_invalid_input_types(self):
        """Verify proper error handling for invalid inputs."""
        with self.assertRaises(Exception):
            tokenize_and_align_labels("not a list", None)


if __name__ == '__main__':
    unittest.main()
