"""
=====================================
contour[f]([X, Y], Z, [levels=], ...)
=====================================
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('mpl_plot_gallery')

# make data
X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
Z = (1 - X/2. + X**5 + Y**3)*np.exp(-X**2-Y**2)
Z = Z - Z.min()
levs = np.linspace(np.min(Z), np.max(Z), 7)

# plot
fig, ax = plt.subplots()

plt.contourf(X, Y, Z, levels=levs)
plt.contour(X, Y, Z, levels=levs, colors="white", linewidths=0.5)

plt.show()
