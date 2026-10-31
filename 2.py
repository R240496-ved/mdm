import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 0.02, 1/100000)

Am = 2
fm = 200
Ac = 5
fc = 2000

m = Am * np.sin(2 * np.pi * fm * t)
c = Ac * np.sin(2 * np.pi * fc * t)
s = Ac * (1 + 0.8 * np.sin(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)

plt.subplot(3, 1, 1)
plt.plot(t, m)
plt.title("Message Signal")

plt.subplot(3, 1, 2)
plt.plot(t, c)
plt.title("Carrier Signal")

plt.subplot(3, 1, 3)
plt.plot(t, s)
plt.title("AM Signal")

plt.tight_layout()
plt.show()
