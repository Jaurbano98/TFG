#Codigo de la figura 2.9: Modelo IF con inputs desde N1 hasta N2

#Importar bibliotecas y definicion de funciones
import matplotlib.pyplot as plt
import numpy as np

# Definición de funciones
def generar_spike_amplitud():
    return np.random.uniform(0.6, 1.0)

##Declaración del espacio, variables y uso de funciones
v_reset = 0.0
tau = 2.0
puntos_tiempo_spike = [2, 4, 6, 8, 10, 12, 14, 16]
umbral = 1.0
retardo_despues_umbral = 0.01
t = np.linspace(0, 15, 1000)  # Ajusté el rango de tiempo para incluir los nuevos spikes
i = np.zeros_like(t)
spikes_tiempo = []
spikes_amplitud = []
umbral_alcanzado_tiempo = []

#Crear el registro de spikes
for punto_spike in puntos_tiempo_spike:
    spike_amplitude = generar_spike_amplitud()
    idx_spike = np.argmin(np.abs(t - punto_spike))

    spikes_tiempo.append(t[idx_spike])
    spikes_amplitud.append(spike_amplitude)
    i[idx_spike:] += spike_amplitude * np.exp(-(t[idx_spike:] - punto_spike) / tau)
    idx_superan_umbral = np.where(i > umbral)[0]
    for idx in idx_superan_umbral:
        umbral_alcanzado_tiempo.append(t[idx])
        i[idx:] = umbral
        idx_cero = np.argmin(np.abs(t - (t[idx] + retardo_despues_umbral)))
        i[idx_cero:] = v_reset


#Visualizacción de los graficos 
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 8))
ax2.plot(t, i, label='Intensidad de Corriente con spikes y umbral', color='blue')
ax2.axhline(umbral, color='red', linestyle='--', label='Umbral')
ax1.stem(spikes_tiempo, spikes_amplitud, linefmt='r-', markerfmt='ro', basefmt='k-', label='Spikes')
ax1.set_ylim(0, 1.5)  # Ajustar límites del eje y según la amplitud de los spikes
for tiempo_umbral in umbral_alcanzado_tiempo:
    ax3.axvline(tiempo_umbral, color='black', linestyle='--', linewidth=1, marker='>', markersize=5, label='Umbral alcanzado')
ax1.set_xlabel('t (ms)')
ax1.set_ylabel('V de entrada')
ax2.set_xlabel('t (ms)')
ax2.set_ylabel('Potencial de membrana en N2')
ax3.set_xlabel('t (ms)')
ax3.set_ylabel('V de salida')
fig.tight_layout()
plt.show()
