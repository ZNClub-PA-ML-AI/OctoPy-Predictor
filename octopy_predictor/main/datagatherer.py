
import pandas as pd
from io import StringIO
from collections import namedtuple

from util import logit
import util

class DataGatherer(object):
    """docstring for DataGatherer"""
    def __init__(self, arg = None):
        super(DataGatherer, self).__init__()
        self.arg = arg

    @logit
    @staticmethod
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
    @staticmethod
    def _determine_resource(path):
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
            file_type = path[file_extension_index + 1 :]
        finally:
            FileResource = namedtuple('FileResource', 'resource_type file_type')
            return FileResource(resource_type = resource_type, file_type = file_type)
    
    
    @logit
    @staticmethod
    def _read_from_path(path):
        '''
        read data from a file available at given path
        '''
        df = pd.DataFrame()
        metadata = _determine_resource(path)
        
        if metadata.resource_type == 'local':
            
            if metadata.file_type == 'csv':
                df = pd.read_csv(path)
            
        elif metadata.resource_type == 'web':
            
            if metadata.file_type == 'csv':
                df = pd.read_csv(path)
        
        return df
                
    @logit
    def read(self, path = None, file = None):
        '''
        read receives either path or file. If received both, file is given priority
        '''
        try:            
            df = None
            if path is None:
                file_content = self._read_from_file(file)
                util.debug_store['StringIO(file_content) at datagatherer'] = StringIO(file_content)                
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
            util.debug_store['df at datagatherer'] = df.to_json(orient='columns')
            return df
