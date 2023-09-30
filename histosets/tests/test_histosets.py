import unittest
from histosets.histogram import Histogram


class TestHistogram(unittest.TestCase):

    def test_invalid_intervals(self):
        # Test if invalid intervals are flagged in the Histogram definition
        invalid_intervals = [(5, 3), (10, 5)]  # Intervals with start > end
        with self.assertRaises(ValueError):
            histogram = Histogram(invalid_intervals)

    def test_overlapping_intervals(self):
        # Test if overlapping intervals are flagged in the Histogram definition
        overlapping_intervals = [(3, 5), (4, 6)]  # Overlapping intervals
        with self.assertRaises(ValueError):
            histogram = Histogram(overlapping_intervals)

if __name__ == '__main__':
    unittest.main()
