import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def holomorphic_func(z):
    return z**2

def meromorphic_func(z):
    return 1/z

# Generate a grid of points in the complex plane
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Evaluate the functions at each point on the grid
Z = X + 1j*Y
holomorphic_vals = holomorphic_func(Z)
meromorphic_vals = meromorphic_func(Z)

# Compute the magnitude and phase of the outputs
holomorphic_magnitude = np.abs(holomorphic_vals)
holomorphic_phase = np.angle(holomorphic_vals)
meromorphic_magnitude = np.abs(meromorphic_vals)
meromorphic_phase = np.angle(meromorphic_vals)

# Create the color map
holomorphic_colors = holomorphic_phase + holomorphic_magnitude
meromorphic_colors = meromorphic_phase + meromorphic_magnitude

# Mask out the pole of the meromorphic function
meromorphic_colors[np.isinf(meromorphic_magnitude)] = np.nan

# Plot the functions
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].imshow(holomorphic_colors, extent=[-2, 2, -2, 2], origin='lower', cmap='hsv')
axs[0].set_title('Holomorphic function: $f(z) = z^2$')

axs[1].imshow(meromorphic_colors, extent=[-2, 2, -2, 2], origin='lower', cmap='hsv')
axs[1].set_title('Meromorphic function: $f(z) = 1/z$')

# Save the file in SVG format
plt.savefig('../images/holomorphic-meromorphic.png', dpi=100)
