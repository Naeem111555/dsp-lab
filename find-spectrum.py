import numpy as np
import matplotlib.pyplot as plt


def signal(k):
    return (0.25 +
            2 * np.sin(2 * np.pi * 5 * k) +
            np.sin(2 * np.pi * 12.5 * k) +
            1.5 * np.sin(2 * np.pi * 20 * k) +
            0.5 * np.sin(2 * np.pi * 35 * k))

# Sampling parameters
sampling_rate = 100  # Hz
T = 1.0 / sampling_rate  # Sampling interval
N = 1000  # Number of sample points

# Sample points
k = np.linspace(0.0, N*T, N, endpoint=False)

# Compute the signal
y = signal(k)

# Compute the FFT
yf = np.fft.fft(y)
xf = np.fft.fftfreq(N, T)[:N//2]

# Plot the signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(k, y)
plt.title('Time Domain Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the spectrum
plt.subplot(2, 1, 2)
plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.title('Frequency Domain Signal (Spectrum)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.grid()

plt.tight_layout()
plt.show()
