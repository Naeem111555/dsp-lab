import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
from scipy.signal.windows import hann

# Specifications
passband_edge = 2000  # Hz
stopband_edge = 5000  # Hz
Fs = 20000  # Hz
filter_length = 21  # Filter length

# Normalized frequencies
passband_edge_normalized = passband_edge / (Fs / 2)
stopband_edge_normalized = stopband_edge / (Fs / 2)

# Design the filter using firwin
coefficients = firwin(filter_length, [passband_edge_normalized, stopband_edge_normalized], pass_zero=False, window='hann')

# Frequency response of the filter
w, h = freqz(coefficients, worN=8000)

# Plot
plt.figure(figsize=(10, 6))

plt.plot(0.5 * Fs * w / np.pi, np.abs(h), 'b')
plt.plot(passband_edge, 0.5*np.sqrt(2), 'ko')
plt.plot(stopband_edge, 0.5*np.sqrt(0.5), 'ko')
plt.axvline(passband_edge, color='k')
plt.axvline(stopband_edge, color='k')
plt.xlim(0, 0.5 * Fs)
plt.title("FIR Filter Frequency Response")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid()

plt.show()
