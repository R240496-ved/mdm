import numpy as np
import matplotlib.pyplot as plt

N, R = 7, 2
D = R * np.sqrt(3*N)
x, y = [0, D, D/2], [0, 0, np.sqrt(3)*D/2]

for a, b in zip(x, y):
    t = np.linspace(0, 2*np.pi, 7) + np.pi/6
    plt.fill(a + R*np.cos(t), b + R*np.sin(t), alpha=0.4)
    plt.text(a, b, "Cell", ha="center")

for i, j in [(0,1), (0,2), (2,1)]:
    plt.plot([x[i],x[j]], [y[i],y[j]], "k--")
    plt.text((x[i]+x[j])/2, (y[i]+y[j])/2, "D")

plt.title("Frequency Reuse")
plt.axis("equal")
plt.grid()
plt.show()

print("N =", N, "\nR =", R, "\nD =", round(D, 2))
