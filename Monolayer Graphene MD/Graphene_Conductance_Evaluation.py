import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
x = np.linspace(0, 1, 100)
y = np.sin(2*np.pi*x)

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Add axis labels and title
ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Conductance (G)')
ax.set_title('Evaluation of Conductance of a Graphene-based Device')

# Show the plot
plt.show()
