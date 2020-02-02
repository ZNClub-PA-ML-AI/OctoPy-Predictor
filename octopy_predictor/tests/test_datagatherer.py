# -*- coding: utf-8 -*-

import unittest
import sqlite3

from octopy_predictor.src.datagatherer import *

def _create_test_connection():
    conn = sqlite3.connect(':memory:')
    
    #TODO create test dataframes and corresponding tables in sqliter3
    

class DataGathererTest(unittest.TestCase):
    """Test cases for DataGatherer"""

    def setUp(self):
        self.gatherer = DataGatherer()    
    
    def test_determine_resource(self):
        """
        TBD
        """
        self.assertTrue(1==1)
        
class DataGathererInputTest(unittest.TestCase):
    """Test cases for DataGathererInput"""

    def setUp(self):
        self.input = DataGathererInput()    
    
    def test_SQL_inputs(self):
        """
        given: input is SQL 
        when: DataGathererInput is created
        then: all parameters required for SQL datagatherer should be available
        """
        conn = _create_test_connection()
        expected = {
            'type': SQL,
            CONNECTION: conn
        }
        
        input = DataGathererInput(SQL)
        input.add(CONNECTION, conn)

        self.assertIsNotNone(input.values)
        self.assertEqual(input.values[CONNECTION], expected[CONNECTION], "expected does not match actual")

if __name__ == '__main__': 
    # unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(DataGathererTest)
    unittest.TextTestRunner().run(suite)
