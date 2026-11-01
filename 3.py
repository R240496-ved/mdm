import numpy as np
import matplotlib.pyplot as plt

N, R = 7, 2
D = R * np.sqrt(3*N)

x = [0, D, D/2]
y = [0, 0, np.sqrt(3)*D/2]

t = np.linspace(0, 2*np.pi, 7)

for i in range(3):
    a, b = x[i], y[i]
    plt.fill(a + R*np.cos(t), b + R*np.sin(t), alpha=0.4)
    plt.text(a, b, "Cell")

for i, j in [(0,1), (0,2), (2,1)]:
    plt.plot([x[i],x[j]], [y[i],y[j]], "k--")
    plt.text((x[i]+x[j])/2, (y[i]+y[j])/2, "D")

plt.title(f"Frequency Reuse (N={N}, R={R}, D={D:.2f})")
plt.axis("equal")
plt.grid()
plt.show()


