'''Application app_context'''

import pandas as pd
import numpy as np

from sklearn.utils import shuffle
from sklearn.metrics import explained_variance_score

from interface import *
from controller import *
from service import *
from datagatherer import *
from analyser import *
from visualizer import *
from model import *


app_context = {}

def init_dependencies():
    
    model_ids = ['SVC_model','SVR_model']
    command_shell_interface = CommandShellInterface(Interface)
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
    app_context['controller'] = controller
    app_context['service'] = service

    command_shell_interface.set_controller(app_context['controller'])
    controller.set_service(app_context['service'])
    controller.set_context(app_context)
    service.set_datagatherer(app_context['datagatherer'])
    service.set_analyser(app_context['analyser'])
    service.set_visualizer(app_context['visualizer'])
    
    '''TODO - Will be taken as user input'''
    service.set_model(app_context['SVR_model'])
    return app_context


def set_app_context(key, value_key):
	app_context[key] = app_context[value_key]


def get_app_context(key):
	return app_context[key]

init_dependencies()