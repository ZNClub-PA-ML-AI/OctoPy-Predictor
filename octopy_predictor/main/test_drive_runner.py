#Test Drive your code here

import context

context.init_dependencies()

viz = context.app_context['visualizer']
gat = context.app_context['datagatherer']

PATH = r'..\data\titanic-test.csv'
PATH = r'..\data\nifty50.csv'

df = gat.read(PATH)

column_dtype_groups = df.columns.to_series().groupby(df.dtypes).groups
for k,v in column_dtype_groups.items():
	print(k,v)
column_dtype_pairs = {k.name:v for k,v in column_dtype_groups.items()}
viz.time_series(df, column_dtype_pairs['float64'])


print('---->End of Test Drive<----')