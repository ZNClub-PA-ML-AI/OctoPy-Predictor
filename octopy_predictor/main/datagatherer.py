
import pandas as pd
import StringIO

class DataGatherer(object):
    """docstring for DataGatherer"""
    def __init__(self, arg):
        super(DataGatherer, self).__init__()
        self.arg = arg

	def _read_from_file(file):
		with open(file, 'r') as file_pointer:
			_file_content = file_pointer.read()
			return _file_content

    def read(self, path = None, file = None):
    	try:	
	    	df = None
	    	if file is None:
	        	df = pd.read_csv(path)
	        elif path is None:
	        	file_content = _read_from_file(file)
				df = pd.read_csv(StringIO(data))
			else:
				raise ValueError
		except ValueError as value_error:
			print('Missing input data. Please submit valid input')
			raise e
		except Exception as exception:
			print('Exception occured while loading data')
		finally:
			return df
