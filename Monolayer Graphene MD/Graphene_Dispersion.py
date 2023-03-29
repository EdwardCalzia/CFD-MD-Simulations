import matplotlib.pyplot as plt
import numpy as np

# Constants
a = 1.0
d = a * np.sqrt(3)
t = 2.7
t2 = 0.5

# Define the function
def f(x, y):
    return t * np.sqrt(3.0 + 2.0 * np.cos(a * x) + 4.0 * np.cos(a / 2.0 * x) * np.cos(d / 2.0 * y))

# Set up the plot
fig = plt.figure()
ax = fig.gca(projection='3d')
x, y = np.meshgrid(np.arange(-2.0 * np.pi, 2.0 * np.pi, 0.1), np.arange(-2.0 * np.pi, 2.0 * np.pi, 0.1))

# Plot the surface
surf = ax.plot_surface(x, y, f(x, y), rstride=1, cstride=1, cmap='plasma', linewidth=0, antialiased=False)
surf2 = ax.plot_surface(x, y, -f(x, y), rstride=1, cstride=1, cmap='plasma', linewidth=0, antialiased=False)

# Customize the plot
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# ax.set_zlim3d(-3.0, 3.0)
fig.colorbar(surf, shrink=0.4, aspect=10, orientation='horizontal')

# Show the plot
plt.show()
