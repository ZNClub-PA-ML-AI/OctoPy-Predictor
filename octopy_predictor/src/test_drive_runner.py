#Test Drive your code here

import context

context.init_dependencies()

viz = context.app_context['visualizer']
gat = context.app_context['datagatherer']

PATH = r'..\data\nifty50.csv'
PATH = r'..\data\titanic-test.csv'

df = gat.read(PATH)

'''time_series'''
#==============================================================================
# column_dtype_groups = df.columns.to_series().groupby(df.dtypes).groups
# column_dtype_dict = {k.name:v for k,v in column_dtype_groups.items()}
# viz.time_series(df, column_dtype_dict['float64'])
#==============================================================================

'''histogram'''
# viz.histogram(df = df, column = 'Fare', bins = 5)

'''analyser: regression or classification'''
print('---->End of Test Drive<----')