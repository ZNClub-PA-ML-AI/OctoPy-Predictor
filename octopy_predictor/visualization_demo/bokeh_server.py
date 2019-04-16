from os.path import dirname, join

import pandas as pd
import numpy as np
import pandas.io.sql as psql
import sqlite3 as sql

from bokeh.plotting import figure
from bokeh.layouts import layout, column
from bokeh.models import ColumnDataSource, Div
from bokeh.models.widgets import Slider, Select, TextInput
from bokeh.io import curdoc

# bokeh.sampledata.download()
# try:
#     from bokeh.sampledata.movies_data import movie_path    
# except Exception as e:
#     raise e

# conn = sql.connect(movie_path)
# query = open(join(dirname(__file__), 'query.sql')).read()
# movies = psql.read_sql(query, conn)

df = pd.read_csv(r"../data/titanic-train.csv")



df["color"] = np.where(df["Survived"] > 0, "orange", "grey")
df["alpha"] = np.where(df["Survived"] > 0, 0.9, 0.25)
df.fillna(0, inplace=True)  # just replace missing values with zero

print(df.columns)
axis_map = {
    "Sex": "Sex",
    "Age": "Age",
    "Sibling/ Spouse": "SibSp",
    "Parent/ Child": "Parch",
    "Fare": "Fare",
    "Embarked": "Embarked",
}
html_template = '''
<html>
<head>
    <title>
        Bokeh Dashboard 
    </title>
</head>
<body>
<div> 
    <h1> Bokeh Dashboard </h1>
</div>
</body>
</html>
'''
desc = Div(text=html_template, sizing_mode="scale_both")

# Create Input controls
# boxoffice = Slider(title="Dollars at Box Office (millions)", start=0, end=800, value=0, step=1)
gender = Select(title="Sex", value="All", options=list(df.Sex.unique()))
# cast = TextInput(title="Cast names contains")
x_axis = Select(title="X Axis", options=sorted(axis_map.keys()), value="Sex")
y_axis = Select(title="Y Axis", options=sorted(axis_map.keys()), value="Fare")



# Create Column Data Source that will be used by the plot
source = ColumnDataSource(data=dict(x=[], y=[], color=[], title=[], year=[], revenue=[], alpha=[]))

TOOLTIPS=[
    ("Title", "@title"),
    ("Year", "@year"),
    ("$", "@revenue")
]

p = figure(plot_height=600, plot_width=700, title="", toolbar_location=None, tool_events=TOOLTIPS, sizing_mode="scale_both")
p.circle(x="x", y="y", source=source, size=7, color="color", line_color=None, fill_alpha="alpha")

'''
def select_movies():
    genre_val = genre.value
    director_val = director.value.strip()
    cast_val = cast.value.strip()
    selected = movies[
        (movies.Reviews >= reviews.value) &
        (movies.BoxOffice >= (boxoffice.value * 1e6)) &
        (movies.Year >= min_year.value) &
        (movies.Year <= max_year.value) &
        (movies.Oscars >= oscars.value)
    ]
    if (genre_val != "All"):
        selected = selected[selected.Genre.str.contains(genre_val)==True]
    if (director_val != ""):
        selected = selected[selected.Director.str.contains(director_val)==True]
    if (cast_val != ""):
        selected = selected[selected.Cast.str.contains(cast_val)==True]
    return selected


def update():
    df = select_movies()
    x_name = axis_map[x_axis.value]
    y_name = axis_map[y_axis.value]

    p.xaxis.axis_label = x_axis.value
    p.yaxis.axis_label = y_axis.value
    p.title.text = "%d movies selected" % len(df)
    source.data = dict(
        x=df[x_name],
        y=df[y_name],
        color=df["color"],
        title=df["Title"],
        year=df["Year"],
        revenue=df["revenue"],
        alpha=df["alpha"],
    )
'''
controls = [gender, x_axis, y_axis]

def update(*args, **kwargs):
    print("update called")

for control in controls:
    control.on_change('value', lambda attr, old, new: update())

inputs = column(*controls, width=320, height=1000)
inputs.sizing_mode = "fixed"
l = layout([
    [desc],
    [inputs, p],
], sizing_mode="scale_both")

update()  # initial load of the data

curdoc().add_root(l)
curdoc().title = "Movies"