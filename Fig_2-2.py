#Codigo de la figura 2.2: Evolucion de v en el caso I_0 = 0

#Importar bibliotecas y definicion de funciones
import numpy as np
import matplotlib.pyplot as plt

def dv_dt(v, t):
    return -v

#Declaracion del espacio y constantes
t = np.linspace(0, 10, 100) 
v0 = 1.0
v = v0 * np.exp(-t) 

#Grafica
plt.plot(t, v, label='dv/dt = -v')
plt.xlabel('Tiempo')
plt.ylabel('v(t)')
plt.legend()
plt.show()
