import numpy as np
import matplotlib.pyplot as plt

# Constants
a = 1e-10
hbar = 1.05457e-34
eV = 1.60218e-19
m_e = 9.10938e-31
v_F = 1e6
k_B = 1.38065e-23

# Density of states for graphene
def dos(E):
    return np.abs(E) / (np.pi * hbar**2 * v_F**2)

# Fermi-Dirac distribution
def fermi(E, mu, T):
    return 1 / (1 + np.exp((E - mu) / (k_B * T)))

# Generate energy range
E_min = -3 * k_B * 300
E_max = 3 * k_B * 300
E_range = np.linspace(E_min, E_max, 100)

# Generate k-space grid
k_min = -5 / a
k_max = 5 / a
k_pts = 100
k_x, k_y = np.meshgrid(np.linspace(k_min, k_max, k_pts), np.linspace(k_min, k_max, k_pts))

# Integrand for the density of states
def integrand(E, k_x, k_y):
    k = np.sqrt(k_x**2 + k_y**2)
    return dos(E) * fermi(E, 0, 300) * k

# Calculate density of states on k-space grid
dos_vals = np.zeros((k_pts, k_pts))
for i in range(k_pts):
    for j in range(k_pts):
        dos_vals[i,j] = np.trapz(integrand(E_range, k_x[i,j], k_y[i,j]), E_range)

# Plot the density of states
plt.figure()
plt.imshow(dos_vals, extent=[k_min, k_max, k_min, k_max])
plt.colorbar()
plt.xlabel('k_x (1/m)')
plt.ylabel('k_y (1/m)')
plt.title('Electronic Density of States')
plt.show()
