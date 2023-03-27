import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
nk = 100
kx, ky = np.meshgrid(np.linspace(k_min, k_max, nk), np.linspace(k_min, k_max, nk))

# Define the tight-binding Hamiltonian
def H_k(k):
    H_ij = np.zeros((2, 2), dtype=np.complex128)
    H_ij[0,0] = epsilon_0
    H_ij[0,1] = t*(1 + np.exp(-1j*np.dot(k,b1)) + np.exp(-1j*np.dot(k,b2)))
    H_ij[1,0] = np.conj(H_ij[0,1])
    H_ij[1,1] = epsilon_0
    return H_ij

# Construct the Hamiltonian matrix
H = np.zeros((nk, nk, 2, 2), dtype=np.complex128)
for i in range(nk):
    for j in range(nk):
        k = np.array([kx[i,j], ky[i,j]])
        H[i,j,:,:] = H_k(k)

# Diagonalize the Hamiltonian
evals = np.zeros((nk, nk, 2))
for i in range(nk):
    for j in range(nk):
        evals[i,j,:] = np.linalg.eigvalsh(H[i,j,:,:])

# Plot the energy bands
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(kx, ky, evals[:,:,0], cmap='Blues', alpha=0.8)
ax.plot_surface(kx, ky, evals[:,:,1], cmap='Reds', alpha=0.8)
ax.set_xlabel('kx')
ax.set_ylabel('ky')
ax.set_zlabel('Energy (eV)')
ax.set_title('Graphene Electronic Band Structure')
plt.show()
