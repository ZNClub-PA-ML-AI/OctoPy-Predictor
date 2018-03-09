#all-in-one Octo-Py

import pandas as pd

class DemoInterface(object):
	"""docstring for DemoInterface"""
	def __init__(self, arg):
		super(DemoInterface, self).__init__()
		self.arg = arg
		self.option_selected_hash = -1
		self.controller = None

	def set_controller(self, controller):
		self.controller = controller

	def greet(self, username):
		print('Welcome {0}. I am Octo-Py: the genius predictor'.format(username))
	def get_input_options(self):
		input_options = ["EXCEL from local","JSON from url","CSV from url"]
		print('Input options available are:\n')
		#print((i,input_options[i]) for i in range(input_options))
		for index in range(len(input_options)):
			print('Press {0} for {1}'.format(index+1, input_options[index]))
	def load_data(self, path):
		self.controller.load_data(path)

###################################################################################################

class Controller(object):
	"""docstring for Controller"""
	def __init__(self, arg):
		super(Controller, self).__init__()
		self.arg = arg
		self.service = None

	def set_service(self, service):
		self.service = service

	def load_data(self, path):
		self.service.load_data(path)

###################################################################################################

class Service(object):
	"""docstring for Service"""
	def __init__(self, arg):
		super(Service, self).__init__()
		self.arg = arg
		self.datagatherer = None

	def set_datagatherer(self, datagatherer):
		self.datagatherer = datagatherer

	def load_data(self, path):
		df = self.datagatherer.read(path)

###################################################################################################

class DataGatherer(object):
	"""docstring for DataGatherer"""
	def __init__(self, arg):
		super(DataGatherer, self).__init__()
		self.arg = arg

	def read(self, path):
		return pd.read_csv(path)
###################################################################################################

class Analyser(object):
	"""docstring for Analyser"""
	def __init__(self, arg):
		super(Analyser, self).__init__()
		self.arg = arg
		
###################################################################################################

class Visualizer(object):
	"""docstring for Visualizer"""
	def __init__(self, arg):
		super(Visualizer, self).__init__()
		self.arg = arg

###################################################################################################

class Model(object):
	"""docstring for Model"""
	def __init__(self, arg):
		super(Model, self).__init__()
		self.arg = arg

###################################################################################################


def init_dependencies():
	context = {}
	interface = DemoInterface(None)
	controller = Controller(None)
	service = Service(None)
	datagatherer = DataGatherer(None)
	analyser = Analyser(None)
	visualizer = Visualizer(None)
	model = Model(None)

	interface.set_controller(controller)
	controller.set_service(service)
	service.set_datagatherer(datagatherer)
	#service.set_analyser(analyser)
	#service.set_visualizer(visualizer)
	#service.set_model(model)

	context['interface'] = interface
	context['controller'] = controller
	context['service'] = service
	context['datagatherer'] = datagatherer
	context['analyser'] = analyser
	context['visualizer'] = visualizer
	context['model'] = model

	return context


if __name__ == '__main__':
	username = "Nevil"
	context = init_dependencies()
	#print(context)

	interface = context['interface']

	interface.greet(username)

	# interface.get_input_options()
	# interface.option_selected_hash = input("Enter any 1 of the above options:")
	# print(interface.option_selected_hash)
	# print("You have selected Option {0} from the above options.".format(interface.option_selected_hash))
	# path = input("please enter/ paste local path:\n")

	path = r"nifty50.csv"
	interface.load_data(path)
