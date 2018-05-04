class Interface(object):
    """docstring for CommandShellInterface"""
    def __init__(self, arg):
        super(Interface, self).__init__()
        self.arg = arg
        self.option_selected_hash = -1
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller
        print("controller set")

    def greet(self, username):
        return 'Welcome {0}. I am Octo-Py: the genius predictor'.format(username)

    def get_input_options(self):
        return ["EXCEL from local","JSON from url","CSV from url"]
        
    def load_data(self, path):
        self.controller.load_data(path)

    def get_summary(self):
        return self.controller.get_summary()

    def get_column_data_types(self):
        return self.controller.get_column_data_types()

    def get_columns(self):
        return self.controller.get_columns()        

    def get_contraints_for_set_features_and_labels(self):
        max_feautures = len(self.controller.get_columns()) - 1
        max_labels = 1
        delimitter = self.controller.get_delimmiter()
        return max_feautures, max_labels, delimitter
        
    
    def set_features_and_labels(self, feature_codes_str, label_codes):            
        self.controller.set_features_and_labels(feature_codes_str, label_codes)

    def get_features_and_labels(self):        
        return self.controller.get_features_and_labels()

    def get_model_ids(self):
        print(self.controller.get_model_ids())

    def train(self, train_split):
        return self.controller.train(train_split)

    def greet(self, username):
        return 'Hi {0}, welcome to Octo-Py'.format(username)
        

class CommandShellInterface(Interface):
    """docstring for CommandShellInterface"""
    def __init__(self, arg):
        super(Interface, self).__init__()

    def set_controller(self, controller):
        super(CommandShellInterface, self).set_controller(controller)

    def greet(self, username):
        statement = super(CommandShellInterface, self).greet(username)
        print(statement)

    def get_input_options(self):
        input_options = super(CommandShellInterface, self).get_input_options() 
        print('Input options available are:\n')
        #print((i,input_options[i]) for i in range(input_options))
        for index in range(len(input_options)):
            print('Press {0} for {1}'.format(index+1, input_options[index]))

    def load_data(self, path):
        super(CommandShellInterface, self).load_data(path)

    def get_columns(self):
        columns = super(CommandShellInterface, self).get_columns()
        for index in range(len(columns)):
            print("Column code : {0} \tColumn Name : {1}".format(index, columns[index]))
    
    def set_features_and_labels(self):
        max_feautures, max_labels, delimitter = super(CommandShellInterface, self).get_contraints_for_set_features_and_labels()
        
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
        
        super(CommandShellInterface, self).set_features_and_labels(feature_codes_str, label_codes)

    def get_features_and_labels(self):
        print('\n(inputs, outputs) for Octo-Py are:')
        print(super(CommandShellInterface, self).get_features_and_labels())

    def get_model_ids(self):
        print(super(CommandShellInterface, self).get_model_ids())

    def train(self, train_split):
        train_score = super(CommandShellInterface, self).train(train_split)
        #print(train_score, type(train_score))
        
        for metric_name in train_score:
            statement = '{0} of model is {1}%'.format(metric_name, train_score[metric_name]*100)
        print(statement)



class WebInterface(Interface):
    """docstring for WebInterface"""
    def __init__(self, arg):
        super(Interface, self).__init__()        

    def set_controller(self, controller):
        super(WebInterface, self).set_controller(controller)
    
    def greet(self, username):
        return super(WebInterface, self).greet(username)

    def load_data(self, path):
        super(WebInterface, self).load_data(path)