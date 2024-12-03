import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm  # For colormap

# Create some data (X, Y, and Z)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Different Z functions
Z1 = np.sin(np.sqrt(X**2 + Y**2))  # Z = sin(sqrt(X^2 + Y^2))
Z2 = np.cos(X) * np.sin(Y)  # Z = cos(X) * sin(Y)
Z3 = np.exp(-0.1*(X**2 + Y**2))  # Z = exp(-0.1*(X^2 + Y^2))

# Create a figure and set of subplots
fig = plt.figure(figsize=(15, 12))

# Plot 1: Surface plot with colormap 'viridis'
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
surf1 = ax1.plot_surface(X, Y, Z1, cmap='viridis', edgecolor='none', shade=True)
ax1.set_title('Surface 1: sin(sqrt(X^2 + Y^2))')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_zlabel('Z axis')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)

# Plot 2: Surface plot with colormap 'inferno'
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
surf2 = ax2.plot_surface(X, Y, Z2, cmap='inferno', edgecolor='none', shade=True)
ax2.set_title('Surface 2: cos(X) * sin(Y)')
ax2.set_xlabel('X axis')
ax2.set_ylabel('Y axis')
ax2.set_zlabel('Z axis')
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)

# Plot 3: Surface plot with colormap 'plasma'
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
surf3 = ax3.plot_surface(X, Y, Z3, cmap='plasma', edgecolor='none', shade=True)
ax3.set_title('Surface 3: exp(-0.1*(X^2 + Y^2))')
ax3.set_xlabel('X axis')
ax3.set_ylabel('Y axis')
ax3.set_zlabel('Z axis')
fig.colorbar(surf3, ax=ax3, shrink=0.5, aspect=5)

# Plot 4: Surface plot with colormap 'cividis'
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
surf4 = ax4.plot_surface(X, Y, Z1, cmap='cividis', edgecolor='none', shade=True)
ax4.set_title('Surface 4: sin(sqrt(X^2 + Y^2)) - cividis colormap')
ax4.set_xlabel('X axis')
ax4.set_ylabel('Y axis')
ax4.set_zlabel('Z axis')
fig.colorbar(surf4, ax=ax4, shrink=0.5, aspect=5)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
