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

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    fermi_energy = 0     # Fermi energy, in eV
    temperature = 300    # Temperature, in K

    # Generate a range of energies to plot
    energy = np.linspace(-2, 2, 1000)

    # Calculate the electronic density of states at each energy
    dos = np.array([electronic_density_of_states(fermi_energy, temperature) for energy in energy])

    # Plot the electronic density of states as a function of energy
    plt.plot(energy, dos, color='blue')
    plt.xlabel("Energy (eV)")
    plt.ylabel("Electronic Density of States (states/eV)")
    plt.title("Electronic Density of States for Graphene")
    plt.show()

