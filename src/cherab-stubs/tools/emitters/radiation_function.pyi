from collections.abc import Callable

from raysect.core import Primitive
from raysect.core.math import AffineMatrix3D, Point3D, Vector3D
from raysect.core.math.function.float import Function3D
from raysect.optical import Ray, Spectrum, World
from raysect.optical.material.emitter import InhomogeneousVolumeEmitter

class RadiationFunction(InhomogeneousVolumeEmitter):
    """
    A general purpose radiation material.

    Radiates power over 4 pi according to the supplied 3D radiation
    function. Note that this model ignores the spectral range of the
    observer. The power specified will be spread of the entire
    observable spectral range. Useful for calculating total radiated
    power loads on reactor wall components.

    Note that the function will be evaluated in the local space of the
    primitive to which this material is attached. For radiation
    functions defined in a different coordinate system, consider
    wrapping this in a VolumeTransform material to ensure the function
    evaluation takes place in the correct coordinate system.

    :param Function3D radiation_function: A 3D radiation function that specifies the amount of radiation
      to be radiated at a given point, :math:`\\phi(x, y, z)` [W/m^3].
    :param float step: The scale length for integration of the radiation function.

    .. code-block:: pycon

       >>> from cherab.tools.emitters import RadiationFunction
       >>>
       >>> # define your own 3D radiation function and insert it into this class
       >>> def rad_function_3d(x, y, z): return 0
       >>> radiation_emitter = RadiationFunction(rad_function_3d)
    """

    radiation_function: Function3D
    def __init__(
        self,
        radiation_function: Callable[[float, float, float], float],
        step: float = 0.1,
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
