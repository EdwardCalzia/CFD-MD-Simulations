import numpy as np
import matplotlib.pyplot as plt

# Lattice constant (in Angstroms)
a = 2.46

# On-site energy (in eV)
epsilon_0 = 0

# Hopping parameter (in eV)
t = 2.7

# Define the reciprocal lattice vectors
b1 = (2*np.pi/a) * np.array([1, -1/np.sqrt(3)])
b2 = (2*np.pi/a) * np.array([1, 1/np.sqrt(3)])

# Define the k-vector range in the first Brillouin zone
k_min = -np.pi/(3*a)
k_max = np.pi/(3*a)
nk = 500
kx, ky = np.meshgrid(np.linspace(k_min, k_max, nk), np.linspace(k_min, k_max, nk))
k_vec = np.stack((kx.ravel(), ky.ravel()), axis=1)

# Define the Fourier transform of the hopping term
def f_k(k):
    return t * (np.exp(-1j*np.dot(k,b1)) + np.exp(-1j*np.dot(k,b2)) + np.exp(1j*np.dot(k,b1-b2)) + np.exp(1j*np.dot(k,b2-b1)) + np.exp(1j*np.dot(k,b1+b2)) + np.exp(-1j*np.dot(k,b1+b2)))

# Calculate the energy dispersion relation
E = np.sqrt((epsilon_0**2) + np.abs(f_k(k_vec).reshape(nk,nk))**2 + 2*epsilon_0*np.sqrt(1+4*np.cos(np.sqrt(3)*ky*a/2)**2+4*np.cos(np.sqrt(3)*ky*a/2)*np.cos(3*kx*a/2)))

# Plot the energy dispersion relation
plt.figure(figsize=(8,6))
plt.imshow(E, origin='lower', extent=[k_min, k_max, k_min, k_max], aspect='auto', cmap='viridis', vmin=-5*t, vmax=5*t)
plt.colorbar(label='Energy (eV)')
plt.xlabel('$k_x$ ($\mathrm{\AA}^{-1}$)')
plt.ylabel('$k_y$ ($\mathrm{\AA}^{-1}$)')
plt.title('Graphene Energy Dispersion Relation')
plt.show()
