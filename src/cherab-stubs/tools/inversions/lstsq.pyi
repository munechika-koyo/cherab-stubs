import numpy as np
from numpy.typing import NDArray

def invert_regularised_lstsq(
    w_matrix: NDArray[np.floating],
    b_vector: NDArray[np.floating],
    alpha: float = 0.01,
    tikhonov_matrix: NDArray[np.floating] | None = None,
) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    r"""
    Solves :math:`\mathbf{b} = \mathbf{W} \mathbf{x}` for the vector :math:`\mathbf{x}`,
    using Tikhonov regulariastion.

    This is a thin wrapper around numpy.linalg.lstsq, which modifies
    the arguments to include the supplied Tikhonov regularisation matrix.

    :param np.ndarray w_matrix: The sensitivity matrix describing the coupling between the
      detectors and the voxels. Must be an array with shape :math:`(N_d, N_s)`.
    :param np.ndarray b_vector: The measured power/radiance vector with shape :math:`(N_d)`.
    :param float alpha: The regularisation hyperparameter :math:`\alpha` which determines
      the regularisation strength of the tikhonov matrix.
    :param np.ndarray tikhonov_matrix: The tikhonov regularisation matrix operator, an array
      with shape :math:`(N_s, N_s)`. If None, the identity matrix is used.
    :return: (x, residuals), the solution and residual vectors.

    .. code-block:: pycon

       >>> from cherab.tools.inversions import invert_regularised_lstsq
       >>> x, rvec = invert_regularised_lstsq(w_matrix, b_vector, tikhonov_matrix=tikhonov_matrix)
    """
