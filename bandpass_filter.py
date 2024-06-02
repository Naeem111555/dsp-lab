import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Specifications
fp1 = 0.2  # Passband edge frequency 1
fp2 = 0.35  # Passband edge frequency 2
fs1 = 0.1   # Stopband edge frequency 1
fs2 = 0.425 # Stopband edge frequency 2
M = 32      # Filter length

# Design the bandpass filter using firwin
coefficients = firwin(M, [fs1, fp1, fp2, fs2], pass_zero=False)

# Frequency response of the filter
w, h = freqz(coefficients, worN=8000)

# Plot
plt.figure(figsize=(10, 6))

plt.plot(0.5 * w / np.pi, np.abs(h), 'b')
plt.axvline(fp1, color='r', linestyle='--', label='Passband Edge 1')
plt.axvline(fp2, color='r', linestyle='--', label='Passband Edge 2')
plt.axvline(fs1, color='g', linestyle='--', label='Stopband Edge 1')
plt.axvline(fs2, color='g', linestyle='--', label='Stopband Edge 2')
plt.title("Bandpass Filter Frequency Response")
plt.xlabel('Normalized Frequency')
plt.ylabel('Gain')
plt.legend()
plt.grid()

plt.show()
