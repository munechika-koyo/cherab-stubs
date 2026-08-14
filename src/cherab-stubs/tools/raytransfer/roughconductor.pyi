from raysect.core import AffineMatrix3D, Point3D, Vector3D
from raysect.core.intersection import Intersection
from raysect.optical import Ray, Spectrum, World
from raysect.optical.material import RoughConductor

class RToptimisedRoughConductor(RoughConductor):
    """
    A `RoughConductor` optimised for calculation of ray transfer matrix (geometry matrix).
    The spectral array in this case contains ~ 10^5 - 10^6 spectral bins but the wavelengths for all of them are equal.
    The Fresnel indices are equal for all spectral bins, so the unnecessary calculations are avoided.
    """
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
