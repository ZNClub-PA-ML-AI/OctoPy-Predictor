
import numpy as np

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
        self.y_ = None
        
    def set_datagatherer(self, datagatherer):
        self.datagatherer = datagatherer

    def set_analyser(self, analyser):
        self.analyser = analyser

    def set_visualizer(self, visualizer):
        self.visualizer = visualizer

    def load_data(self, path):
        self.df = self.datagatherer.read(path)
        self.df = self.df[0:100]

    def get_columns(self):
        return np.asanyarray(self.df.columns.values)

    def get_max_labels(self):
        return self.max_labels

    def get_delimmiter(self):
        return self.delimitter;
    
    def fetch_all_features(self, str):
        ''' TODO '''
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

    def set_model(self, model):
        ''' TODO '''
        self.model = model        

    def train(self, train_split):
        self.y_ = self.model.fit(self.df, self.features, self.labels, train_split)
        metrics = self.analyser.get_model_metrics(self.y_, 'regression')
        return metrics
