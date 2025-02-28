import numpy as np
import matplotlib.pyplot as plt

N = 100

def count_iterations(N, k1, k2):
    arr = list(range(1, N + 1))
    sol = list(range(1, N + 1))

    i = 0
    while True:
        if i % 2 == 0:
            arr = arr[:k1][::-1] + arr[k1:]
        else:
            arr = arr[:k2][::-1] + arr[k2:]
        i += 1

        if arr == sol:
            return i
        
results = np.zeros((N, N))

for k1 in range(1, N + 1):
    for k2 in range(1, N + 1):
        results[k1-1, k2-1] = count_iterations(N, k1, k2)

plt.figure(figsize=(10, 8))
plt.imshow(results, cmap='hot', origin='lower', extent=[1, N, 1, N])
plt.colorbar(label='Iterations to Return to Identity')
plt.xlabel('k2')
plt.ylabel('k1')
plt.title(f'Iterations Needed for (k1, k2) Reversals (N={N})')
plt.show()
