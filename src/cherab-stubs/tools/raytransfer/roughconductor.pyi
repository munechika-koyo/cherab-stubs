from raysect.core import AffineMatrix3D, Point3D, Vector3D
from raysect.core.intersection import Intersection
from raysect.optical import Ray, Spectrum, World
from raysect.optical.material import RoughConductor

class RToptimisedRoughConductor(RoughConductor):
    def evaluate_shading(
        self,
        world: World,
        ray: Ray,
        s_incoming: Vector3D,
        s_outgoing: Vector3D,
        w_reflection_origin: Point3D,
        w_transmission_origin: Point3D,
        back_face: bool,
        world_to_surface: AffineMatrix3D,
        surface_to_world: AffineMatrix3D,
        intersection: Intersection,
    ) -> Spectrum: ...
