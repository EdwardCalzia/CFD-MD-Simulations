import matplotlib.pyplot as plt

# Sample data
gate_voltage = [-10, -5, 0, 5, 10]
resistance = [10, 7, 5, 7, 10]
EF = -2
ED = 2

# Create the plot
plt.plot(gate_voltage, resistance, 'bo-')
plt.axhline(y=resistance[gate_voltage.index(0)], color='r', linestyle='-')
plt.axvline(x=EF, color='g', linestyle='--')
plt.axvline(x=ED, color='k', linestyle='--')

# Add labels and titles
plt.title('Graphene Resistance as a function of Gate Voltage')
plt.xlabel('Gate Voltage (V)')
plt.ylabel('Resistance (Ohms)')
plt.text(EF-0.5, max(resistance)*0.8, 'Fermi Level', rotation=90)
plt.text(ED+0.2, max(resistance)*0.8, 'Dirac Point', rotation=90)

# Display the plot
plt.show()
