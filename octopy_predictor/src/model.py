from sklearn import svm, model_selection, linear_model
from sklearn.utils import shuffle
import numpy as np

class Model(object):
    """docstring for Model"""
    def __init__(self, arg):
        super(Model, self).__init__()
        self.arg = arg
        self.clf = None
    
    def fit(self, df, clf, features, labels, train_split=0.8):
        X = np.array(df[features])
        ''' TODO '''
        y = np.array(df[labels], dtype = df[labels].dtype)
        
        X, y = shuffle(X, y, random_state=1)
        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size= round(1 - train_split,2))
        print('before fit')
        clf.fit(X_train, y_train)
        print('before predict')
        y_true, y_pred = y_test, clf.predict(X_test)
        
        return clf, (y_true, y_pred)

class SVR_Model(Model):
    """docstring for SVR_Model"""
    def __init__(self, arg):
        super(Model, self).__init__()
        self.arg = arg
        self.model_configs = []
#        self.algorithm = svm.SVR()
        self.algorithm = linear_model.LinearRegression()
        

    def set_model_config(self, model_config):
        self.model_config = model_config

    def get_model_config(self):
        return self.model_config

    def fit(self, df, features, labels, train_split):    
        self.algorithm, y_ = super(SVR_Model, self).fit(df, self.algorithm, features, labels, train_split)
        return y_

class SVC_Model(Model):
    """docstring for SVC_Model"""
    def __init__(self, arg):
        super(Model, self).__init__()
        self.arg = arg
        self.model_configs = []
        ''' TODO '''
#       self.algorithm = svm.SVR()

    def set_model_config(self, model_config):
        self.model_config = model_config

    def get_model_config(self):
        return self.model_config

    def fit(self, df, features, labels, train_split):   
        self.algorithm, y_ = context['model'].fit(df, self.algorithm, features, labels, train_split)
        print("Y_: ",y_)
        return y_
