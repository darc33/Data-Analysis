import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import math
import statsmodels.api as sm 
from statsmodels.formula.api import ols

#creates the figure in where the data is plot
def plotting(x,y, div):
    fig=plt.figure() 
    ax = fig.add_axes([0.1, 0.1, 0.6, 0.75])
    ax.plot(x,y,'x', label = 'datos')
    ax.axvline(div , color='k')
    ax.set_xlabel('requested')
    ax.set_ylabel('received')

#traza el modelo de regresion y su correspondiente error
def trazaError(x, y,side):
    X = sm.add_constant(x)
    model = sm.OLS(y,X).fit()
    m = model.params[1]#pendiente
    b = model.params[0]#intercepcion con y
    desvStd = np.std(y)#desviacion estandar
    cCor = np.corrcoef(x,y)[0][1]#Correlacion
    err = desvStd * math.sqrt(1 - cCor*cCor)#error cuadratico medio
    points = np.linspace(x.min(), x.max())
    plt.plot(points, m*points + b, label='%s model: %.2f x+%.2f'%(side,m,b))
    plt.plot(points, m*points + (b+err), label='%s error1: %.2f x+%.2f'%(side,m,b+err))
    plt.plot(points, m*points + (b-err), label='%s erorr2: %.2f x+%.2f'%(side,m,b-err))
    print('{:s} error {:.2f}'.format(side, err))

datos = pd.read_csv('Resources/Employees.csv')
x1 = datos.requested
y1 = datos.received
div1 = 10 #limite que divide los dos modelos

datos2 = datos[(datos.requested <= div1)] #filtro del modelo que elimina los val mayores al limite
x2 = datos2.requested
y2 = datos2.received

datos3 = datos[(datos.requested > div1)]#filtro del modelo para valores mayores al limite
x3 = datos3.requested
y3 = datos3.received

plotting(x1,y1,div1)

trazaError(x2,y2,'lower')
trazaError(x3,y3,'upper')

plt.legend(bbox_to_anchor=(1.02, 1), borderaxespad=0.)
plt.show()