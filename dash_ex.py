import numpy as np
import plotly.graph_objs as go
import plotly.offline as ply

import plotly.dashboard_objs as dashboard
import IPython.display
import plotly.plotly as py
from IPython.display import Image

#data
n = 201
x = np.linspace(0, 2.0*np.pi, n)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1 + y2

##Plotly begin

#create traces - data collections 
trace1 = go.Scatter(
            x = x,
            y = y1,
            name = 'sine curve',
            line = dict(
                color = ("red"),
                width = 4,
                dash = 'dash'
            )
        )

trace2 = go.Scatter(
            x = x,
            y = y2,
            name = 'cosine curve', 
            line = dict(
                color = ("green"),
                width = 4,
                dash = 'dot' # dot, dashdot
            )
        )

trace3 = go.Scatter(
            x = x,
            y = y3,
            name = 'sine + cosine curve',
            line = dict(
                color = ("blue"),
                width = 4,
                dash = "dashdot"
            )
        )

#create information dictionary
layout = dict(
    title = "trying dashboard",
    xaxis = dict( title = "angle in radian"),
    yaxis = dict( title = "Magnitude")
)


#Pack data
data = [trace1, trace2, trace3]

#Create a figure
fig = dict(data = data, layout = layout)

#Plot
ply.plot(fig, filename='Resources/simple_plot.html')
    
my_dboard = dashboard.Dashboard()
my_dboard.get_preview()

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 'PlotBot:1296',
    'title': 'scatter-for-dashboard'
}
 
box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 'PlotBot:1298',
    'title': 'pie-for-dashboard'
}
 
box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 'PlotBot:1342',
    'title': 'box-for-dashboard',
    'shareKey':'uVoeGB1i8Xf4fk0b57sT2l'
}
 
my_dboard.insert(box_1)
my_dboard.insert(box_2, 'above', 1)
my_dboard.insert(box_3, 'left', 2)
ply.plot(my_dboard, filename='Resources/trying dashb.html')
#py.dashboard_ops.upload(my_dboard, 'My First Dashboard with Python')