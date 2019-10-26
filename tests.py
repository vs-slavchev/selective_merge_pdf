import unittest
from selective_merge_pdf import pages_args_to_array, range_pattern, comma_pattern

class TestPageNumbersExtraction(unittest.TestCase):
	
	def test_single(self):
		self.assertEqual(pages_args_to_array("1"), [1])

	def test_multiple(self):
		self.assertEqual(pages_args_to_array("1,2,3"), [1,2,3])

	def test_range_dots(self):
		self.assertEqual(pages_args_to_array("2..5"), [2,3,4,5])

	def test_range_dash(self):
		self.assertEqual(pages_args_to_array("5-8"), [5,6,7,8])

if __name__ == '__main__':
    unittest.main()
