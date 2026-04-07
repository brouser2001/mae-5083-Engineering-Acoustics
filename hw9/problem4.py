import numpy as np
from matplotlib import pyplot as plt

c=343

def TL (S, S1, f, L):
    return 10*np.log10(1+0.25*(((S1/S)-(S/S1))**2)*np.sin(2*np.pi*f*L/c)**2)

# Define a function to convert inches to meters
def in_to_m(inches):
    return inches * 0.0254

def Area(d):
    return (d**2)*np.pi/4

#b

d1=in_to_m(2)
A1=Area(d1)
d2=in_to_m(6)
A2=Area(d2)
L=in_to_m(7.12)
print(L)
f=np.linspace(0,3000,1000)

losses=TL(A1,A2,f,L)

print(A1, A2)
print(np.max(losses))

plt.figure(figsize=(8, 6)) # added argument to figure
plt.plot(f,losses)
plt.xlabel('frequency (Hz)')
plt.ylabel('TL (dB)')
plt.savefig('losses.png')
