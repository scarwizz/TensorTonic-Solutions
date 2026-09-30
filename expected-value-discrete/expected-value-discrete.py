import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    xa = np.asarray(x, dtype=float)
    pa = np.asarray(p, dtype=float)
    return float(np.dot(xa, pa))
    # Write code here
    pass