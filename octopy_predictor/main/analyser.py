
from sklearn.metrics import explained_variance_score

class Analyser(object):
    """docstring for Analyser"""        
    def __init__(self, arg):
        super(Analyser, self).__init__()
        self.arg = arg        
        self.regression_metrics = {'Explained Variance' : explained_variance_score}
        self.metrics = {'regression' : self.regression_metrics}
        
    def get_columns(self, df):
        return df.columns.values

    def get_column_data_types(self, df):
        return str(df.dtypes).split('\n')[:-1]
    
    def get_summary(self, df):
        return df.describe()

    def get_model_metrics(self, y_, mode):
        metric_values = {}
        y_true, y_pred = y_[0], y_[1]

        for metric_name, metric_method in self.metrics[mode].items():            
            metric_values[metric_name] = metric_method(y_true, y_pred)
        return metric_values