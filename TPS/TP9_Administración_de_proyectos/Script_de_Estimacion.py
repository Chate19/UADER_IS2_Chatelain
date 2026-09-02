import numpy as np
import matplotlib.pyplot as plt

# Fórmulas dadas
def calcular_esfuerzo(S):
    return 8 * (S ** 0.95)

def calcular_tiempo(E):
    return 2.4 * (E ** 0.33)

# 1. Gráfico del Esfuerzo (E) para tamaños (S) en el intervalo [0, 10000]
S_values = np.linspace(0, 10000, 500)
E_values = calcular_esfuerzo(S_values)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(S_values, E_values, color='blue')
plt.title('Esfuerzo vs Tamaño del Proyecto')
plt.xlabel('Tamaño (S)')
plt.ylabel('Esfuerzo (E)')
plt.grid(True)