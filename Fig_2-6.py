##Codigo de la figura 2.6: Representacion de la función Delta

#Importar bibliotecas
import matplotlib.pyplot as plt
import numpy as np

#Definicion de funcion delta
def delta_function(x, a=0, delta_width=0.1):
    return np.exp(-((x - a) / delta_width)**2) / (delta_width * np.sqrt(np.pi))

#Declaracion del espacio y constantes
x = np.linspace(-5, 5, 1000)
y = delta_function(x)

#DIbujo de la funcion delta de Dirac
fig, ax = plt.subplots(figsize=(8, 4)) 
ax.plot(x, y, label='Función Delta')
ax.set_xlabel('t')
ax.set_ylabel(r'$\delta(\epsilon)$')  # Utilizamos LaTex para la representación delta-epsilon
ax.legend()
plt.show()
