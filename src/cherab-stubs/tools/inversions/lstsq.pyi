import numpy as np
from numpy.typing import NDArray

def invert_regularised_lstsq(
    w_matrix: NDArray[np.floating],
    b_vector: NDArray[np.floating],
    alpha: float = 0.01,
    tikhonov_matrix: NDArray[np.floating] | None = None,
) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
