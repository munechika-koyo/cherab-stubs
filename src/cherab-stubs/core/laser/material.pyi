from raysect.core.math import AffineMatrix3D, Point3D, Vector3D
from raysect.optical import Ray, Spectrum
from raysect.optical.material.emitter import InhomogeneousVolumeEmitter, VolumeIntegrator
from raysect.optical.scenegraph import Primitive, World

from .model import LaserModel
from .node import Laser

class LaserMaterial(InhomogeneousVolumeEmitter):
    def __init__(self, laser: Laser, laser_segment: Primitive, models: list[LaserModel], integrator: VolumeIntegrator) -> None: ...
    def emission_function(  # pyrefly: ignore [bad-override-param-name]
        self,
        point: Point3D,
        direction: Vector3D,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        to_local: AffineMatrix3D,
        to_world: AffineMatrix3D,
    ) -> Spectrum: ...
