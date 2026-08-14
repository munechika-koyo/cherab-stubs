import numpy as np
from numpy.typing import ArrayLike, NDArray

def invert_sart(
    geometry_matrix: ArrayLike,
    measurement_vector: ArrayLike,
    initial_guess: ArrayLike | None = None,
    max_iterations: int = 250,
    relaxation: float = 1.0,
    conv_tol: float = 1.0e-4,
) -> tuple[NDArray[np.float64], float]:
    r"""
    Performs a SART inversion on the specified measurement vector.

    This function implements the Simultaneous Algebraic Reconstruction Technique (SART), as published in
    A. Andersen, and A. Kak, Ultrasonic imaging 6, 81 (1984). The SART method is an iterative inversion
    scheme where the source cells are updated with the formula

    .. math::

       x_l^{(i+1)} = f_\mathrm{sart}(x_l^{(i)}) = x_l^{(i)} + \frac{\omega}{W_{\oplus,l}} \sum_{k=1}^{N_d} \frac{W_{k,l}}{W_{k,\oplus}} (\Phi_k - \hat{\Phi}_k),

    where

    .. math::
       W_{k,\oplus} = \sum_{l=1}^{N_s} W_{k,l}, \quad W_{\oplus, l} = \sum_{k=1}^{N_d} W_{k,l}.

    Here :math:`x_l^{(i)}` is the previous estimate for the emission at voxel :math:`l` in iteration :math:`i`.
    The SART method effectively updates each cell by the weighted average error between the forward modelled
    :math:`\hat{\Phi}_k` and observed :math:`\Phi_k` measurements. The observed errors are weighted by both
    their proportion of the total ray length (:math:`W_{k,\oplus}`) and the sum of the effective ray paths
    crossing that cell (:math:`W_{\oplus, l}`).

    :param np.ndarray geometry_matrix: The sensitivity matrix describing the coupling between the detectors
      and the voxels. Must be an array with shape :math:`(N_d, N_s)`.
    :param np.ndarray measurement_vector: The measured power/radiance vector with shape :math:`(N_d)`.
    :param initial_guess: An optional initial guess, can be an array of shape :math:`(N_s)` or a constant
      value that will be used to seed the algorithm.
    :param int max_iterations: The maximum number of iterations to run the SART algorithm before returning
      a result, defaults to `max_iterations=250`.
    :param float relaxation: The relaxation hyperparameter, defaults to `relaxation=1`. Consult the reference
      papers for more information on this hyperparameter.
    :param float conv_tol: The convergence limit at which the algorithm will be terminated, unless the maximum
      number of iterations has been reached. The convergence is calculated as the normalised squared difference
      between the measurement and solution vectors.
    :return: A tuple with the inverted solution vector :math:`\mathbf{x}` as an ndarray with shape :math:`(N_s)`,
      and the convergence achieved as a float.

    .. code-block:: pycon

       >>> from cherab.tools.inversions import invert_sart
       >>> inverted_solution, conv = invert_sart(weight_matrix, observations, max_iterations=100)
    """

def invert_constrained_sart(
    geometry_matrix: ArrayLike,
    laplacian_matrix: ArrayLike,
    measurement_vector: ArrayLike,
    initial_guess: ArrayLike | None = None,
    max_iterations: int = 250,
    relaxation: float = 1.0,
    beta_laplace: float = 0.01,
    conv_tol: float = 1.0e-4,
) -> tuple[NDArray[np.float64], float]:
    r"""
    Performs a constrained SART inversion on the specified measurement vector.

    The core of the constrained SART algorithm is identical to the basic SART algorithm implemented in
    `invert_sart()`. The only difference is that now the iterative update formula includes a
    regularisation operator.

    .. math::

       x_l^{(i+1)} = f_\mathrm{sart}(x_l^{(i)}) - \hat{\mathcal{L}}_\mathrm{iso}(x_l^{(i)}).

    In this particular function we have implemented a isotropic Laplacian smoothness operator,

    .. math::

       \hat{\mathcal{L}}_\mathrm{iso}(x_l^{(i)}) = \beta_L (Cx_l^{(i)} - \sum_{c=1}^C x_c^{(i)}).

    Here, :math:`c` is the index for the sum over the neighbouring voxels. The regularisation
    hyperparameter :math:`\beta_L` determines the amount of local smoothness imposed on the
    solution vector. When :math:`\beta_L = 0`, the solution is fully determined by the
    measurements, and as :math:`\beta_L \rightarrow 1`, the solution is dominated by the
    smoothness operator.

    :param np.ndarray geometry_matrix: The sensitivity matrix describing the coupling between the detectors
      and the voxels. Must be an array with shape :math:`(N_d, N_s)`.
    :param np.ndarray laplacian_matrix: The laplacian regularisation matrix of shape :math:`(N_s, N_s)`.
    :param np.ndarray measurement_vector: The measured power/radiance vector with shape :math:`(N_d)`.
    :param initial_guess: An optional initial guess, can be an array of shape :math:`(N_s)` or a constant
      value that will be used to seed the algorithm.
    :param int max_iterations: The maximum number of iterations to run the SART algorithm before returning
      a result, defaults to `max_iterations=250`.
    :param float relaxation: The relaxation hyperparameter, defaults to `relaxation=1`. Consult the reference
      papers for more information on this hyperparameter.
    :param float beta_laplace: The regularisation hyperparameter in the range [0, 1]. Defaults
      to `beta_laplace=0.01`.
    :param float conv_tol: The convergence limit at which the algorithm will be terminated, unless the maximum
      number of iterations has been reached. The convergence is calculated as the normalised squared difference
      between the measurement and solution vectors.
    :return: A tuple with the inverted solution vector :math:`\mathbf{x}` as an ndarray with shape :math:`(N_s)`,
      and the convergence achieved as a float.

    .. code-block:: pycon

       >>> from cherab.tools.inversions import invert_constrained_sart
       >>> inverted_solution, conv = invert_constrained_sart(weight_matrix, laplacian, observations)
    """
