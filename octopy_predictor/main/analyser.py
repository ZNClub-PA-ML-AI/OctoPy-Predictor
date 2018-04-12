
from sklearn.metrics import explained_variance_score

class Analyser(object):
    """docstring for Analyser"""
    def __init__(self, arg):
        super(Analyser, self).__init__()
        self.arg = arg

    def get_columns(self, df):
        return df.columns.values

    def get_column_data_types(self, df):
        return str(df.dtypes).split('\n')[:-1]
    
    def get_summary(self, df):
        return df.describe()

    def get_model_metrics(self, y_, mode):
        metrics = {}
        y_true, y_pred = y_[0], y_[1]
        if mode == 'regression':
            metrics['Explained Variance'] = explained_variance_score(y_true, y_pred)
        return metrics