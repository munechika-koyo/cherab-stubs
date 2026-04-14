from numpy.typing import ArrayLike
from raysect.primitive.mesh import Mesh

def toroidal_mesh_from_polygon(
    polygon: ArrayLike,
    toroidal_extent: float,
    polygon_triangles: ArrayLike | None = None,
    num_toroidal_segments: int = 500,
) -> Mesh:
    """
    Generate a watertight Raysect Mesh primitive from the specified 2D polygon in R-Z plane
    by extending it in toroidal direction by a given angle and closing the
    poloidal faces with triangulated polygons.

    :param object polygon: An object which can be converted to a numpy array with shape
                           [N,2] specifying the wall outline polygon in the R-Z plane.
                           The polygon should not be closed, i.e. vertex i = 0 and i = N
                           should not be the same vertex, but neighbours.
    :param object polygon_triangles: An object which can be converted to a numpy array
                                     with shape [M,3] specifying the triangulation
                                     of a polygon (polygon_triangles = [[v1, v2, v3],...),
                                     where v1, v2, v3 are the vertex array indices specifying
                                     the triangle’s vertices. Should be with clockwise winding.
                                     Defaults to None.
                                     If not provided, the triangulation will be performed using
                                     `triangulate2d(polygon)` from raysect.core.math.polygon.
    :param float toroidal_extent: Angular extension of an element in toroidal direction (in degrees).
                                  Note that in the case of toroidal_extent=360  produces
                                  an axisymmetric mesh which has no end faces
    :param int num_toroidal_segments: The number of repeating toroidal segments
                                      per given `toroidal_extent` that will be used to construct
                                      the mesh. Defaults to 500.

    :return: A watertight Raysect Mesh primitive constructed from the R-Z polygon.

    .. code-block:: pycon

        >>> from cherab.tools.primitives import toroidal_mesh_from_polygon
        >>>
        >>> # wall_polygon is your (N, 2) ndarray describing the polygon
        >>> mesh = toroidal_mesh_from_polygon(wall_polygon, toroidal_extent = 50)
    """
