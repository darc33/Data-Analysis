import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from plotly import tools
import plotly.graph_objs as go
import plotly.offline as ply
matplotlib.style.use('ggplot')

#creates the figure in where the data is plot
def plotting_one(datos1,datos2,datos3):
    y_mosc = datos1.ciudad_residencia
    #print(y_mosc)
    '''
    trace1 = go.Bar(
            x = datos1.genero_est,
            y = y_mosc
        )
        
    trace2 = go.Bar(
            x = datos2.profesion_docente,
            y = datos2.tipo_contrato,
            #mode = 'markers',#make the scattter plot
            )
    trace3 = go.Pie(labels=datos3.modalidad,
             values=datos3.Intensidad_horaria
             )          
    fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Plot 1', 'Plot 2',
                                                          'Plot 3', 'Plot 4'))
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 1, 2)
    fig.append_trace(trace3, 2, 1)
    fig['layout']['xaxis1'].update(title='xaxis 1 title')
    fig['layout']['xaxis2'].update(title='xaxis 2 title')
    #fig['layout']['xaxis3'].update(title='xaxis 3 title')
    #fig['layout']['xaxis4'].update(title='xaxis 4 title')

    fig['layout']['yaxis1'].update(title='yaxis 1 title')
    fig['layout']['yaxis2'].update(title='yaxis 2 title')
    #fig['layout']['yaxis3'].update(title='yaxis 3 title')
    #fig['layout']['yaxis4'].update(title='yaxis 4 title')
    
    fig['layout'].update(title='DASHBOARD')
    '''
    trace1 = dict(
             x=datos1.genero_est,
             y = y_mosc,
             type='bar',
             name='estudiantes',
             xaxis='x1',
             yaxis='y1',
             orientation='h'                          
             ) 
    trace2 = dict(
             x = datos2.profesion_docente,
             y = datos2.tipo_contrato,
             type='bar',
             name='Docentes',
             xaxis='x2',
             yaxis='y2',
             cliponaxis=True                          
             ) 
    trace3 = dict(
             labels=datos3.modalidad,
             values=datos3.Intensidad_horaria,
             type='pie',
             name='Cursos',
             domain= {'x': [0, .45],
                      'y': [0, .45]},
             showlegend=False
             ) 
    layout=dict(
        title="DASHBOARD",
        xaxis = dict( domain=[0, 0.45]),
        yaxis = dict( title = "genero_est", domain=[0.55, 1]),
        xaxis2 = dict( domain=[0.55, 1]),
        yaxis2 = dict( domain=[0.55, 1]),#showticklabels=False)
        margin = list(l = 100)
        )
    
    data = [trace1, trace2, trace3]
    fig = dict(data = data, layout = layout)
    
    
    ply.plot(fig, filename='Resources/estudio.html')
    

if __name__ == '__main__':
    tabla1 = pd.read_csv('Resources/PP_estudiante.csv')
    tabla2 = pd.read_csv('Resources/PP_Docente.csv')
    tabla3 = pd.read_csv('Resources/PP_Curso.csv')
    #datos1 = tabla1[['Automovil','millasg','desp','tiempo']]
    #datos2 = tabla2[['Automovil','millasg','desp','tiempo']]

    datos1 = tabla1[['Id_estudiante','nombre_est','correo_est','genero_est',\
             'ciudad_residencia','pais_residencia','edad_est','estatura_est']]
    datos2 = tabla2[['id_docente','nombre_docente','correo_docente','genero_docente',\
             'Pais_rec_docente','ciudad_docente','profesion_docente','tipo_contrato',\
             'id_programa_FK']]
    datos3 = tabla3[['Id_curso','nombre_curso','modalidad','Intensidad_horaria',\
             'Id_docente_FK','Id_aula_FK']]
    

    plotting_one(datos1,datos2,datos3)

    plt.show()