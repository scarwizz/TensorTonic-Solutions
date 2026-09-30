import numpy as np

def tanh(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    xa = np.asarray(x)
    return (np.exp(xa) - np.exp(-xa))/(np.exp(xa) + np.exp(-xa))
    # Write code here
    pass