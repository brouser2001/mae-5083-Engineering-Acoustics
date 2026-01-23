import numpy as np
import matplotlib.pyplot as plt
from _5b import hAn

l_ratio=1/10
n_harmonics = 8  
ct_L = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
L=1 #assumption/simplification
x = np.linspace(0, 1, 1000)# x positions along the string


# Loop over time fractions
plt.figure(figsize=(12, 8))
for idx, t_frac in enumerate(ct_L):
    y = np.zeros_like(x)
    for n in range(1, n_harmonics + 1):
        wn = n * np.pi / L  # omega_n = n*pi/L (scaled)
        y += hAn(l_ratio,n) * np.sin(n * np.pi * x/L) * np.cos(n*np.pi*t_frac)
    plt.plot(x, y, label=f'ct/L = {t_frac}')

plt.title(f'String shape for l = L/10 (fundamental + 7 overtones)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('5d-answer.png')

