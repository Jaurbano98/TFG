##Codigo de la figura 2.8: Funciones delta utilizadas en un modelo IF

#Importar bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#Definicion de la neurona como clase
class IntegrateAndFireNeuron:
    def __init__(self, tau, threshold=0.3, reset_potential=0.0):
        self.tau = tau
        self.threshold = threshold
        self.reset_potential = reset_potential
        self.potential = 0.0
      
    def integrate_and_fire(self, input_current, time_step, duration):
        time_points = np.arange(0, duration, time_step)
        membrane_potential = []
        spikes = []
        for t in time_points:
            self.potential += (input_current - self.potential) * (1 - np.exp(-time_step / self.tau))
            membrane_potential.append(self.potential)
            if self.potential >= self.threshold:
                spikes.append(t)
                self.potential = self.reset_potential
            elif self.potential <= self.reset_potential:
                self.potential = 0.0
        return time_points, membrane_potential, spikes

#Declaración del espacio, variables y parametros
tau = 10.0
threshold = 0.3
reset_potential = 0.0
input_current = 0.4
time_step = 0.1
duration = 50.0

#Simulación
neuron = IntegrateAndFireNeuron(tau, threshold, reset_potential)
time_points, membrane_potential, spikes = neuron.integrate_and_fire(input_current, time_step, duration)

# Visualización

#Visualización (arriba) Modelo IF
plt.subplot(2, 1, 1)
plt.xlim(0, 50)
plt.plot(time_points, membrane_potential, label='Potencial de membrana')
plt.scatter(spikes, [threshold] * len(spikes), color='r', label='Spikes')
plt.axhline(y=threshold, color='g', linestyle='dashed', label='Umbral')
plt.xlabel('Tiempo (ms)')
plt.ylabel('Potencial de membrana')

#Visualización (abajo) uso de las funciones Delta en modelo IF
plt.subplot(2, 1, 2)
plt.stem(spikes, np.ones_like(spikes), linefmt='r', markerfmt='ro', basefmt='r', label='Delta')
plt.xlim(0, 50)
plt.ylim(0, 2)  
plt.text(13.8, 1.25, '$\delta(t - t1)$', color='r')
plt.text(27.7, 1.25, '$\delta(t - t2)$', color='r')
plt.text(41.6, 1.25, '$\delta(t - t3)$', color='r')
plt.xlabel('Tiempo (ms)')
plt.ylabel('Delta')
plt.tight_layout()
plt.show()
#Para ver en que instantes hay que graficar las funciones delta
#print("Valores t de spikes", spikes)
