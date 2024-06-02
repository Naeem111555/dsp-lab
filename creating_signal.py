import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Sampling rate
Fs = 100  # Hz

# Time vector
t = np.linspace(0, 1, Fs, endpoint=False)  # 1 second

# Frequencies of sinusoidal components
frequencies = [5, 15, 30]  # Hz

# Create signal with three sinusoidal components
s = np.sum([np.sin(2 * np.pi * f * t) for f in frequencies], axis=0)

# Design IIR filter to suppress frequencies of 5 Hz and 30 Hz
def butter_bandstop_filter(data, lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='bandstop')
    filtered_data = lfilter(b, a, data)
    return filtered_data

filtered_s = butter_bandstop_filter(s, 5, 30, Fs)

# Plot original and filtered signals
plt.figure(figsize=(10, 6))
plt.plot(t, s, label='Original Signal')
plt.plot(t, filtered_s, label='Filtered Signal')
plt.title('Original and Filtered Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
