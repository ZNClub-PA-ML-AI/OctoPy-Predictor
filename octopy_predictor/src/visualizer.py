import pandas as pd


from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show, output_file

from matplotlib import pyplot as plt

class Visualizer(object):
    """base class for all Visualizers"""
    def __init__(self, arg = None):
        super(Visualizer, self).__init__()
        self.arg = arg
        self.colors = ['#D2B4DE','#D68910','#58D68D','#633974','#34495E']
    
    def _is_valid_histogram_input(self, df, column):
        return column is not None\
        and column in set(df.columns.values.tolist())
    
    def histogram(self, df, column = None, bins = 5):
        if self._is_valid_histogram_input(df, column):
            df = df.fillna(0)
            
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.hist(df[column].tolist(), bins)
            
            plt.title(column + ' Distribution')
            plt.xlabel(column)
            plt.ylabel('Count')
            plt.show()

class BokehVisualizer(Visualizer):
    """docstring for BokehVisualizer"""
    def __init__(self, arg):
        super(BokehVisualizer, self).__init__()
        self.arg = arg

    def time_series(self, df, columns):
        
        df = df.fillna(0)
        
        df.set_index('date', inplace = True)
        df.index = pd.to_datetime(df.index)
        df.sort_index(inplace=True)
        df['date'] = df.index
       
        p = figure(x_axis_type="datetime", plot_width=1200, plot_height=350)
        source = ColumnDataSource(df)
        for index, column in enumerate(columns):
            p.line('date', column, source=source, color= self.colors[index])

        output_file("time_series.html")
        show(p)

        
class PandasVisualizer(Visualizer):
    """visualization using Pandas plotting methods
    
    single column df : bar, line, area, hist
    
    """
    
    def bar(self, df, column):
        df[column].value_counts().plot.bar()
        