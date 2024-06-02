import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

def short_term_autocorrelation(signal, frame_size, overlap):
    step_size = frame_size - overlap
    num_frames = (len(signal) - overlap) // step_size
    autocorrelation_matrix = np.zeros((num_frames, frame_size))

    for i in range(num_frames):
        start = i * step_size
        end = start + frame_size
        frame = signal[start:end]
        autocorrelation_matrix[i] = np.correlate(frame, frame, mode='full')[frame_size - 1:]

    return autocorrelation_matrix

def plot_autocorrelation(autocorrelation_matrix, frame_size, sample_rate):
    time_axis = np.arange(autocorrelation_matrix.shape[0]) * (frame_size / sample_rate)
    lag_axis = np.arange(frame_size) / sample_rate

    plt.figure(figsize=(10, 6))
    plt.imshow(autocorrelation_matrix.T, aspect='auto', origin='lower', extent=[0, time_axis[-1], 0, lag_axis[-1]])
    plt.colorbar(label='Amplitude')
    plt.xlabel('Time (s)')
    plt.ylabel('Lag (s)')
    plt.title('Short-Term Auto-Correlation')
    plt.show()

# Generate a synthetic speech-like signal (a simple sine wave)
duration = 2  # seconds
sample_rate = 16000  # Hz
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
frequency = 440  # A4 note
signal = 0.5 * np.sin(2 * np.pi * frequency * t)

# Parameters for short-term analysis
frame_size = int(0.025 * sample_rate)  # 25 ms frames
overlap = int(0.01 * sample_rate)  # 10 ms overlap

# Compute short-term auto-correlation
autocorrelation_matrix = short_term_autocorrelation(signal, frame_size, overlap)

# Plot the result
plot_autocorrelation(autocorrelation_matrix, frame_size, sample_rate)
