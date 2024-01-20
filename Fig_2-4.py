#Codigo de la figura 2.4: Modelo IF que no llega al umbral de disparo.

#Importar bibliotecas y definicion de funciones
import numpy as np
import matplotlib.pyplot as plt

def init_neurona(tau, umbral=np.inf, umbral_reset=-np.inf, v_reposo=0.0, v_reset=0.0):
    v_membrana = v_reposo

    def integrar_disparar(I_entrada, paso_tiempo, duracion):
        nonlocal v_membrana
        tiempos = np.arange(0, duracion, paso_tiempo)
        v_membrana_lista = []
        for t in tiempos:
            v_membrana += (I_entrada - v_membrana) * (1 - np.exp(-paso_tiempo / tau))
            v_membrana_lista.append(v_membrana)
            if v_membrana <= umbral_reset:
                v_membrana = v_reset
        return tiempos, v_membrana_lista
    return integrar_disparar

#Declaración del espacio, variables y uso de funciones
tau = 8
v_reposo = 0.0
neurona_sin_umbral = init_neurona(tau, v_reposo=v_reposo)
tiempos_sin_umbral, v_membrana_sin_umbral = neurona_sin_umbral(0.5, 0.1, 50.0)

# Visualizar resultados
plt.plot(tiempos_sin_umbral, v_membrana_sin_umbral, label='Sin Umbral', linewidth=2, color='blue')
plt.xlabel('Tiempo (ms)')
plt.hlines(y=0.6, xmin=0, xmax=50, color='red', linestyle='--', label='$I_0$')
plt.ylabel('V(t)')
plt.show()

