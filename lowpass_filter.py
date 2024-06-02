import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Specifications
passband_edge = 1500  # Hz
transition_width = 500  # Hz
Fs = 10000  # Hz
filter_length = 67  # Filter length
window = 'blackman'

# Normalized frequencies
passband_edge_normalized = passband_edge / (Fs / 2)
transition_width_normalized = transition_width / (Fs / 2)

# Design the filter using firwin
coefficients = firwin(filter_length, passband_edge_normalized, window=window, fs=Fs)

# Frequency response of the filter
w, h = freqz(coefficients, worN=8000)

# Plot
plt.figure(figsize=(10, 6))

plt.plot(0.5 * Fs * w / np.pi, np.abs(h), 'b')
plt.axvline(passband_edge, color='r')
plt.axvline(passband_edge + transition_width, color='r', linestyle='--')
plt.axvline(passband_edge - transition_width, color='r', linestyle='--')
plt.title("Lowpass Filter Frequency Response")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid()

plt.show()
