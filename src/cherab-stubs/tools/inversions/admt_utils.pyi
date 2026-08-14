import numpy as np
from numpy.typing import NDArray

__author__: str

def generate_derivative_operators(
    voxel_vertices: NDArray[np.floating],
    grid_index_1d_to_2d_map: NDArray[np.integer],
    grid_index_2d_to_1d_map: NDArray[np.integer],
) -> dict[str, NDArray[np.float64]]:
    """
    Generate the first and second derivative operators for a regular grid.

    :param ndarray voxel_vertices: an Nx4x2 array of coordinates of the
    vertices of each voxel, (R, Z)
    :param dict grid_1d_to_2d_map: a mapping from the 1D array of
    voxels in the grid to a 2D array of voxels if they were arranged
    spatially.
    :param dict grid_2d_to_1d_map: the inverse mapping from a 2D
    spatially-arranged array of voxels to the 1D array.

    :return dict operators: a dictionary containing the derivative
    operators: Dij for i, y ∊ (x, y) and Di for i ∊ (x, y).

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
        D_{xx} \\equiv \\frac{\\partial^2}{\\partial x^2}\\\\\n        D_{xy} \\equiv \\frac{\\partial^2}{\\partial x \\partial y}

    etc.

    Note that the standard 2D laplacian (for isotropic regularisation)
    can be trivially calculated as L = Dxx * dx + Dyy * dy, where dx and
    dy are the voxel width and height respectively. This expression does
    not however produce the 2D laplacian derived from the N-dimensional
    case.
    """

def calculate_admt(
    voxel_radii: NDArray[np.floating],
    derivative_operators: dict[str, NDArray[np.floating]],
    psi_at_voxels: NDArray[np.floating],
    dx: float,
    dy: float,
    anisotropy: float = 10,
) -> NDArray[np.float64]:
    """
    Calculate the ADMT regularisation operator.

    :param ndarray voxel_radii: a 1D array of the radius at the centre
    of each voxel in the grid
    :param tuple derivative_operators: a named tuple with the derivative
    operators for the grid, as returned by :func:generate_derivative_operators
    :param ndarray psi_at_voxels: the magnetic flux at the centre of
    each voxel in the grid
    :param float dx: the width of each voxel.
    :param float dy: the height of each voxel
    :param float anisotropy: the ratio of the smoothing in the parallel
    and perpendicular directions.

    :return ndarray admt: the ADMT regularisation operator.

    The degree of anisotropy dictates the relative suppression of
    gradients in the directions parallel and perpendicular to the
    magnetic field. For example, `anisotropy=10` implies parallel
    gradients in solution are 10 times smaller than perpendicular
    gradients.

    This function assumes that all voxels are rectilinear, with their
    axes aligned to the coordinate axes. Additionally, all voxels are
    assumed to have the same width and height. If this is not the case,
    the results will be nonsense.

    N.B. the expression for the ADMT operator is taken from equation
    56 of Ingesson's report, where the ADMT operator L satisfies:

    .. math::
        \\Omega = L^T \\cdot L

    This means it is suitable for use in Cherab's inversion methods,
    such as NNLS and SART.
    """
