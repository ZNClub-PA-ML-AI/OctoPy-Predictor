
import pandas as pd
from io import StringIO
from util import logit
import util

class DataGatherer(object):
    """docstring for DataGatherer"""
    def __init__(self, arg):
        super(DataGatherer, self).__init__()
        self.arg = arg
    @logit
    def _read_from_file(file):
        _file_content = None
        try:
            _file_content = file.read()
            util.debug_store['file_content at datagatherer'] = _file_content
        except IOError as io_error:
            util.debug_store['io_error at datagatherer'] = io_error.__traceback__
            raise io_error
        else:
            return _file_content
    @logit
    def read(self, path = None, file = None):
        try:            
            df = None
            if file is None:
                df = pd.read_csv(path)
            elif path is None:
                file_content = self._read_from_file(file)
                util.debug_store['StringIO(file_content) at datagatherer'] = StringIO(file_content)                
                df = pd.read_csv(StringIO(file_content))
            else:
                raise ValueError
        except ValueError as value_error:
            print('Missing input data. Please submit valid input')
            raise value_error
        except Exception as exception:
            print('Exception occured while loading data')
            raise exception
        finally:
            util.debug_store['df at datagatherer'] = df.to_json(orient='columns')
            return df
