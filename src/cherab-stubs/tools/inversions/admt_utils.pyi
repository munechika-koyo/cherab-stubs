from collections.abc import Mapping
from typing import Literal, overload

import numpy as np
from numpy.typing import NDArray
from scipy.sparse import csr_array

__author__: str

@overload
def generate_derivative_operators(
    voxel_vertices: NDArray[np.floating],
    grid_index_1d_to_2d_map: Mapping[int, tuple[int, int]] | None = None,
    grid_index_2d_to_1d_map: Mapping[tuple[int, int], int] | None = None,
    sparse: Literal[False] = False,
) -> dict[str, NDArray[np.float64]]: ...
@overload
def generate_derivative_operators(
    voxel_vertices: NDArray[np.floating],
    grid_index_1d_to_2d_map: Mapping[int, tuple[int, int]] | None = None,
    grid_index_2d_to_1d_map: Mapping[tuple[int, int], int] | None = None,
    sparse: Literal[True] = True,
) -> dict[str, csr_array]: ...
@overload
def generate_derivative_operators(
    voxel_vertices: NDArray[np.floating],
    grid_index_1d_to_2d_map: Mapping[int, tuple[int, int]] | None = None,
    grid_index_2d_to_1d_map: Mapping[tuple[int, int], int] | None = None,
    sparse: bool = False,
) -> dict[str, NDArray[np.float64]] | dict[str, csr_array]:
    r"""
    Generate the first and second derivative operators for a regular grid.

    :param ndarray voxel_vertices: an Nx4x2 array of coordinates of the
        vertices of each voxel, (R, Z)
    :param dict grid_1d_to_2d_map: a mapping from the 1D array of
        voxels in the grid to a 2D array of voxels if they were arranged
        spatially. Computed from grid_2d_to_1d_map if not given.
    :param dict grid_2d_to_1d_map: the inverse mapping from a 2D
        spatially-arranged array of voxels to the 1D array. Computed from
        grid_1d_to_2d_map if not given.
    :param sparse: return the operators as sparse matrices if True, or
        as dense matrices if False.

    :return: a dictionary containing the derivative operators: Dij for
        i, j ∊ (x, y) and Di for i ∊ (x, y), Dsp and Dsm.

    This function assumes that all voxels are rectilinear, with their
    axes aligned to the coordinate axes. Additionally, all voxels are
    assumed to have the same width and height. If this is not the case,
    the results will be nonsense.

    The mappings between the 1D list of voxel coordinate and their
    order in a 2D grid assume that the 2D grid would by indexed by
    (x, y), with the y coordinate varying most quickly.

    The return dict contains all the first and second derivative
    operators:

    .. math::
        D_{xx} \equiv \frac{\partial^2}{\partial x^2}\\
        D_{xy} \equiv \frac{\partial^2}{\partial x \partial y}

    etc. It also produces two additional operators, Dsp and Dsm, for
    second derivatives on the dy/dx = 1 and dy/dx = -1 diagonals
    respectively.

    Note that the standard 2D laplacian (for isotropic regularisation)
    can be trivially calculated as follows:

    .. math::
        L = (1 - \alpha) (D_{xx} + D_{yy}) + (\alpha / 2) (D_{sp} + D_{sm})

    α = 2/3 produces the operator used in Carr et. al. RSI 89, 083506 (2018).
    α = 1/3 produces the operator with optimal isotropy.
    """

@overload
def calculate_admt(
    voxel_radii: NDArray[np.floating],
    derivative_operators: Mapping[str, NDArray[np.floating]],
    psi_at_voxels: NDArray[np.floating],
    dx: float,
    dy: float,
    anisotropy: float = 10,
) -> NDArray[np.float64]: ...
@overload
def calculate_admt(
    voxel_radii: NDArray[np.floating],
    derivative_operators: Mapping[str, csr_array],
    psi_at_voxels: NDArray[np.floating],
    dx: float,
    dy: float,
    anisotropy: float = 10,
) -> csr_array:
    r"""
    Calculate the ADMT regularisation operator.

    :param ndarray voxel_radii: a 1D array of the radius at the centre
        of each voxel in the grid
    :param dict derivative_operators: a dictionary with the derivative
        operators for the grid, as returned by :func:generate_derivative_operators
    :param ndarray psi_at_voxels: the magnetic flux at the centre of
        each voxel in the grid
    :param float dx: the width of each voxel.
    :param float dy: the height of each voxel
    :param float anisotropy: the ratio of the smoothing in the parallel
        and perpendicular directions.
    :return: the ADMT regularisation operator.

    The degree of anisotropy dictates the relative suppression of
    gradients in the directions parallel and perpendicular to the
    magnetic field. For example, ``anisotropy=10`` implies parallel
    gradients in the solution are 10 times smaller than perpendicular
    gradients.

    This function assumes that all voxels are rectilinear, with their
    axes aligned to the coordinate axes. Additionally, all voxels are
    assumed to have the same width and height. If this is not the case,
    the results will be nonsense.

    N.B. the expression for the ADMT operator is taken from equation
    56 of Ingesson's report, where the ADMT operator L satisfies:

    .. math::
        \Omega = L^T \cdot L

    This means it is suitable for use in Cherab's inversion methods,
    such as NNLS and SART.

    If the derivative operators are sparse matrices, the returned admt
    operator is also a sparse matrix. Otherwise a dense matrix is
    returned.
    """
