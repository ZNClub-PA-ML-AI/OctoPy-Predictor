"""Tests for analyser.py"""

from octopy_predictor.src.analyser import Analyser, AnalyserMetricsRegistry, REGRESSION_MODEL
import unittest

class AnalyserMetricsRegistryTest(unittest.TestCase):
    """Test cases for AnalyserMetricsRegistry"""
    
    def setUp(self):
        self.registry = AnalyserMetricsRegistry()
    
    def test_regression_model(self):
        
        result = self.registry.apply_metrics(REGRESSION_MODEL,
                                    ([.0, 1.5, 3.0], [-3.0, -1.5, .0])
                                    )
        
        self.assertIsNotNone(result, "apply_metrics returned null") 

class AnalyserTest(unittest.TestCase):
	"""Test cases for Analyser"""

	def setUp(self):
		self.analyser = Analyser()	

	def test_is_regression_model_type(self):
		expected_result = 'Regression'
		array = [i for i in range(20)]

		actual_result = self.analyser.get_model_type_by_label(array)

		self.assertEqual(actual_result, expected_result, "expected does not match actual")

if __name__ == '__main__': 
    # unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AnalyserMetricsRegistryTest)
    unittest.TextTestRunner().run(suite)
