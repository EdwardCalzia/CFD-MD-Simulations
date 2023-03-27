import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(-5, 5, 100)
pristine_y = np.exp(-x**2)
n_type_y = np.exp(-(x+1)**2)
p_type_y = np.exp(-(x-1)**2)

# Plot the three bell curves
plt.plot(x, pristine_y, label='pristine')
plt.plot(x, n_type_y, label='n-type')
plt.plot(x, p_type_y, label='p-type')

# Add vertical lines for Fermi level and Dirac point
plt.axvline(x=0, color='black', linestyle='--', label='EF')
plt.axvline(x=-1, color='black', linestyle='--', label='ED')

# Add legend and axis labels
plt.legend()
plt.xlabel('Gate voltage')
plt.ylabel('Resistance')

# Show the plot
plt.show()
