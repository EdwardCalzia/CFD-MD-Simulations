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
nk = 100
kx, ky = np.meshgrid(np.linspace(k_min, k_max, nk), np.linspace(k_min, k_max, nk))
k_vec = np.stack((kx.ravel(), ky.ravel()), axis=1)

# Define the tight-binding Hamiltonian
def H_k(k):
    H_ij = np.zeros((2, 2), dtype=np.complex128)
    H_ij[0,0] = epsilon_0
    H_ij[0,1] = t*(1 + np.exp(-1j*np.dot(k,b1)) + np.exp(-1j*np.dot(k,b2)))
    H_ij[1,0] = np.conj(H_ij[0,1])
    H_ij[1,1] = epsilon_0
    return H_ij

# Construct the Hamiltonian matrix
H = np.zeros((nk*nk, nk*nk), dtype=np.complex128)
for i in range(nk):
    for j in range(nk):
        k = k_vec[i*nk+j]
        H_ij = H_k(k)
        H[i*2:(i+1)*2, j*2:(j+1)*2] = H_ij

# Diagonalize the Hamiltonian
evals, evecs = np.linalg.eigh(H)

# Plot the energy bands
plt.figure(figsize=(8,6))
for i in range(2):
    plt.plot(np.diag(evals[i*nk:(i+1)*nk]).real, color='k')
plt.axhline(y=0, color='k', ls='--')
plt.xticks(np.arange(0, nk, nk//3), ('K', r'$\Gamma$', 'M', 'K'))
plt.ylabel('Energy (eV)')
plt.title('Graphene Electronic Band Structure')
plt.show()
