# -*- coding: utf-8 -*-

import unittest
import sqlite3

from octopy_predictor.src.datagatherer import *

   
# c1 = sqlite3.connect("file::memory:?cache=shared", uri=True)   
conn = 'file::memory:?cache=shared'

class DataGathererTest(unittest.TestCase):
    """Test cases for DataGatherer"""

    def setUp(self):
        self.gatherer = DataGatherer()    
    
    def test_read_sql(self):
        """
        Test ...

 
        given: input is SQL 
        when: DataGathererInput is created
        then: all parameters required for SQL datagatherer should be available
        
        """        
 
        input = DataGathererInput(SQL)
        input.add(QUERY, "SELECT 'A1' AS A, 'B1' AS B FROM DUAL ")
        input.add(CONNECTION, )
        gatherer = DataGatherer()
        
        df = gatherer.read_sql(input)
        
        assertIsNotNone(df)

        
        

        
        
class DataGathererInputTest(unittest.TestCase):
    """Test cases for DataGathererInput"""
            
    def test_SQL_inputs(self):
        """
        given: input is SQL 
        when: DataGathererInput is created
        then: all parameters required for SQL datagatherer should be available
        """
     
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
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(DataGathererInputTest)
    unittest.TextTestRunner().run(suite)
