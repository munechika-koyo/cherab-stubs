from raysect.core import Node, Point2D
from raysect.optical import World
from raysect.optical.material.emitter.homogeneous import HomogeneousVolumeEmitter

def generate_annulus_mesh_segments(
    lower_corner: Point2D,
    upper_corner: Point2D,
    number_segments: int,
    world: World,
    material: HomogeneousVolumeEmitter | None = None,
) -> Node:
    """
    Generate an annulus from many smaller mesh segments.

    Used for calculating sensitivity matrices for poloidal inversion grids.

    :param Point2D lower_corner: the lower corner of the poloidal 2D cell.
    :param Point2D upper_corner: the upper corner of the poloidal 2D cell.
    :param int number_segments: The number of angular mesh segments used to build the annulus.
    :param World world: The scene-graph to which the annulus will be attached.
    :return: Node holding all the annulus segment primitives.
    :rtype: Node
    """
