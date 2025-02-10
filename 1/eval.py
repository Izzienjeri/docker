"""Unit tests for the get_current_time function."""

import pytest
from datetime import datetime, timezone
from unittest.mock import patch
from solution import get_current_time

# Store the module name dynamically
MODULE_NAME = get_current_time.__module__


class TestCurrentTime:
    """Test suite for the get_current_time function."""

    # Class-level constant
    MOCK_NOW = datetime(2024, 12, 23, 16, 18, 0, tzinfo=timezone.utc)

    @pytest.fixture
    def mock_datetime_now(self):
        """Fixture to mock the datetime.now() function.

        Returns a mock datetime object with a fixed time.
        """
        with patch(f"{MODULE_NAME}.datetime") as mock_datetime:
            mock_datetime.now.return_value = self.MOCK_NOW
            mock_datetime.side_effect = datetime
            yield

    def test_valid_timezone_offset_positive(self, mock_datetime_now):
        """Test get_current_time with a valid positive timezone offset (+5).

        Verifies that the function correctly adjusts time forward by 5 hours.
        """
        result = get_current_time(5)
        expected_time = "2024-12-23 21:18:00"
        assert result == expected_time

    def test_valid_timezone_offset_negative(self, mock_datetime_now):
        """Test get_current_time with a valid negative timezone offset (-8).

        Verifies that the function correctly adjusts time backward by 8 hours.
        """
        result = get_current_time(-8)
        expected_time = "2024-12-23 08:18:00"
        assert result == expected_time

    def test_invalid_timezone_offset_non_integer(self):
        """Test get_current_time with an invalid non-integer input.

        Verifies that the function raises ValueError for string input.
        """
        with pytest.raises(ValueError):
            get_current_time("5")

    def test_invalid_timezone_offset_out_of_range_below(self):
        """Test get_current_time with timezone offset below valid range (-25).

        Verifies that the function raises ValueError for offsets less than -24.
        """
        with pytest.raises(ValueError):
            get_current_time(-25)

    def test_invalid_timezone_offset_out_of_range_above(self):
        """Test get_current_time with timezone offset above valid range (+25).

        Verifies that function raises ValueError for offsets greater than +24.
        """
        with pytest.raises(ValueError):
            get_current_time(25)

    def test_valid_timezone_offset_negative_24(self, mock_datetime_now):
        """Test get_current_time with edge case timezone offset (-24).

        Verifies that the function handles the minimum valid offset correctly.
        """
        result = get_current_time(-24)
        expected_time = "2024-12-22 16:18:00"
        assert result == expected_time

    def test_valid_timezone_offset_positive_24(self, mock_datetime_now):
        """Test get_current_time with edge case timezone offset (+24).

        Verifies that the function handles the maximum valid offset correctly.
        """
        result = get_current_time(24)
        expected_time = "2024-12-24 16:18:00"
        assert result == expected_time


if __name__ == "__main__":
    pytest.main([__file__, '-v'])
