import numpy as np
from helper_methods import *

def make_householder(col):
    n_height = len(col)
    m_matrix = np.eye(n_height, 1)
    I = np.eye(n_height)
    v = np.array([x + y for x, y in zip(col, norm(col) * m_matrix)])
    u = v / norm(v)
    return I - 2 * u * u.T

def qr_fact_househ(matrixA):
