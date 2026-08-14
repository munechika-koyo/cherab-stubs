from raysect.core.math import AffineMatrix3D, Point3D, Vector3D
from raysect.optical import Ray, Spectrum
from raysect.optical.material.emitter import InhomogeneousVolumeEmitter, VolumeIntegrator
from raysect.optical.scenegraph import Primitive, World

from ..atomic import AtomicData
from ..plasma import Plasma
from .model import BeamModel
from .node import Beam

class BeamMaterial(InhomogeneousVolumeEmitter):
    def __init__(self, beam: Beam, plasma: Plasma, atomic_data: AtomicData, models: list[BeamModel], integrator: VolumeIntegrator) -> None: ...
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
