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
) -> dict[str, Primitive]: ...
def load_first_wall(
    parent: Node | None = None,
    material: Material = ...,
    mesh_folder: str | PathLike[str] | None = None,
) -> dict[str, dict[str, Primitive]]: ...
