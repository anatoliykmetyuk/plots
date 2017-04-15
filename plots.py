import numpy as np

from bokeh.io import show, output_notebook, push_notebook
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from ipywidgets import interact

def new_plot(x_range=[-2*np.pi, 2*np.pi], y_range=[-2.5, 2.5]):
  source = ColumnDataSource(data=dict(x=[], y=[]))

  plot = figure(plot_height=400, plot_width=400, title="Plot",
                tools="crosshair,pan,reset,save,wheel_zoom",
                x_range=x_range, y_range=y_range)

  plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

  return plot, source

# Num => Num, (Dbl, Dbl) => (Num, Num)
def plot_data(f, frm, to, N):
    x = np.linspace(frm, to, N)
    y = f(x)
    return x, y

def update_source(source, f, frm, to, N):
    x, y = plot_data(f, frm, to, N)
    source.data = dict(x=x, y=y)
    push_notebook()

# f_gen: KWARGS => X => Y
def update_gen(f_gen, source, frm, to, N):
  def upd(**kwargs):
    f = f_gen(**kwargs)
    update_source(source, f, frm, to, N)
  return upd

def jupyter_two_colons():
  from IPython.core.display import HTML
  return HTML("""
<style> 
  div#notebook-container.container {
    /* This acts as a spacer between cells, that is outside the border */
    margin: 2px 0px 2px 0px;
    list-style: none;
    padding: 0;
    margin: 0;
    -ms-box-orient: horizontal;
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -moz-flex;
    display: -webkit-flex;
    display: flex;  
    justify-content: space-around;
    -webkit-flex-wrap: wrap;
    flex-wrap: wrap;
    -webkit-flex-direction: row;
    flex-direction: row;
  }
  div.cell {
  width:550px
  }
</style>
""")

