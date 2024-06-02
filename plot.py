import numpy as np
import matplotlib.pyplot as plt

# Define the sequence x(n)
x = np.array([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1])

# Define the length of x(n)
N = len(x)

# Define the range of n
n = np.arange(-10, 20)  # Chosen to handle shifts and have a reasonable plotting range

# Initialize y(n) with zeros
y = np.zeros_like(n, dtype=float)

# Compute y(n) = 2x(n - 5) - 3x(n + 4)
for i in range(len(n)):
    if (n[i] - 5 >= 0) and (n[i] - 5 < N):
        y[i] += 2 * x[n[i] - 5]
    if (n[i] + 4 >= 0) and (n[i] + 4 < N):
        y[i] -= 3 * x[n[i] + 4]

# Plot the original sequence x(n)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.stem(np.arange(N), x)
plt.title('Sequence x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid()

# Plot the resulting sequence y(n)
plt.subplot(2, 1, 2)
plt.stem(n, y)
plt.title('Sequence y(n) = 2x(n-5) - 3x(n+4)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid()

plt.tight_layout()
plt.show()
