#all-in-one Octo-Py

import pandas as pd
import numpy as np
from sklearn import svm, preprocessing, cross_validation

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

    def get_columns(self):
        columns = self.controller.get_columns()
        for index in range(len(columns)):
            print("Column code : {0} \tColumn Name : {1}".format(index, columns[index]))
    
    def set_features_and_labels(self):
        max_feautures = len(self.controller.get_columns()) - 1
        max_labels = 1
        delimitter = self.controller.get_delimmiter()
        
        statement = 'Octo-Py needs the column code which it needs to predict. \
            Please enter any {0} code from the above:\n'.format(max_labels)
        #print(statement)
        label_codes = int(input(statement))
        
        statement = 'Octo-Py needs the column codes which will be its inputs.\
            Please enter equal to or less than {0}  codes from the above separated with {1}\
            OR\n enter -1 to select all columns except your output prediction label:\n'.format(max_feautures,delimitter)
        #print(statement)
        #feature_codes_str = '-1'
        feature_codes_str = input(statement)
        
        self.controller.set_features_and_labels(feature_codes_str, label_codes)

    def get_features_and_labels(self):
        print('\n(inputs, outputs) for Octo-Py are:')
        print(self.controller.get_features_and_labels())

    def get_model_ids(self):
        print(self.controller.get_model_ids())

    def train(self, train_split):
        self.controller.train(train_split)

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

    def get_columns(self):
        return self.service.get_columns()

    def get_max_labels(self):
        return self.service.get_max_labels()
        
    def get_max_features(self):
        return self.service.get_max_features()

    def get_delimmiter(self):
        return self.service.get_delimmiter()

    def set_features_and_labels(self, feature_code_str, label_codes):
        self.service.set_features_and_labels(feature_code_str, label_codes)

    def get_features_and_labels(self):
        return self.service.get_features_and_labels()

    def get_model_ids(self):
        self.service.get_model_ids()

    def train(self, train_split):
        self.service.train(train_split)

###################################################################################################

class Service(object):
    """docstring for Service"""
    def __init__(self, arg):
        super(Service, self).__init__()
        self.arg = arg
        self.datagatherer = None
        self.analyser = None
        self.visualizer = None
        self.model = None
        self.df = None
        self.features = None
        self.labels = None
        self.delimitter = ','
        self.model = None
        self.model_ids = ['SVC','LinearSVC']

    def set_datagatherer(self, datagatherer):
        self.datagatherer = datagatherer

    def set_analyser(self, analyser):
        self.analyser = analyser

    def set_visualizer(self, visualizer):
        self.visualizer = visualizer

    def set_model(self, model):
        self.model = model

    def load_data(self, path):
        self.df = self.datagatherer.read(path)

    def get_columns(self):
        return np.asanyarray(self.df.columns.values)

    def get_max_labels(self):
        return self.max_labels

    def get_delimmiter(self):
        return self.delimitter;

    def fetch_all_features(self, str):
        return str == '-1'

    def set_features_and_labels(self, feature_codes_str, label_codes):
        feature_codes = []
        if self.fetch_all_features(feature_codes_str):
            column_codes = [i for i in range(len(self.df.columns.values))]
            feature_codes = set(column_codes).difference(set([label_codes]))
        else:
            feature_codes = map(int, feature_codes_str.split(self.delimitter))

        self.features = [self.df.columns.values[index] for index in feature_codes]
        self.labels = self.df.columns.values[label_codes]
    
    def get_features_and_labels(self):
        return self.features,self.labels
    
    def get_model_ids(self):
        return self.model_ids

    def set_model(self, model, model_id = 'SVC'):
        self.model = model
        #return self.model.get_configure_params()

    def train(self, train_split):
        self.model.fit(self.df, self.features, self.labels, train_split)


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

    def get_columns(self, df):
        return self.df.columns.values
        
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
        self.clf = None
    
    def fit(self, df, clf, features, labels, train_split=0.8):
        X = np.array(df[features])
        y = np.array(df[labels])
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size= round(1 - train_split,2))
        clf.fit(X,y)
        return clf

class SVC_Model(Model):
    """docstring for SVC_Model"""
    def __init__(self, arg):
        super(Model, self).__init__()
        self.arg = arg
        self.model_configs = []
        self.algorithm = svm.SVC()

    def set_model_config(self, model_config):
        self.model_config = model_config

    def get_model_config(self):
        return self.model_config

    def fit(self, df, features, labels, train_split):
        self.algorithm = super(Model, self).fit(df, self.algorithm, features, labels, train_split)
    
        
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
    svc_model = SVC_Model(model)

    interface.set_controller(controller)
    controller.set_service(service)
    service.set_datagatherer(datagatherer)
    service.set_analyser(analyser)
    service.set_visualizer(visualizer)
    service.set_model(model)

    context['interface'] = interface
    context['controller'] = controller
    context['service'] = service
    context['datagatherer'] = datagatherer
    context['analyser'] = analyser
    context['visualizer'] = visualizer
    context['model'] = model
    context['SVC_model'] = svc_model
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
    interface.get_columns()
    interface.set_features_and_labels()
    interface.get_features_and_labels()
    interface.get_model_ids()
    interface.train(0.8)