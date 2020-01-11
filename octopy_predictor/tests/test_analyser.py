# test for visualizer.py

#import sys
#sys.path.insert(0, '../main/')

from octopy_predictor.src.analyser import Analyser
import unittest

class AnalyserTest(unittest.TestCase):
	"""Test cases for Analyser"""

	def setUp(self):
		self.analyser = Analyser()	

	def test_is_regression_model_type(self):
		expected_result = 'Regression'
		array = [i for i in range(20)]

		actual_result = self.analyser.get_model_type_by_label(array)

		self.assertEquals(actual_result, expected_result)

if __name__ == '__main__': 
    # unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AnalyserTest)
    unittest.TextTestRunner().run(suite)
