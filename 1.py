import numpy as np
import matplotlib.pyplot as plt

Fs = 6000
t = np.arange(0, 0.05, 1/Fs)

Am, fm = 5, 100
in_signal = Am * np.sin(2*np.pi*fm*t)

noise_signal = np.random.normal(0, 0.3, len(t))
Received_signal = in_signal + noise_signal

plt.subplot(3,1,1)
plt.plot(t, in_signal)
plt.title("Input Signal")

plt.subplot(3,1,2)
plt.plot(t, noise_signal)
plt.title("Noise Signal")

plt.subplot(3,1,3)
plt.plot(t, Received_signal, label="Received Signal")
plt.plot(t, in_signal, "r:", label="Input Signal")
plt.title("Received Signal")
plt.legend()

plt.tight_layout()
plt.show()
