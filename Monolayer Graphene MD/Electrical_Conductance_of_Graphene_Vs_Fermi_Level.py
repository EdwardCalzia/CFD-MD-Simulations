import numpy as np
import matplotlib.pyplot as plt

# Define the Fermi level range and corresponding electrical conductivity values
Ef_range = np.linspace(-2, 2, 100)  # in eV
sigma = 4 * np.pi * np.exp(-np.abs(Ef_range))  # in units of e^2 / h

# Create a line plot to display the relationship between the Fermi level and the electrical conductivity
plt.plot(Ef_range, sigma)

# Set the axis labels and title
plt.xlabel('Fermi Level (eV)')
plt.ylabel('Electrical Conductivity (e²/h)')
plt.title('Electrical Conductance of Graphene')

# Show the plot
plt.show()
