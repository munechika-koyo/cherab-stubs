from raysect.core import Point3D as Point3D
from raysect.core import Vector3D as Vector3D
from raysect.core.scenegraph._nodebase import _NodeBase
from raysect.optical.observer import FibreOptic
from raysect.optical.observer.base import Pipeline0D

from .base import _SpectroscopicObserver0DBase as _SpectroscopicObserver0DBase

class SpectroscopicFibreOptic(FibreOptic, _SpectroscopicObserver0DBase):
    """
    .. deprecated:: 1.4.0
       Use Raysect\'s FibreOptic observer instead.

    An optic fibre spectroscopic observer with non-zero acceptance angle.

    Rays are sampled over a circular area at the fibre tip and a conical solid angle
    defined by the acceptance_angle parameter.

    Multiple `SpectroscopicFibreOptic` observers can be combined into `FibreOpticGroup`.

    :param Point3D origin: The origin point for this sight-line. (optional)
    :param Vector3D direction: The observation direction for this sight-line. (optional)
    :param list pipelines: A list of pipelines that will process the resulting spectra
                           from this observer.
                           Default is [SpectralRadiancePipeline0D(accumulate=False)].
    :param float acceptance_angle: The angle in degrees between the z axis and the cone surface
                                   which defines the fibres solid angle sampling area.
    :param float radius: The radius of the fibre tip in metres. This radius defines a circular
                         area at the fibre tip which will be sampled over.

    .. code-block:: pycon

       >>> from matplotlib import pyplot as plt
       >>> from raysect.optical import World
       >>> from raysect.core.math import Point3D, Vector3D
       >>> from cherab.tools.observers import SpectroscopicFibreOptic
       >>>
       >>> world = World()
       ...
       >>> fibreoptic = SpectroscopicFibreOptic(Point3D(3., 0, 0), Vector3D(-1, 0, 0), name="MyFibreOptic", parent=world)
       >>> fibreoptic.acceptance_angle = 5.
       >>> fibreoptic.radius = 2.e-3
       >>> fibreoptic.display_progress = False  # control pipeline parameters through the group observer
       >>> fibreoptic.pixel_samples = 5000
       >>> fibreoptic.observe()
       >>> fibreoptic.plot_spectrum(in_photons=True)  # plots the spectrum
       >>> plt.show()
    """

    origin: Point3D
    direction: Vector3D
    def __init__(
        self,
        origin: Point3D | None = None,
        direction: Vector3D | None = None,
        pipelines: list[Pipeline0D] | None = None,
        acceptance_angle: float | None = None,
        radius: float | None = None,
        parent: _NodeBase | None = None,
        name: str | None = None,
    ) -> None: ...
