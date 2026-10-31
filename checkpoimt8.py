
import numpy as np
import matplotlib.pyplot as plt

# Ecuacion diferencial
def f(t, y):
    return -2 * y

# Parametros
h = 0.2
t = np.arange(0, 1.01, h)
y_euler = np.zeros(len(t))
y_euler[0] = 1

# Metodo de Euler
for i in range(len(t) - 1):
    y_euler[i + 1] = y_euler[i] + h * f(t[i], y_euler[i])

# Solucion exacta
y_exacta = np.exp(-2 * t)

# Resultados
print("Tiempo | Exacta | Euler")
for i in range(len(t)):
    print(f"{t[i]:.1f} | {y_exacta[i]:.6f} | {y_euler[i]:.6f}")

# Grafica
plt.plot(t, y_exacta, 'o-', label="Solucion exacta")
plt.plot(t, y_euler, 's--', label="Metodo de Euler")
plt.xlabel("Tiempo (t)")
plt.ylabel("y(t)")
plt.title("Comparacion de soluciones")
plt.grid(True)
plt.legend()
plt.show()
