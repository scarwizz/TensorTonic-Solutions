import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    xarray = np.asarray(x, dtype = float)

    for i in range(len(xarray)):
        if xarray[i] < 0 :
            xarray[i] = alpha*xarray[i]
        else :
            xarray[i] = xarray[i]
    return xarray
    # Write code here
    pass