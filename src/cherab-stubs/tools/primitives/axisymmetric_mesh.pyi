from numpy.typing import ArrayLike
from raysect.primitive.mesh import Mesh

def axisymmetric_mesh_from_polygon(
    polygon: ArrayLike,
    num_toroidal_segments: int = 500,
) -> Mesh:
    """
    Generate a Raysect Mesh primitive from the specified 2D polygon.

    :param object polygon: An object which can be converted to a numpy array with shape [N,2]
                           specifying the wall outline polygon in the R-Z plane. The polygon
                           should not be closed, i.e. vertex i = 0 and i = N should not be the
                           same vertex, but neighbours.
    :param int num_toroidal_segments: The number of repeating toroidal segments that will be used
                                      to construct the mesh.
    :return: A Raysect Mesh primitive constructed from the R-Z polygon using symmetry.

    .. code-block:: pycon

        >>> from cherab.tools.primitives import axisymmetric_mesh_from_polygon
        >>>
        >>> # wall_polygon is your (N, 2) ndarray describing the polygon
        >>> mesh = axisymmetric_mesh_from_polygon(wall_polygon)
    """
