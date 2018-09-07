import pandas as pd


from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show, output_file

from matplotlib import pyplot as plt

class Visualizer(object):
    """docstring for Visualizer"""
    def __init__(self, arg = None):
        super(Visualizer, self).__init__()
        self.arg = arg
        self.colors = ['#D2B4DE','#D68910','#58D68D','#633974','#34495E']

    def time_series(self, df, columns):

        df = df.fillna(0)
        df.set_index('date', inplace= True)
        df.index = pd.to_datetime(df.index)
        df.sort_index(inplace=True)
        source = ColumnDataSource(df)
        df['date'] = df.index
        p = figure(x_axis_type="datetime", plot_width=1200, plot_height=350)
        for index, column in enumerate(columns):
            p.line('date', column, source=source, color= self.colors[index])

        output_file("time_series.html")
        show(p)
    
    def histogram(self, df, columns = ['Age']):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        print(columns)
        ax.hist(df[columns],bins = 10)
        plt.title('Age distribution')
        plt.xlabel('Age')
        plt.ylabel('#Employee')
        plt.show()
    '''
    from visualizer import Visualizer

    from datagatherer import DataGatherer
    PATH = r'..\data\titanic-test.csv'
    dg = DataGatherer()
    df = dg.read(dg, PATH)
    viz = Visualizer()
    viz.histogram(df, ['Fare'])
    '''