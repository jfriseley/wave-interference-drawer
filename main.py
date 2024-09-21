import numpy as np
import pyvista as pv
from random import uniform

# Define the grid dimensions
WIDTH_PIXELS = 1000  # Number of points along x-axis
HEIGHT_PIXELS = 1000  # Number of points along y-axis
NUM_WAVES = 20

def ripple_function_with_decay(x, y, x0=0, y0=0, A=0.1, k=20, decay_rate=2.0):
    # Compute radial distance from the center (x0, y0)
    r = np.sqrt((x - x0)**2 + (y - y0)**2)
    # Compute height using a sine function to create ripples with exponential decay
    return A * np.cos(k * r) * np.exp(-decay_rate * r)




if __name__=="__main__":



    # Generate epicentres
    epicentres = []
    for i in range(NUM_WAVES):
        epicentres.append((uniform(-1, 1), uniform(-1, 1)))


    # Create evenly spaced points along x and y axes
    x = np.linspace(-1, 1, WIDTH_PIXELS)
    y = np.linspace(-1, 1, HEIGHT_PIXELS)

    # Create a mesh grid of (x, y) points (z = 0 to make it flat)
    X, Y = np.meshgrid(x, y)
    Z_total = np.zeros_like(X)
    for (x0, y0) in epicentres:
        Z_total += ripple_function_with_decay(X, Y, x0, y0, A=0.005, k=100, decay_rate=10.0)

    grid = pv.StructuredGrid(X, Y, Z_total)

    # Delaunay 2D to stitch the points into a flat surface

    plotter = pv.Plotter()
    plotter.add_mesh(grid, show_edges=False, scalars=None, cmap="winter")
    plotter.export_obj('mesh.obj')
    plotter.show()
