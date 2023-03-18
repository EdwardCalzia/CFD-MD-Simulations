import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the electric field
E = np.array([0, 0, 1])  # Electric field along the z-axis

# Define the initial position and velocity of the electron
r0 = np.array([0, 0, 0])  # Initial position at the origin
v0 = np.array([0, 0, 0])  # Initial velocity is zero

# Define the charge and mass of the electron
q = -1.6e-19  # Charge of an electron in Coulombs
m = 9.11e-31  # Mass of an electron in kg

# Define the time step and duration of the simulation
dt = 1e-9  # Time step in seconds
t_max = 1e-6  # Duration of the simulation in seconds

# Define the equation of motion
def eom(y, t):
    r, v = np.split(y, 2)
    a = q/m * E
    dydt = np.concatenate([v, a])
    return dydt

# Define the initial conditions
y0 = np.concatenate([r0, v0])

# Define the time array
t = np.arange(0, t_max, dt)

# Run the simulation
result = odeint(eom, y0, t)

# Extract the position and velocity arrays
r = result[:, :3]
v = result[:, 3:]

# Plot the trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(r[:, 0], r[:, 1], r[:, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
