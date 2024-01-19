import numpy as np
import matplotlib.pyplot as plt

def dv_dt(v, t):
    return -v


t = np.linspace(0, 10, 100) 
v0 = 1.0

v = v0 * np.exp(-t) 

plt.plot(t, v, label='dv/dt = -v')
plt.xlabel('Tiempo')
plt.ylabel('v(t)')
plt.legend()
plt.show()
