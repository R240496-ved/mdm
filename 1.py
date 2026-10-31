import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 0.05, 1/6000)
x = 5 * np.sin(2 * np.pi * 100 * t)
n = np.random.normal(0, 0.3, len(t))
y = x + n
r = np.convolve(y, np.ones(15)/15, mode="same")

plt.subplot(4, 1, 1)
plt.plot(t, x)
plt.title("Transmitted Signal")

plt.subplot(4, 1, 2)
plt.plot(t, n)
plt.title("Noise Signal")

plt.subplot(4, 1, 3)
plt.plot(t, y)
plt.title("Received Signal")

plt.subplot(4, 1, 4)
plt.plot(t, r)
plt.title("Recovered Signal")

plt.tight_layout()
plt.show()
