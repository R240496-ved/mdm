import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 0.02, 1/100000)

Am, fm = 2, 200
Ac, fc = 5, 2000

m = Am * np.sin(2*np.pi*fm*t)
c = Ac * np.sin(2*np.pi*fc*t)
s = (1 + 0.4*m) * c

plt.subplot(3,1,1)
plt.plot(t, m)
plt.title("Message Signal")

plt.subplot(3,1,2)
plt.plot(t, c)
plt.title("Carrier Signal")

plt.subplot(3,1,3)
plt.plot(t, s)
plt.title("AM Signal")

plt.tight_layout()
plt.show()
