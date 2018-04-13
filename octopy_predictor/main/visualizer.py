import pandas as pd

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show, output_file



class Visualizer(object):
	"""docstring for Visualizer"""
	def __init__(self, arg):
		super(Visualizer, self).__init__()
		self.arg = arg
		self.colors = ['#D2B4DE','#D68910','#58D68D','#633974','#34495E']

	def time_series(self, df, columnLines):

		df = df.fillna(0)
		df.set_index('date', inplace= True)
		df.index = pd.to_datetime(df.index)
		df.sort_index(inplace=True)
		source = ColumnDataSource(df)
		p = figure(x_axis_type="datetime", plot_width=800, plot_height=350)
		for index in len(columnLines):
			p.line('date', columnLines[index], source=source, color= self.colors[index])

		output_file("ts.html")
		show(p)

'''
from visualizer import Visualizer as viz
from datagatherer import DataGatherer as dg
PATH = r'..\data\nifty50.csv'
df = dg.read(dg, PATH)
columnDtypeGroups =  df.columns.to_series().groupby(df.dtypes).groups
dtypeColumnPairs = {k.name,v for k,v in columnDtypeGroups.items()}
viz.time_series(viz, df, dtypeColumnPairs['float64'])
'''
