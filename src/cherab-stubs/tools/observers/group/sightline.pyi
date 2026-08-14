from abc import ABCMeta
from collections.abc import Sequence

from raysect.optical.observer import SightLine

from .base import Observer0DGroup as Observer0DGroup

class SightLineGroup(Observer0DGroup, metaclass=ABCMeta):
    """
    A group of SightLine under a single scene-graph node.

    A scene-graph object regrouping a series of \'SightLine\'
    observers as a scene-graph parent. Allows combined observation and display
    control simultaneously.

    :ivar list observers: A list of sight lines (SightLine instances) in this group.

    .. code-block:: pycon

       >>> from math import cos, sin, pi
       >>>
       >>> import matplotlib.pyplot as plt
       >>> from raysect.core import translate, rotate_basis, Point3D, Vector3D
       >>> from raysect.optical import World
       >>> from raysect.optical.observer import RadiancePipeline0D, SpectralRadiancePipeline0D, PowerPipeline0D, SpectralPowerPipeline0D, SightLine
       >>>
       >>> from cherab.tools.observers import SightLineGroup
       >>> from cherab.tools.observers.group.plotting import plot_group_total, plot_group_spectra
       >>>
       >>> world = World()
       >>>
       >>> transform1 = translate(3., 0, 0) * rotate_basis(Vector3D(-cos(pi/10), 0, sin(pi/10)), Vector3D(0, 1, 0))
       >>> sightline_1 = SightLine(transform=transform1, name="SightLine 1")
       >>> transform2 = translate(3, 0 ,0) * rotate_basis(Vector3D(-1, 0, 0), Vector3D(0, 1, 0))
       >>> sightline_2 = SightLine(transform=transform2, name="SightLine 2")
       >>> transform3 = translate(3, 0, 0) * rotate_basis(Vector3D(-cos(pi/10), 0, -sin(pi/10)), Vector3D(0, 1, 0))
       >>> sightline_3 = SightLine(transform=transform3, name="SightLine 3")
       >>>
       >>> group = SightLineGroup(name=\'MySightLineGroup\', parent=world, observers=[sightline_1, sightline_2])
       >>> group.add_observer(sightline_3)
       >>> pipelines = [SpectralRadiancePipeline0D, RadiancePipeline0D]
       >>> keywords = [{\'name\': \'MySpectralPipeline\'}, {\'name\': \'MyMonoPipeline\'}]
       >>> group.connect_pipelines(pipelines, keywords)  # add pipelines to all observers in the group
       >>> group.acceptance_angle = 2  # same value for all sightlines in the group
       >>> group.radius = 2.e-3
       >>> group.spectral_bins = 512
       >>> group.pixel_samples = [2000, 1000, 2000]  # individual value for each sightline in the group
       >>> group.observe()  # combined observation
       >>>
       >>> plot_group_spectra(group, item=\'MySpectralPipeline\', in_photons=True)  # plot the spectra
       >>> plot_group_total(group, item=\'MyMonoPipeline\')  # plot the total signals
       >>> plt.show()
    """

    _OBSERVER_TYPE = SightLine
    @property
    def sensitivity(self) -> list[float]: ...
    @sensitivity.setter
    def sensitivity(self, value: float | Sequence[float]) -> None: ...
