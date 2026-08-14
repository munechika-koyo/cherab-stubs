from raysect.core import Point3D as Point3D
from raysect.core import Vector3D as Vector3D
from raysect.core.scenegraph._nodebase import _NodeBase
from raysect.optical.observer import SightLine
from raysect.optical.observer.base import Pipeline0D

from .base import _SpectroscopicObserver0DBase as _SpectroscopicObserver0DBase

class SpectroscopicSightLine(SightLine, _SpectroscopicObserver0DBase):
    """
    .. deprecated:: 1.4.0
       Use Raysect\'s SightLine observer instead.

    A simple line of sight observer.

    Multiple `SpectroscopicSightLine` observers can be combined into `SightLineGroup`.

    :param Point3D origin: The origin point for this sight-line. (optional)
    :param Vector3D direction: The observation direction for this sight-line. (optional)
    :param list pipelines: A list of pipelines that will process the resulting spectra
                           from this observer.
                           Default is [SpectralRadiancePipeline0D(accumulate=False)].

    .. code-block:: pycon

       >>> from matplotlib import pyplot as plt
       >>> from raysect.optical import World
       >>> from raysect.core.math import Point3D, Vector3D
       >>> from cherab.tools.observers import SpectroscopicSightLine
       >>>
       >>> world = World()
       ...
       >>> sightline = SpectroscopicSightLine(Point3D(3., 0, 0), Vector3D(-1, 0, 0), name="MySightLine", parent=world)
       >>> sightline.display_progress = False  # control pipeline parameters through the group observer
       >>> sightline.pixel_samples = 5000
       >>> sightline.observe()
       >>> sightline.plot_spectrum(in_photons=True)  # plot the spectrum
       >>> plt.show()
    """

    origin: Point3D
    direction: Vector3D
    def __init__(
        self,
        origin: Point3D | None = None,
        direction: Vector3D | None = None,
        pipelines: list[Pipeline0D] | None = None,
        parent: _NodeBase | None = None,
        name: str | None = None,
    ) -> None: ...
