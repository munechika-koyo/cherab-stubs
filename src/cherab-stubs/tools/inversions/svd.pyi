import numpy as np
from numpy.typing import NDArray

def invert_svd(w_matrix: NDArray[np.floating], b_vector: NDArray[np.floating]) -> NDArray[np.float64]:
    """
    Performs a Singular Value Decomposition (SVD) operation inversion.

    :param np.ndarray w_matrix: The sensitivity matrix describing the coupling between the
      detectors and the voxels. Must be an array with shape :math:`(N_d, N_s)`.
    :param np.ndarray b_vector: The measured power/radiance vector with shape :math:`(N_d)`.
    :return: The solution vector x as an ndarray.
    """
