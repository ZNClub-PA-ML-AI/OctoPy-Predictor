# -*- coding: utf-8 -*-

import unittest

from octopy_predictor.src.datagatherer import DataGatherer

class DataGathererTest(unittest.TestCase):
    """Test cases for Analyser"""

    def setUp(self):
        self.datagatherer = DataGatherer()    
    
    def test_determine_resource(self):
        """
        TBD
        """
        self.assertEquals(1,1)
        
    

if __name__ == '__main__': 
    # unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(DataGathererTest)
    unittest.TextTestRunner().run(suite)
