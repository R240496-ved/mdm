import numpy as np
import matplotlib.pyplot as plt

d = np.arange(1, 101)
c = 3e8

for f in [800e6, 950e6]:
    L = 20*np.log10(f) + 20*np.log10(d) + 20*np.log10(4*np.pi/c)
    plt.plot(d, L, label=f"{f/1e6:.0f} MHz")

plt.xlabel("Distance (m)")
plt.ylabel("Path Loss (dB)")
plt.title("Free-Space Path Loss")
plt.legend()
plt.grid()
plt.show()
