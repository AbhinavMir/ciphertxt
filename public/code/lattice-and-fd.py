import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Define lattice parameters
omega1 = 1 + 0j
omega2 = 0.5 + 0.5j * np.sqrt(3)  # This gives a hexagonal lattice

# Generate lattice points
lattice_points = [m * omega1 + n * omega2 for m in range(-5, 6) for n in range(-5, 6)]

# Plot lattice points
plt.figure(figsize=(6, 6))
plt.scatter(
    [z.real for z in lattice_points], [z.imag for z in lattice_points], color='blue')
plt.grid(True)

# Add a rectangle to represent the fundamental domain
rectangle = Rectangle(
    (0, 0), omega1.real, omega2.imag, linewidth=1, edgecolor='r', facecolor='none')
plt.gca().add_patch(rectangle)

plt.title('Lattice and Fundamental Domain')
plt.xlabel('Re')
plt.ylabel('Im')
plt.axis('equal')
plt.savefig('../images/lattice-and-fd.png', dpi=100)
