import numpy as np
import matplotlib.pyplot as plt

def DFT(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def IDFT(X):
    N = len(X)
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
    return x / N

# Example signal
N = 64
t = np.arange(N)
signal = np.sin(2 * np.pi * t / N) + 0.5 * np.sin(2 * np.pi * 3 * t / N)

# Compute DFT
X = DFT(signal)

# Compute IDFT
reconstructed_signal = IDFT(X)

# Plot the original signal and the reconstructed signal
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, signal, label='Original Signal')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, np.abs(X), label='DFT Magnitude')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, reconstructed_signal.real, label='Reconstructed Signal')
plt.legend()

plt.tight_layout()
plt.show()
