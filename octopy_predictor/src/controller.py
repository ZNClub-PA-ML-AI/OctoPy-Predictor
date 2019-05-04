


class Controller(object):
 """docstring for Controller"""
 def __init__(self, arg):
     super(Controller, self).__init__()
     self.arg = arg
     self.service = None
     self.context = None

 def set_service(self, service):
     self.service = service

 def set_context(self, context):
     self.context = context

 def load_data(self, path, file):
     self.service.load_data(path=path, file=file)

 def get_summary(self):
     return self.service.get_summary()

 def get_column_data_types(self):
     return self.service.get_column_data_types()

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
     return self.context['model_ids']

 def train(self, train_split):
     return self.service.train(train_split)
