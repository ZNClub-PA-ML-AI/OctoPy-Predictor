'''
DataGatherer Component: responsible to read data from resource
and return a pandas DataFrame
'''
import pandas as pd
from io import StringIO
from collections import namedtuple
import sqlite3


# TODO
# from util import logit
# import util


# CONSTANTS

FILE = 'FILE'
SQL = 'SQL'
FILE_PATH = 'FILEPATH'
CONNECTION = 'CONN'
QUERY = 'SQL'
QUERY_PARAMERTERS = 'SQLPARAMS'


class DataGathererInput(object):

    """
    DataGathererInput

    Usage
    ----------
    DataGatherer

    """
    FILE_CONSTRAINTS = [FILE_PATH]
    SQL_CONSTRAINTS = [CONNECTION, QUERY, QUERY_PARAMERTERS]

    CONSTRAINTS = {
        FILE: FILE_CONSTRAINTS,
        SQL: SQL_CONSTRAINTS
    }

    def __init__(self, type: str):
        """


        Parameters
        ----------
        type : str
            TYPE of DataGatherer.

        Returns
        -------
        None.

        """
        if type not in DataGathererInput.CONSTRAINTS.keys():
            pass
            # TODO Throw error
        self.type = type
        self.values = {}

    def add(self, key: str, value):
        """


        Parameters
        ----------
        key : str
            valid keys present in CONSTRAINTS _values.
        value : any
            value corresponding to key.

        Returns
        -------
        None.

        """

        if key in DataGathererInput.CONSTRAINTS[self.type]:
            self.values[key] = value


class DataGatherer(object):
    """docstring for DataGatherer
    DataGatherer is responsible to fetch data from multiple sources
    and convert it to a specific type using provided Adapters

    The defaul Adapter is DataFrame
    """

    def __init__(self, arg=None):
        super(DataGatherer, self).__init__()
        self.arg = arg

    # @logit
    @staticmethod
    def _read_from_file(file):
        _file_content = None
        try:
            _file_content = file.read()
            # util.debug_store['file_content'] = _file_content
        except IOError as io_error:
            # util.debug_store['io_error'] = io_error.__traceback__
            raise io_error
        else:
            return _file_content

    # @logit
    @staticmethod
    def determine_resource(path):
        resource_type, file_type = None, None

        # resource type
        resource_type = 'web' if path.startswith('http') else 'local'

        # file type
        try:
            file_extension_index = path.rindex('.')
        except ValueError as val_error:
            # TODO: message = invalid path
            raise val_error
        else:
            file_type = path[file_extension_index + 1:]
        finally:
            FileResource = namedtuple('FileResource',
                                      'resource_type file_type')
            return FileResource(resource_type=resource_type,
                                file_type=file_type)

    # @logit
    @staticmethod
    def _read_from_path(path):
        '''
        read data from a file available at given path
        '''
        df = pd.DataFrame()
        metadata = DataGatherer.determine_resource(path)

        if metadata.resource_type == 'local':

            if metadata.file_type == 'csv':
                df = pd.read_csv(path)

        elif metadata.resource_type == 'web':

            if metadata.file_type == 'csv':
                df = pd.read_csv(path)

        return df

    # @logit
    def read(self, path=None, file=None, sql=None):
        '''
        read receives either path or file.
        If received both, file is given priority
        '''
        try:
            df = None
            if path is None:
                file_content = self._read_from_file(file)
                # util.debug_store['S'] = StringIO(file_content)
                df = pd.read_csv(StringIO(file_content))
            elif file is None:
                df = pd.read_csv(path)
            else:
                raise ValueError
        except ValueError as value_error:
            print('Missing input data. Please submit valid input')
            raise value_error
        except Exception as exception:
            print('Exception occured while loading data')
            raise exception
        finally:
            # util.debug_store['df'] = df.to_json(orient='columns')
            return df

    def read_sql(self, gatherer_input: DataGathererInput):
        """


        Parameters
        ----------
        input : DataGathererInput

        Contains _values required to execute SQL QUERY.

        Returns
        -------
        df : DataFrame
        Result of SQL QUERY.

        """
        df = pd.DataFrame()
        # TODO Move all connections to application start-up
        conn = sqlite3.connect(gatherer_input.values[CONNECTION])
        df = pd.read_sql_query(gatherer_input.values[QUERY], con=conn)
        return df
