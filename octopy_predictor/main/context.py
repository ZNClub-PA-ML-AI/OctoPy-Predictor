'''Application Context in app_context'''

from interface import WebInterface, CommandShellInterface, Interface
from controller import Controller
from service import Service
from datagatherer import DataGatherer
from analyser import Analyser
from visualizer import Visualizer
from model import Model, SVC_Model, SVR_Model

app_context = {}
UPLOAD_FOLDER = r'C:\Users\Augus\dev\Projects\OctoPy-Predictor\octopy_predictor\data'
is_file_stored = True

def init_dependencies():
    
    model_ids = ['SVC_model','SVR_model']
    command_shell_interface = CommandShellInterface(Interface)
    web_interface = WebInterface(Interface)
    controller = Controller(None)
    service = Service(None)
    datagatherer = DataGatherer(None)
    analyser = Analyser(None)
    visualizer = Visualizer(None)
    model = Model(None)
    svc_model = SVC_Model(model)
    svr_model = SVR_Model(model)         
    
    app_context['model_ids'] = model_ids
    app_context['datagatherer'] = datagatherer
    app_context['analyser'] = analyser
    app_context['visualizer'] = visualizer
    app_context['model'] = model
    app_context['SVC_model'] = svc_model
    app_context['SVR_model'] = svr_model

    app_context['CommandShellInterface'] = command_shell_interface
    app_context['WebInterface'] = web_interface
    app_context['controller'] = controller
    app_context['service'] = service
    
    app_context['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    command_shell_interface.set_controller(app_context['controller'])
    web_interface.set_controller(app_context['controller'])
    controller.set_service(app_context['service'])
    controller.set_context(app_context)
    service.set_datagatherer(app_context['datagatherer'])
    service.set_analyser(app_context['analyser'])
    service.set_visualizer(app_context['visualizer'])
    
    '''TODO - Will be taken as user input'''
    service.set_model(app_context['SVR_model'])    

def set_app_context(key, value_key):
	app_context[key] = app_context[value_key]

def get_app_context(key):
	return app_context[key]
