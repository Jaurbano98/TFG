#Codigo de la figura 2.5: Modelo IF con avances repetidos de espigas

#Importar bibliotecas y definicion de funciones
import numpy as np
import matplotlib.pyplot as plt

#Definicion de la neurona como clase
class Neuron:
    def __init__(self, tau, threshold=None, reset_threshold=None, resting_potential=None, reset_potential=None):
        self.tau = tau
        self.threshold = threshold if threshold is not None else np.inf
        self.reset_threshold = reset_threshold if reset_threshold is not None else -np.inf
        self.resting_potential = resting_potential if resting_potential is not None else 0.0
        self.reset_potential = reset_potential if reset_potential is not None else 0.0

        self.time_constant = 1.0 / (1 - np.exp(-1.0 / tau))
        self.potential = self.resting_potential

    def integrate_and_fire(self, input_current, time_step, duration):
        time_points = np.arange(0, duration, time_step)
        membrane_potential = []

        for t in time_points:
            self.potential += (input_current - self.potential) * (1 - np.exp(-time_step / self.tau))
            membrane_potential.append(self.potential)

            if self.potential >= self.threshold:
                self.potential = self.reset_potential
            elif self.potential <= self.reset_threshold:
                self.potential = 0.0

        return time_points, membrane_potential

#Declaración del espacio, variables y uso de funciones
tau = 13.0
threshold = 0.3
reset_threshold = 0.0
resting_potential = 0.0
reset_potential = 0.0
corriente_entrada = 0.4
paso_tiempo = 0.1
duracion = 50.0

#Simulación neurona con umbral
neurona_con_umbral = Neuron(tau, threshold, reset_threshold, resting_potential, reset_potential)
tiempos_con_umbral, potencial_con_umbral = neurona_con_umbral.integrate_and_fire(corriente_entrada, paso_tiempo, duracion)

#Simulación neurona sin umbral
neurona_sin_umbral = Neuron(tau, resting_potential=0.0)
tiempos_sin_umbral, potencial_sin_umbral = neurona_sin_umbral.integrate_and_fire(corriente_entrada, paso_tiempo, duracion)

# Visualización superpuesta de ambas simulaciones.
plt.plot(tiempos_con_umbral, potencial_con_umbral, label='Con Umbral')
plt.plot(tiempos_sin_umbral, potencial_sin_umbral, label='Sin Umbral', linewidth=2, color='red')
plt.hlines(y=0.3, xmin=0, xmax=50, color='red', linestyle='--')
plt.xlabel('Tiempo (ms)')
plt.ylabel('Potencial de membrana')
plt.legend()
plt.show()
