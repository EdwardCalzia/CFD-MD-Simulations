import numpy as np
from scipy.integrate import quad

def density_of_states(energy):
    hbar = 6.626e-34 / (2 * np.pi)   # Planck constant / 2pi, in J*s
    v_f = 1e6                       # Fermi velocity, in m/s
    return 2 * np.abs(energy) / (np.pi * hbar**2 * v_f**2)

def fermi_dirac_distribution(energy, fermi_energy, temperature):
    k_b = 8.617e-5                  # Boltzmann constant, in eV/K
    return 1 / (1 + np.exp((energy - fermi_energy) / (k_b * temperature)))

def electronic_density_of_states(fermi_energy, temperature):
    def integrand(energy):
        return density_of_states(energy) * fermi_dirac_distribution(energy, fermi_energy, temperature)
    return quad(integrand, -np.inf, np.inf)[0]

if __name__ == '__main__':
    fermi_energy = 0     # Fermi energy, in eV
    temperature = 300    # Temperature, in K

    dos = electronic_density_of_states(fermi_energy, temperature)

    # Print the electronic density of states in a table
    print("{:<15} {:<15}".format("Fermi Energy", "Electronic Density"))
    print("{:<15} {:<15.5e}".format(fermi_energy, dos))
