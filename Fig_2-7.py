##Codigo de la figura 2.7: Representacion de funciones Delta en distintos instantes de tiempo

#Importar bibliotecas
import matplotlib.pyplot as plt
import numpy as np

#Definicion de funcion delta
def delta_function(x, a=0, delta_width=0.1):
    return np.exp(-((x - a) / delta_width)**2) / (delta_width * np.sqrt(np.pi))

#Declaracion del espacio y constantes
x = np.linspace(-5, 5, 1000)
y = delta_function(x)
t1 = 1
t2 = 3
y_t1 = delta_function(x, a=t1)
y_t2 = delta_function(x, a=t2)

#DIbujo de la funcion delta de Dirac en los instantes t = 0, t = 1 y t = 3.
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, label='Función $\delta(t = 0)$')
ax.plot(x, y_t1, label=r'Función $\delta(t - t1) $, t1 = 1', linestyle='dashed')
ax.plot(x, y_t2, label=r'Función $\delta(t - t1) $, t2 = 3', linestyle='dashed')
ax.set_xlabel('t')
ax.set_ylabel(r'$\delta$')
ax.legend()
plt.text(-0.1, 0.1, '$t_0$', color='r')
plt.text(0.9, 0.1, '$t_1$', color='r')
plt.text(2.9, 0.1, '$t_2$', color='r')
plt.show()
