from raysect.core.math import AffineMatrix3D, Point3D, Vector3D
from raysect.optical import Ray, Spectrum
from raysect.optical.material.emitter import InhomogeneousVolumeEmitter, VolumeIntegrator
from raysect.optical.scenegraph import Primitive, World

from ..atomic import AtomicData
from .model import PlasmaModel
from .node import Plasma

class PlasmaMaterial(InhomogeneousVolumeEmitter):
    """Raysect Material that handles the integration of the plasma model emission."""

    _plasma: Plasma
    _atomic_data: AtomicData
    _models: list[PlasmaModel]
    _local_to_plasma: AffineMatrix3D

    def __init__(
        self,
        plasma: Plasma,
        atomic_data: AtomicData,
        models: list[PlasmaModel],
        integrator: VolumeIntegrator,
        local_to_plasma: AffineMatrix3D,
    ) -> None: ...
    def emission_function(
        self,
        point: Point3D,
        direction: Vector3D,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum: ...
