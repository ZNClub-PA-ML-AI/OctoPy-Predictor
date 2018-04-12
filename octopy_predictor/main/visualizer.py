import pandas as pd

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show, output_file



class Visualizer(object):
	"""docstring for Visualizer"""
	def __init__(self, arg):
		super(Visualizer, self).__init__()
		self.arg = arg

	def time_series(self, df):

		df = df.fillna(0)
		df.set_index('date')
		df.index = pd.to_datetime(df.index)
		df.index.name = 'Date'
		df.sort_index(inplace=True)

		#df['Total'] = df.Yes + df['Not sure'] + df.No + df.Others
		#df['Precision'] = round(df.Yes/df.Total, 2)

		source = ColumnDataSource(df)

		p = figure(x_axis_type="datetime", plot_width=800, plot_height=350)
		p.line('Date', 'open', source=source)

		output_file("ts.html")
		show(p)