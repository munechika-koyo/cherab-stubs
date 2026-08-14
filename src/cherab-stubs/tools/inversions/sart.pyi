import numpy as np
from numpy.typing import ArrayLike, NDArray

def invert_sart(
    geometry_matrix: ArrayLike,
    measurement_vector: ArrayLike,
    initial_guess: ArrayLike | None = None,
    max_iterations: int = 250,
    relaxation: float = 1.0,
    conv_tol: float = 1.0e-4,
) -> tuple[NDArray[np.float64], float]: ...
def invert_constrained_sart(
    geometry_matrix: ArrayLike,
    laplacian_matrix: ArrayLike,
    measurement_vector: ArrayLike,
    initial_guess: ArrayLike | None = None,
    max_iterations: int = 250,
    relaxation: float = 1.0,
    beta_laplace: float = 0.01,
    conv_tol: float = 1.0e-4,
) -> tuple[NDArray[np.float64], float]: ...
