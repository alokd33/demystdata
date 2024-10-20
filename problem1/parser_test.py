import unittest
from parser import split_line_into_segments


class TestSegmentSplitting(unittest.TestCase):

    def test_basic_split(self):
        line = "unit test 1234"
        offsets = [4, 9, 14]
        expected = ['unit', 'test 123', '4']
        self.assertEqual(split_line_into_segments(line, offsets), expected)

    def test_split_with_trailing_space(self):
        line = "unit test 1234   "
        offsets = [4, 3, 2, 5]
        expected = ['unit', 'te', 'st', '1234']
        self.assertEqual(split_line_into_segments(line, offsets), expected)

    def test_split_with_varied_length(self):
        line = "123456789"
        offsets = [4, 6, 9]
        expected = ['1234', '56789', '_']
        self.assertEqual(split_line_into_segments(line, offsets), expected)


if __name__ == '__main__':
    unittest.main()
