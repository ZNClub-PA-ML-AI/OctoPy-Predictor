# test for visualizer.py

import sys
sys.path.insert(0, '../main/')

from analyser import Analyser
import unittest
import pandas as pd
import numpy as np

class AnalyserTest(unittest.TestCase):
	"""Test cases for Analyser"""

	def setUp(self):
		self.analyser = Analyser()

	def test(self):
		self.assertTrue(True)

	def test_is_regression_model_type(self):
		expected_result = 'Regression'
		array = np.random.randint(100)

		actual_result = self.analyser.get_model_type_by_label(array.tolist())

		self.assertEquals(actual_result, expected_result)

if __name__ == '__main__': 
    # unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AnalyserTest)
    unittest.TextTestRunner().run(suite)
