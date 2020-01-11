"""
analyser.py
 
"""
from sklearn.metrics import explained_variance_score

REGRESSION_MODEL = 'REGRESSION'
CLASSIFICATION_MODEL = 'CLASSIFICATION'


class AnalyserMetric(object):
    """"AnalyserMetrics: state to represent metrics for Analyser"""        
    
    def __init__(self,
                 name = 'Analyser Metric',
                 model_type = REGRESSION_MODEL,
                 function = lambda x:x):
        """
        fields to store different metric configuration
        """
        self.name = name
        self.model_type = model_type
        self.function = function
        
        
class AnalyserMetricsRegistry(object):
    """"AnalyserMetricsRegistry: create metrics for Analyser"""
            
    metrics = [
        AnalyserMetric('Explained Variance', REGRESSION_MODEL, explained_variance_score)
    ]
    
    @staticmethod
    def apply_metrics(model_type = REGRESSION_MODEL, data = {}):
        expected, actual = data
        
        filtered_metrics =  filter(
            lambda member: member.model_type == model_type,
            AnalyserMetricsRegistry.metrics
        )
        
        return { metric.name : metric.function(expected, actual)
            for metric in filtered_metrics
        }


class Analyser(object):
    """Analyser: logic to analyse data
    """
    
    def columns(self, df):
        """
        input: DataFrame
        output: list of names of columns of DataFrame
        """
        return df.columns.values
    
    def types(self, df):
        """
        input: DataFrame
        output: str containing data types of columns of DataFrame
        """
        return str(df.dtypes).split('\n')[:-1]
    
    def describe(self, df):
        """
        input: DataFrame
        output: DataFrame containing descriptive statistics of DataFrame
        """
        return df.describe(how ='all')

    #TODO
    def model_metrics(self, y_, mode):
        metric_values = {}
        y_true, y_pred = y_[0], y_[1]

        for metric_name, metric_method in self.metrics[mode].items():            
            metric_values[metric_name] = metric_method(y_true, y_pred)
        return metric_values
    
    #TODO
    def _is_categorical(self, label):
        """
        input: 
        """
        return len(set(label)) < 10 and all(map(label, lambda x: isinstance(x, str)))
    
    #TODO
    def get_model_type_by_label(self, label = []):
        return 'Classification' if self._is_categorical(label) else 'Regression'
