from abc import ABCMeta
from collections.abc import Sequence

from raysect.optical.observer import FibreOptic

from .base import Observer0DGroup as Observer0DGroup

class FibreOpticGroup(Observer0DGroup, metaclass=ABCMeta):
    """
    A group of fibre optics under a single scene-graph node.

    A scene-graph object regrouping a series of \'FibreOptic\'
    observers as a scene-graph parent. Allows combined observation and display
    control simultaneously.

    :ivar list/float acceptance_angle: The angle in degrees between the z axis and the cone
                                       surface which defines the fibres solid angle sampling
                                       area. The same value can be shared between all observers,
                                       or each observer can be assigned with individual value.
    :ivar list/float radius: The radius of the fibre tip in metres. This radius defines a circular
                             area at the fibre tip which will be sampled over. The same value
                             can be shared between all observers, or each observer can be
                             assigned with individual value.

    .. code-block:: pycon

       >>> from math import cos, sin, pi
       >>>
       >>> import matplotlib.pyplot as plt
       >>> from raysect.core import translate, rotate_basis, Point3D, Vector3D
       >>> from raysect.optical import World
       >>> from raysect.optical.observer import RadiancePipeline0D, SpectralRadiancePipeline0D, PowerPipeline0D, SpectralPowerPipeline0D, FibreOptic
       >>>
       >>> from cherab.tools.observers import FibreOpticGroup
       >>> from cherab.tools.observers.group.plotting import plot_group_total, plot_group_spectra
       >>>
       >>> world = World()
       >>>
       >>> transform1 = translate(3., 0, 0) * rotate_basis(Vector3D(-cos(pi/10), 0, sin(pi/10)), Vector3D(0, 1, 0))
       >>> fibre1 = FibreOptic(transform=transform1, name="Fibre 1")
       >>> transform2 = translate(3, 0 ,0) * rotate_basis(Vector3D(-1, 0, 0), Vector3D(0, 1, 0))
       >>> fibre2 = FibreOptic(transform=transform2, name="Fibre 2")
       >>> transform3 = translate(3, 0, 0) * rotate_basis(Vector3D(-cos(pi/10), 0, -sin(pi/10)), Vector3D(0, 1, 0))
       >>> fibre3 = FibreOptic(transform=transform3, name="Fibre 3")
       >>>
       >>> group = FibreOpticGroup(name=\'MyFibreGroup\', parent=world, observers=[fibre1, fibre2])
       >>> group.add_observer(fibre3)
       >>> pipelines = [SpectralRadiancePipeline0D, RadiancePipeline0D]
       >>> keywords = [{\'name\': \'MySpectralPipeline\'}, {\'name\': \'MyMonoPipeline\'}]
       >>> group.connect_pipelines(pipelines, keywords)  # add pipelines to all observers in the group
       >>> group.acceptance_angle = 2  # same value for all fibres in the group
       >>> group.radius = 2.e-3
       >>> group.spectral_bins = 512
       >>> group.pixel_samples = [2000, 1000, 2000]  # individual value for each fibre in the group
       >>> group.observe()  # combined observation
       >>>
       >>> plot_group_spectra(group, item=\'MySpectralPipeline\', in_photons=True)  # plot the spectra
       >>> plot_group_total(group, item=\'MyMonoPipeline\')  # plot the total signals
       >>> plt.show()
    """

    _OBSERVER_TYPE = FibreOptic
    @property
    def acceptance_angle(self) -> list[float]: ...
    @acceptance_angle.setter
    def acceptance_angle(self, value: float | Sequence[float]) -> None: ...
    @property
    def radius(self) -> list[float]: ...
    @radius.setter
    def radius(self, value: float | Sequence[float]) -> None: ...
