from os import PathLike
from typing import TypedDict

from raysect.core import Node, Primitive
from raysect.optical.material import Material

class _FirstWallComponent(TypedDict):
    component_name: str
    file_name: str
    initial_toroidal_shift: float
    toroidal_step: float
    toroidal_instances: int
    initial_vertical_shift: float
    vertical_step: float
    vertical_instances: int

FIRST_WALL_COMPONENT: dict[str, _FirstWallComponent]

def load_component_group(
    file_path: str | PathLike[str],
    parent: Node | None,
    material: Material | None,
    component_name: str,
    toroidal_step: float = 0,
    toroidal_instances: int = 1,
    initial_toroidal_shift: float = 0,
    vertical_step: float = 0,
    vertical_instances: int = 1,
    initial_vertical_shift: float = 0,
) -> dict[str, Primitive]:
    """
    Adds a group of first wall components. The group consists of identical components which are toroidally
    and vertically distributed. The components are instances of the mesh loaded from the given
    Wavefront OBJ mesh file (.obj) and have the same material. The distribution is on a 2 dimensional matrix
    where the first dimension is the toroidal and the second is the vertical direction. The toroidal angle
    is calculated from the x axis and the component 0 is on the x axis. The vertical direction is calculated
    from the midplane and the component 0 is the bottom most component.

    :param str file_path: Path to the Wavefront OBJ mesh file (.obj) containing the first wall component mesh.
    :param Node parent: The parent node in the Raysect scene-graph.
    :param Material material: Instance of Raysect optical material given to the components within the group.
    :param str component_name: Name of the component.
    :param float toroidal_step: Toroidal angle by which the components in the group are rotated. Defaults to 0.
    :param integer toroidal_instances: Number of instances in the toroidal direction. Defaults to 1.
    :param float initial_toroidal_shift: Angle by which the whole group should be rotated in the toroidal direction.
                                         Defaults to 0.
    :param float vertical_step: Vertical distance by which the components in the group are shifted. Defaults to 0.
    :param int vertical_instances: Number of components in the vertical direction. Defaults to (0, 1).
    :param float initial_vertical_shift: Distance by which the whole group is translated in the z direction.
                                         Defaults to 0.

     :return: Dictionary of the components in the group.
    """

def load_first_wall(
    parent: Node | None = None,
    material: Material = ...,
    mesh_folder: str | PathLike[str] | None = None,
) -> dict[str, dict[str, Primitive]]:
    """
    Load Generomak first wall components.

    :parameter Node parent: The parent node in the Raysect scene-graph.
    :param Material material: Instance of Raysect optical material given to the components within the group.
    :param str mesh_folder: Path to the folder containing the first wall components.

    :return: Dictionary of the Generomak first wall component groups.
    """
