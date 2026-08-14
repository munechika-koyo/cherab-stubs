import sys
from types import TracebackType

import numpy as np
from numpy.typing import NDArray

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

from .opencl_utils import device_select as device_select

_has_pyopencl: bool

class SartOpencl:
    """
    A GPU-accelerated version of SART inversion.
    The geometry matrix and Laplacian matrix are provided on initialisation because they must
    be copied to GPU memory, which takes time. Inversions may be performed multiple times
    for different measurement vectors without copying the matrices each time. If required,
    the Laplacian matrix can be updated by calling
    `update_laplacian_matrix(new_laplacian_matrix)` method. Note that computations are
    performed with single precision.

    :param np.ndarray geometry_matrix: The sensitivity matrix describing the coupling between
                                       the detectors and the voxels. Must be an array
                                       with shape :math:`(N_d, N_s)`.
    :param np.ndarray laplacian_matrix:  The laplacian regularisation matrix of
                                         shape :math:`(N_s, N_s)`.
                                         Default value: `laplacian_matrix=None`.
    :param pyopencl.Device device: OpenCL device which will be used for computations.
                                   Default value: `device=None` (autoselect).
    :param int block_size: Number of GPU threads per block. Must be the power of 2.
                           For the best performance try from 256 to 1024 for Nvidia
                           (use 1024 on high-end GPUs), from 64 to 256 for AMD and from 16 to 64
                           for Intel GPUs. Default value: `block_size=256`.
    :param bool copy_column_major: If True, the two copies of geometry matrix will be stored in
                                   GPU memory. One in row-major order and the other one in
                                   column-major order. This provides much better performance
                                   of the inversions but requires twice as much GPU memory.
                                   Default value: `copy_column_major=True`.
    :param int block_size_row_maj: If `copy_column_major` is set to False, this parameter defines
                                   the number of GPU threads per block in mat_vec_mult_row_maj()
                                   kernel used to calculate y_hat. Must be lower than
                                   `block_size`. Default value: `block_size_row_maj=64` (optimal
                                   value for Nvidia GPUs).
    :param bool use_atomic: If True, increases the number of thread blocks that can run in
                            parallel with the help of atomic operations (custom atomic add on floats).
                            Set this to False, if the atomic operations are running slow on your device
                            (Nvidia GPUs before Kepler, some AMD APUs, some Intel GPUs).
                            Default value: `use_atomic=True`.
    :param int steps_per_thread: If `use_atomic` is set to True, this parameters defines the
                                 maximum number of loop steps performed by the parallel threads
                                 in a single thread block. Default value: `steps_per_thread=64`
                                 (optimal for Nvidia GPUs).
    :param bool verbose: Verbose output, defaults to `verbose=False`.

    .. code-block:: pycon

        >>> with SartOpencl(geometry_matrix, block_size=1024) as invert_sart:
        >>>     solution, residual = invert_sart(measurement_vector)
        >>> ### or ###
        >>> inv_sart = SartOpencl(geometry_matrix, block_size=1024)
        >>> solution, residual = inv_sart(measurement_vector)
        >>> inv_sart.clean()
    """

    def __init__(
        self,
        geometry_matrix: NDArray[np.floating],
        laplacian_matrix: NDArray[np.floating] | None = None,
        device: object | None = None,
        block_size: int = 256,
        copy_column_major: bool = True,
        block_size_row_maj: int = 64,
        use_atomic: bool = True,
        steps_per_thread: int = 64,
        verbose: bool = False,
    ) -> None: ...
    def clean(self) -> None:
        """Releases GPU buffers"""
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def update_laplacian_matrix(self, laplacian_matrix: NDArray[np.floating]) -> None:
        """
        Updates the Laplacian matrix in GPU memory

        :param np.ndarray laplacian_matrix:  The laplacian regularisation matrix of
            shape :math:`(N_s, N_s)`.
        """
    def __call__(
        self,
        measurement_vector: NDArray[np.floating],
        initial_guess: NDArray[np.floating] | float | None = None,
        max_iterations: int = 250,
        relaxation: float = 1.0,
        beta_laplace: float = 0.01,
        conv_tol: float = 0.0001,
        time_limit: float | None = None,
    ) -> tuple[NDArray[np.float32], list[float]]:
        """
        Performs the inversion for a given measurement vector.

        :param np.ndarray measurement_vector: The measured power/radiance vector with
            shape :math:`(N_d)`.
        :param initial_guess: An optional initial guess, can be an array of shape :math:`(N_s)`
            or a constant value that will be used to seed the algorithm.
        :param int max_iterations: The maximum number of iterations to run the SART algorithm
            before returning a result, defaults to `max_iterations=250`.
        :param float relaxation: The relaxation hyperparameter, defaults to `relaxation=1`.
            Consult the reference papers for more information on this hyperparameter.
        :param float beta_laplace: The regularisation hyperparameter in the range [0, 1].
            Defaults to `beta_laplace=0.01`.
        :param float conv_tol: The convergence limit at which the algorithm will be terminated,
            unless the maximum number of iterations has been reached. The convergence is
            calculated as the normalised squared difference between the measurement and solution
            vectors. Note that reaching convergence lower than 1.e-6 is hardly possible
            on GPUs due to single precision calculations and relaxed math.
        :param float time_limit: If set, the iterations will stop after this time limit (in
            seconds) is reached. Default value: `time_limit=None`.

        :return: A tuple with the inverted solution vector :math:`\\mathbf{x}` as an ndarray with
            shape :math:`(N_s)`, and the list of convergence values achieved after each iteration
            step.
        """
    def _calc_y_hat(self, queue: object) -> None: ...
    def _make_iteration(self, queue: object, relaxation: float, beta_laplace: float) -> None: ...
