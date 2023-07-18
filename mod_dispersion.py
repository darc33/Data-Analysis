import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from plotly import tools
import plotly.graph_objs as go
import plotly.offline as ply
matplotlib.style.use('ggplot')

#creates the figure in where the data is plot
def plotting(datos1,datos2):
    Promedios1=datos1.apply(np.mean)
    Promedios2=datos2.apply(np.mean)
    #datos1=datos1.tolist()
    f,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,sharey='row')#sharey=True

    ax1.scatter(datos1.millasg,datos1.desp, c='orange')
    ax1.axvline(Promedios1[0], c='b')
    ax1.axhline(Promedios1[1], c='b')
    ax2.scatter(datos2.millasg,datos2.desp, c='C1')
    ax2.axvline(Promedios2[0], c='k')
    ax2.axhline(Promedios2[1], c='k')
    ax3.scatter(datos1.millasg,datos1.tiempo, c='orange')
    ax3.axvline(Promedios1[0], c='b')
    ax3.axhline(Promedios1[2], c='b')
    ax4.scatter(datos2.millasg,datos2.tiempo, c='C1')
    ax4.axvline(Promedios2[0], c='k')
    ax4.axhline(Promedios2[2], c='k')

    ax1.set_title('Caliente')
    #ax1.set_xlabel('mpg')
    ax1.set_ylabel('desplazamiento(m)')

    ax2.set_title('Frio')
    #ax2.set_xlabel('mpg')
    #ax2.set_ylabel('desplazamiento(m)')

    #ax3.set_title('Caliente')
    ax3.set_xlabel('mpg')
    ax3.set_ylabel('tiempo(s)')

    #ax4.set_title('Frio')
    ax4.set_xlabel('mpg')
    #ax4.set_ylabel('tiempo(s)')

    #f.savefig('temp.png')
    trace1 = go.Scatter(
            x = datos1.millasg,
            y = datos1.desp,
            mode = 'markers'#make the scattter plot
            #line = dict(
            #    color = ("red"),
            #    width = 4,
            #    dash = 'dash'
            #)
        )
        
    trace2 = go.Scatter(
            x = datos1.millasg,
            y = datos1.tiempo,
            mode = 'markers',
            xaxis='x2',
            yaxis='y2'
            )
            
    trace3 = go.Scatter(
            x = datos2.millasg,
            y = datos2.desp,
            mode = 'markers',
            xaxis='x3',
            yaxis='y3'
            )
        
    layout = dict(
        title = "modelo dispersion",
        xaxis = dict( title = "mpg", domain=[0, 0.45]),
        yaxis = dict( title = "desplazamiento(m)", domain=[0, 0.45]),
        xaxis2 =  dict(domain=[0,0.45]),
        yaxis2 = dict( title = "tiempo(s)", domain=[0.55, 1]),
        xaxis3 = dict(domain=[0.55,1]),
        yaxis3 = dict(domain=[0,0.45])
        
    )
    data = [trace1, trace2, trace3]
    fig = dict(data = data, layout = layout)
    ply.plot(fig, filename='simple_plot.html')
    

if __name__ == '__main__':
    tabla1 = pd.read_csv('Resources/Caliente.csv')
    tabla2 = pd.read_csv('Resources/Frio.csv')

    #datos1 = tabla1[['Automovil','millasg','desp','tiempo']]
    #datos2 = tabla2[['Automovil','millasg','desp','tiempo']]

    datos1 = tabla1[['millasg','desp','tiempo']]
    datos2 = tabla2[['millasg','desp','tiempo']]

    plotting(datos1,datos2)

    plt.show()