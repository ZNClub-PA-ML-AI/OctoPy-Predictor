# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import numpy as np
from octopy_predictor.src.datagatherer import *

conn = 'file::memory:?cache=shared'


class DataGathererTest(unittest.TestCase):
    """Test cases for DataGatherer"""

    def setUp(self):
        self.gatherer = DataGatherer()

    def test_read_sql_from_empty_table(self):
        """
        Test read_sql()

        given a gatherer_input with SQL gatherer values 
        and empty in-memory database
        
        when read_sql is called
        
        then dataframe should be returned

        """
        c = sqlite3.connect(conn, uri=True)
        c.execute('drop table if exists test')
        gatherer_input = DataGathererInput(SQL)
        gatherer_input.add(QUERY, "SELECT * FROM sqlite_master")
        gatherer_input.add(CONNECTION, conn)
        gatherer = DataGatherer()
        
        df = gatherer.read_sql(gatherer_input)
        
        self.assertIsNotNone(df)
        self.assertTrue(df.empty)

    def test_read_sql_from_populated_table(self):
        """
        Test read_sql

        given a gatherer_input with SQL gatherer values 
        and empty in-memory database
        
        when read_sql is called
        
        then dataframe should be returned

        """
        #%%
        expected_df = pd.DataFrame(np.reshape(np.arange(10), (2,5)))
        c = sqlite3.connect(conn, uri=True)
        expected_df.to_sql('test', con=c, if_exists='replace', index=False)
        #%%
        
        #%%
        gatherer_input = DataGathererInput(SQL)
        gatherer_input.add(QUERY, "SELECT * FROM test")
        gatherer_input.add(CONNECTION, conn)
        gatherer = DataGatherer()
        
        df = gatherer.read_sql(gatherer_input)
        #%%
        self.assertIsNotNone(df)
        self.assertFalse(df.empty, "df is empty")
        self.assertEqual(expected_df.shape, df.shape)


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
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(DataGathererTest)
    unittest.TextTestRunner().run(suite)
