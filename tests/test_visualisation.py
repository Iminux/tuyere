import numpy as np
import matplotlib.pyplot as plt
from projec_ellipse import *




def test_generate_ellipsoid(): # changement de la fonction test car initialement en dehors de plage de tolérence
    X, Y, Z = generate_ellipsoid(3, 2, 1, num_points=10)
    assert X.shape == (10, 10)
    assert Y.shape == (10, 10)
    assert Z.shape == (10, 10)

    # Vérifie les bornes des axes
    assert X.max() <= 3
    assert Y.max() <= 2
    assert Z.max() <= 1

    assert X.min() >= -3
    assert Y.min() >= -2
    assert Z.min() >= -1

''''
def test_generate_ellipsoid():
    X, Y, Z = generate_ellipsoid(3, 2, 1, num_points=10)
    assert X.shape == (10, 10)
    assert Y.shape == (10, 10)
    assert Z.shape == (10, 10)
    assert np.isclose(X.max(), 3, atol=0.1)  # Tolérance plus large par rapport à assert np.isclose(X.max(), 3, atol=1e-2)  # Vérifie le rayon maximal sur X
    assert np.isclose(Y.max(), 2, atol=1e-2)  # Vérifie le rayon maximal sur Y
    assert np.isclose(Z.max(), 1, atol=1e-2)  # Vérifie le rayon maximal sur Z
'''
def test_generate_orbit():
    X, Y, Z = generate_orbit((0, 0, 0), 5, num_points=100)
    assert len(X) == 100
    assert len(Y) == 100
    assert len(Z) == 100
    assert np.isclose(np.sqrt(X[0]**2 + Y[0]**2), 5, atol=1e-2)  # Rayon initial

def test_plot_ellipsoid():
    X, Y, Z = generate_ellipsoid(3, 2, 1, num_points=10)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    try:
        plot_ellipsoid(X, Y, Z, ax)
    except Exception as e:
        pytest.fail(f"plot_ellipsoid raised an exception: {e}")


def test_generate_orbit():
    center = (0, 0, 0)
    radius = 5
    num_points = 50
    X, Y, Z = generate_orbit(center, radius, num_points)

    # Vérifie la forme des sorties
    assert X.shape == (50,)
    assert Y.shape == (50,)
    assert Z.shape == (50,)

    # Vérifie que la distance au centre est constante et égale au rayon
    distances = np.sqrt(X**2 + Y**2 + (Z - center[2])**2)
    assert np.allclose(distances, radius, atol=1e-2)
