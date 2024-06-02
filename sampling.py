import numpy as np
import matplotlib.pyplot as plt

# 1. Sampling
def sample_signal(signal, sampling_rate):
    """Sample the signal at the given sampling rate."""
    sampled_signal = signal[::sampling_rate]
    return sampled_signal

# 2. Quantization
def quantize_signal(signal, levels):
    """Quantize the signal to the given number of levels."""
    min_val = np.min(signal)
    max_val = np.max(signal)
    quantized_signal = np.round((signal - min_val) / (max_val - min_val) * (levels - 1))
    quantized_signal = quantized_signal / (levels - 1) * (max_val - min_val) + min_val
    return quantized_signal

# 3. Coding
def encode_signal(signal, levels):
    """Encode the signal into binary representation based on the quantization levels."""
    # Map quantized values to integers
    min_val = np.min(signal)
    max_val = np.max(signal)
    quantized_indices = np.round((signal - min_val) / (max_val - min_val) * (levels - 1)).astype(int)
    # Convert integers to binary strings
    bit_length = int(np.ceil(np.log2(levels)))
    binary_codes = [np.binary_repr(val, width=bit_length) for val in quantized_indices]
    return binary_codes

# Generate a continuous signal (e.g., a sine wave)
fs = 1000  # Sampling frequency of the original continuous signal
t = np.arange(0, 1, 1/fs)
continuous_signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)

# Sampling
sampling_rate = 10
sampled_signal = sample_signal(continuous_signal, sampling_rate)

# Quantization
quantization_levels = 16
quantized_signal = quantize_signal(sampled_signal, quantization_levels)

# Coding
encoded_signal = encode_signal(quantized_signal, quantization_levels)

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t, continuous_signal, label='Continuous Signal')
plt.legend()

plt.subplot(4, 1, 2)
plt.stem(t[::sampling_rate], sampled_signal, linefmt='r-', markerfmt='ro', basefmt='r-', label='Sampled Signal')
plt.legend()

plt.subplot(4, 1, 3)
plt.stem(t[::sampling_rate], quantized_signal, linefmt='g-', markerfmt='go', basefmt='g-', label='Quantized Signal')
plt.legend()

plt.subplot(4, 1, 4)
for i, binary in enumerate(encoded_signal):
    plt.text(i, 0, binary, ha='center', va='center', fontsize=10)
plt.xlim(-1, len(encoded_signal))
plt.ylim(-0.5, 0.5)
plt.title('Encoded Signal (Binary Codes)')
plt.axis('off')

plt.tight_layout()
plt.show()
