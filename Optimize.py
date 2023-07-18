import numpy as np
from scipy.optimize import minimize

#solve the optimization problem
def optimization(objective,x0,bnds,cons):
    sol = minimize (objective,x0,method='SLSQP',bounds=bnds,constraints=cons)
    return sol

def ejemplo():
    #funcion objetivo
    def objective(x, sign=-1.0):
        x1 = x[0]
        x2 = x[1]
        gananciaF = 5
        gananciaB = 4
        return sign*((gananciaF*x1) + (gananciaB*x2))
    
    #metodo de restricciones
    def constraint1(x, sign=-1.0):
        materialUnidadF = 100
        materialUnidadB = 125
        materialDisponible = 50000.0
        return sign*(materialUnidadF*x[0] +materialUnidadB*x[1]- materialDisponible)

    x0=[0,0]#Guess

    pelotaFutbol = (0,400)#Limites 0<=pf<=400
    pelotaBasquet = (0,300)#Limites 0<=pB<=300
    bnds= (pelotaFutbol,pelotaBasquet) #bounds

    con1 = {'type': 'ineq', 'fun': constraint1}
    cons = [con1]

    sol = optimization(objective,x0,bnds,cons)

    #print(sol)
    print(sol.message)
    print('pelotas futbol: {:.1f}'.format(sol.x[0]))
    print('pelotas basquet: {:.1f}'.format(sol.x[1]))    
    print('Ganancia: {:.1f}'.format(-objective(sol.x)))

def ejercicio1():
    
    def objective(x, sign=-1.0):
        x1 = x[0]
        x2 = x[1]
        ganancia_S1 = 10
        ganancia_S2 = 15
        return sign*((ganancia_S1*x1) + (ganancia_S2*x2))
    
    def constraint1(x, sign=-1.0):
        t_man_s1 = 0.333
        t_man_s2 = 0.5
        t_man_max = 100
        return sign*(t_man_s1*x[0] + t_man_s2*x[1] - t_man_max)

    def constraint2(x,sign=-1.0):
        t_maq_s1 = 0.333
        t_maq_s2 = 0.1667
        t_maq_max = 80
        return sign*(t_maq_s1*x[0] + t_maq_s2*x[1] - t_maq_max)

    x0=[0,0]#Guess

    S1 = (0,None)
    S2 = (0,None)
    bnds= (S1,S2) #bounds

    cons = ({'type': 'ineq', 'fun': constraint1},
            {'type': 'ineq', 'fun': constraint2})

    sol = optimization(objective,x0,bnds,cons)

    print(sol.message)
    print('Sillas tipo 1: {:.2f}'.format(sol.x[0]))
    print('Sillas tipo 2: {:.2f}'.format(sol.x[1]))
    print('Ganancia: {:.1f}'.format(-objective(sol.x)))

def ejercicio2():

    def objective(x, sign=1.0):
        x1 = x[0]
        x2 = x[1]
        gastos_M1 = 500
        gastos_M2 = 750
        return sign*((gastos_M1*x1) + (gastos_M2*x2))
    
    def constraint1(x, sign=1.0):
        c_alta_M1 =1
        c_alta_M2 =2
        c_alta_min = 70
        return sign*(c_alta_M1*x[0] + c_alta_M2*x[1] - c_alta_min)

    def constraint2(x,sign=1.0):
        c_med_M1 = 2
        c_med_M2 = 2
        c_med_min = 130
        return sign*(c_med_M1*x[0] + c_med_M2*x[1] - c_med_min)

    def constraint3(x,sign=1.0):
        c_baj_M1 = 4
        c_baj_M2 = 4
        c_baj_min = 150
        return sign*(c_baj_M1*x[0] + c_baj_M2*x[1] - c_baj_min)

    x0=[0,0]#Guess

    M1 = (0,None)
    M2 = (0,None)
    bnds= (M1,M2) #bounds

    cons = ({'type': 'ineq', 'fun': constraint1},
            {'type': 'ineq', 'fun': constraint2},
            {'type': 'ineq', 'fun': constraint3})

    sol = optimization(objective,x0,bnds,cons)

    print(sol.message)
    print('Tiempo mina A: {:.2f}'.format(sol.x[0]))
    print('Tiempo mina B: {:.2f}'.format(sol.x[1]))
    print('Costo: {:.2f}'.format(objective(sol.x)))

def ejercicio3():
    
    def objective(x, sign=-1.0):
        x1 = x[0]
        x2 = x[1]
        beneficio_A = 1200
        beneficio_B = 1400
        return sign*((beneficio_A*x1) + (beneficio_B*x2))
    
    def constraint1(x, sign=-1.0):
        nar_la = 1
        nar_lb = 2
        nar_max = 800
        return sign*(nar_la*x[0] + nar_lb*x[1] - nar_max)

    def constraint2(x,sign=-1.0):
        man_la = 2
        man_lb = 1
        man_max = 800
        return sign*(man_la*x[0] + man_lb*x[1] - man_max)

    def constraint3(x,sign=-1.0):
        plat_la = 1
        plat_lb = 1
        plat_max = 500
        return sign*(plat_la*x[0] + plat_lb*x[1] - plat_max)

    x0=[0,0]#Guess

    la = (0,None)
    lb = (0,None)
    bnds= (la,lb) #bounds

    cons = ({'type': 'ineq', 'fun': constraint1},
            {'type': 'ineq', 'fun': constraint2},
            {'type': 'ineq', 'fun': constraint3})

    sol = optimization(objective,x0,bnds,cons)

    print(sol.message)
    print('Kg lote A: {:.2f}'.format(sol.x[0]))
    print('Kg lote B: {:.2f}'.format(sol.x[1]))
    print('Beneficio: {:.1f}'.format(-objective(sol.x)))

def ejercicio4():
    
    def objective(x, sign=1.0):
        x1 = x[0]
        x2 = x[1]
        costo_pa = 600
        costo_pb = 400
        return sign*((costo_pa*x1) + (costo_pb*x2))
    
    def constraint1(x, sign=1.0):
        prot_pa =2
        prot_pb =1
        prot_min = 8
        return sign*(prot_pa*x[0] + prot_pb*x[1] - prot_min)

    def constraint2(x,sign=1.0):
        HC_pa = 6
        HC_pb = 1
        HC_min = 12
        return sign*(HC_pa*x[0] + HC_pb*x[1] - HC_min)
    
    def constraint3(x,sign=1.0):
        g_pa = 1
        g_pb = 3
        g_min = 9
        return sign*(g_pa*x[0] + g_pb*x[1] - g_min)

    x0=[0,0]#Guess

    pa = (0,None)
    pb = (0,None)
    bnds= (pa,pb) #bounds

    cons = ({'type': 'ineq', 'fun': constraint1},
            {'type': 'ineq', 'fun': constraint2},
            {'type': 'ineq', 'fun': constraint3})

    sol = optimization(objective,x0,bnds,cons)

    print(sol.message)
    print('Producto A: {:.2f}'.format(sol.x[0]))
    print('Producto B: {:.2f}'.format(sol.x[1]))
    print('Costo: {:.1f}'.format(objective(sol.x)))

ejemplo()
ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()