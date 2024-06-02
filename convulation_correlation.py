import numpy as np
import matplotlib.pyplot as plt

# Define two sequences
x = np.array([1, 2, 3, 4, 5])
h = np.array([2, 1, 0, -1, -2])

# Convolution using numpy's built-in function
convolution_result = np.convolve(x, h, mode='full')

# Correlation using numpy's built-in function
correlation_result = np.correlate(x, h, mode='full')

# Manual implementation of convolution
def manual_convolution(x, h):
    N = len(x)
    M = len(h)
    y = np.zeros(N + M - 1)
    for n in range(N + M - 1):
        for k in range(M):
            if 0 <= n - k < N:
                y[n] += x[n - k] * h[k]
    return y

# Manual implementation of correlation
def manual_correlation(x, h):
    N = len(x)
    M = len(h)
    y = np.zeros(N + M - 1)
    for n in range(N + M - 1):
        for k in range(M):
            if 0 <= n - k < N:
                y[n] += x[n - k] * h[M - 1 - k]
    return y

# Manual computation results
manual_convolution_result = manual_convolution(x, h)
manual_correlation_result = manual_correlation(x, h)

# Plotting the results
plt.figure(figsize=(14, 8))

plt.subplot(2, 2, 1)
plt.stem(convolution_result, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Convolution Result (NumPy)')
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 2)
plt.stem(correlation_result, linefmt='g-', markerfmt='go', basefmt='r-')
plt.title('Correlation Result (NumPy)')
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 3)
plt.stem(manual_convolution_result, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Manual Convolution Result')
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 4)
plt.stem(manual_correlation_result, linefmt='g-', markerfmt='go', basefmt='r-')
plt.title('Manual Correlation Result')
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
