#all-in-one Octo-Py

class Controller(object):
	"""docstring for Controller"""
	def __init__(self, arg):
		super(Controller, self).__init__()
		self.arg = arg

class Service(object):
	"""docstring for Service"""
	def __init__(self, arg):
		super(Service, self).__init__()
		self.arg = arg

class CLIInterface(object):
	"""docstring for CLIInterface"""
	def __init__(self, arg):
		super(CLIInterface, self).__init__()
		self.arg = arg
		self.option_selected_hash = -1
	def greet(self, username):
		print('Welcome {0}. I am Octo-Py: the genius predictor'.format(username))
	def get_input_options(self):
		input_options = ["EXCEL from local","JSON from url","CSV from url"]
		print('Input options available are:\n')
		#print((i,input_options[i]) for i in range(input_options))
		for index in range(len(input_options)):
			print('Press {0} for {1}'.format(index+1, input_options[index]))

class Service(object):
	"""docstring for Service"""
	def __init__(self, arg):
		super(Service, self).__init__()
		self.arg = arg

class DataGatherer(object):
	"""docstring for DataGatherer"""
	def __init__(self, arg):
		super(DataGatherer, self).__init__()
		self.arg = arg
		
		
class Analyser(object):
	"""docstring for Analyser"""
	def __init__(self, arg):
		super(Analyser, self).__init__()
		self.arg = arg
		

class Visualizer(object):
	"""docstring for Visualizer"""
	def __init__(self, arg):
		super(Visualizer, self).__init__()
		self.arg = arg

class Model(object):
	"""docstring for Model"""
	def __init__(self, arg):
		super(Model, self).__init__()
		self.arg = arg


if __name__ == '__main__':
	username = "Nevil"
	interface = CLIInterface(None)
	interface.greet(username)
	interface.get_input_options()
	interface.option_selected_hash = input("Enter any 1 of the above options:")
	print(interface.option_selected_hash)
	#interface.load_data()