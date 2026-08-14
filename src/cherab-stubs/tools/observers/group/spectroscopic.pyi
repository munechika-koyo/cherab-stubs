from abc import ABCMeta
from collections.abc import Sequence

from raysect.core.math import AffineMatrix3D, Point3D, Vector3D
from raysect.core.scenegraph._nodebase import _NodeBase
from raysect.optical import SpectralFunction
from raysect.optical.observer import Pipeline0D

from ..spectroscopy import SpectroscopicFibreOptic as SpectroscopicFibreOptic
from ..spectroscopy import SpectroscopicSightLine as SpectroscopicSightLine
from .base import Observer0DGroup as Observer0DGroup

class SpectroscopicObserver0DGroup(Observer0DGroup, metaclass=ABCMeta):
    """
    .. deprecated:: 1.4.0
       Use SightLineGroup or FibreOpticGroup based on Raysect's observers instead.

    A base class for a group of 0D spectroscopic observers under a single scene-graph node.

    A scene-graph object regrouping a series of observers as a scene-graph parent.
    Allows combined observation and display control simultaneously.
    Note that for any property except `names` and `pipelines`, the same value can be shared between
    all sight lines, or each sight line can be assigned with individual value.

    :ivar list/Point3D origin: The origin points for the sight lines.
    :ivar list/Vector3D direction: The observation directions for the sight lines.
    :ivar list/bool display_progress: Toggles the display of live render progress.
    :ivar list/bool accumulate: Toggles whether to accumulate samples with subsequent
                                observations.
    """
    def __init__(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
        observers: Sequence[SpectroscopicFibreOptic | SpectroscopicSightLine] | None = None,
    ) -> None: ...
    @property
    def sight_lines(self) -> tuple[SpectroscopicFibreOptic | SpectroscopicSightLine, ...]: ...
    @sight_lines.setter
    def sight_lines(self, value: Sequence[SpectroscopicFibreOptic | SpectroscopicSightLine]) -> None: ...
    def add_sight_line(self, sight_line: SpectroscopicFibreOptic | SpectroscopicSightLine) -> None:
        """
        Adds new fibre optic to the group.

        :param SpectroscopicFibreOptic sight_line: Fibre optic to add.
        """
    @property
    def origin(self) -> Point3D | list[Point3D]: ...
    @origin.setter
    def origin(self, value: Point3D | Sequence[Point3D]) -> None: ...
    @property
    def direction(self) -> Vector3D | list[Vector3D]: ...
    @direction.setter
    def direction(self, value: Vector3D | Sequence[Vector3D]) -> None: ...
    @property
    def display_progress(self) -> bool | list[bool]: ...
    @display_progress.setter
    def display_progress(self, value: bool | Sequence[bool]) -> None: ...
    @property
    def accumulate(self) -> bool | list[bool]: ...
    @accumulate.setter
    def accumulate(self, value: bool | Sequence[bool]) -> None: ...
    def connect_pipelines(  # type: ignore[override]
        self, properties: Sequence[tuple[type[Pipeline0D], str | None, SpectralFunction | None]] = ...
    ) -> None:
        """
        Connects pipelines of given kinds and names to each sight-line in the group.
        Connected pipelines are non-accumulating by default.

        :param list properties: 3-tuple list of pipeline properties in order (class, name, filter).
                                Default is [(SpectralRadiancePipeline0D, None, None)].
                                The following pipeline classes are supported:
                                    SpectralRadiacnePipeline0D,
                                    SpectralPowerPipeline0D,
                                    RadiacnePipeline0D,
                                    PowerPipeline0D.
                                Filters are applied to the mono pipelines only, namely,
                                PowerPipeline0D or RadiacnePipeline0D. The values provided for spectral
                                pipelines will be ignored. The filter must be an instance of
                                SpectralFunction or None.

        """
    def _get_same_pipelines(self, item: int | str) -> tuple[list[Pipeline0D], list[SpectroscopicFibreOptic | SpectroscopicSightLine]]: ...
    def plot_total_signal(self, item: int | str = 0, ax: object | None = None) -> object:
        """
        Plots total (wavelength-integrated) signal for each sight line in the group.

        :param str/int item: The index or name of the pipeline. Default: 0.
        :param Axes ax: Existing matplotlib axes.

        """
    def plot_spectra(self, item: int | str = 0, in_photons: bool = False, ax: object | None = None) -> object:
        """
        Plot the spectra observed by each line of sight in the group for a given pipeline.

        :param str/int item: The index or name of the pipeline. Default: 0.
        :param bool in_photons: If True, plots the spectrum in photon/s/nm instead of W/nm.
                                Default is False.
        :param Axes ax: Existing matplotlib axes.
        """

class SpectroscopicFibreOpticGroup(SpectroscopicObserver0DGroup, metaclass=ABCMeta):
    """
    .. deprecated:: 1.4.0
       Use FibreOpticGroup based on Raysect\'s FibreOptic observer instead.

    A group of fibre optics under a single scene-graph node.

    A scene-graph object regrouping a series of \'SpectroscopicFibreOptic\'
    observers as a scene-graph parent. Allows combined observation and display
    control simultaneously.

    :ivar list sight_lines: A list of fibre optics (SpectroscopicFibreOptic instances) in this
                            group.
    :ivar list/float acceptance_angle: The angle in degrees between the z axis and the cone
                                       surface which defines the fibres solid angle sampling
                                       area. The same value can be shared between all sight lines,
                                       or each sight line can be assigned with individual value.
    :ivar list/float radius: The radius of the fibre tip in metres. This radius defines a circular
                             area at the fibre tip which will be sampled over. The same value
                             can be shared between all sight lines, or each sight line can be
                             assigned with individual value.

    .. code-block:: pycon

       >>> from math import cos, sin, pi
       >>> from matplotlib import pyplot as plt
       >>> from raysect.optical import World
       >>> from raysect.optical.observer import SpectralPowerPipeline0D, PowerPipeline0D
       >>> from raysect.core.math import Point3D, Vector3D
       >>> from cherab.tools.observers import SpectroscopicFibreOptic, FibreOpticGroup
       >>>
       >>> world = World()
       ...
       >>> group = FibreOpticGroup(parent=world)
       >>> group.add_sight_line(SpectroscopicFibreOptic(Point3D(3., 0, 0), Vector3D(-cos(pi/10), 0, sin(pi/10)), name="Fibre 1"))
       >>> group.add_sight_line(SpectroscopicFibreOptic(Point3D(3., 0, 0), Vector3D(-1, 0, 0), name="Fibre 2"))
       >>> group.add_sight_line(SpectroscopicFibreOptic(Point3D(3., 0, 0), Vector3D(-cos(pi/10), 0, -sin(pi/10)), name="Fibre 3"))
       >>> group.connect_pipelines([(SpectralPowerPipeline0D, \'MySpectralPipeline\', None),
                                    (PowerPipeline0D, \'MyMonoPipeline\', None)])  # add pipelines to all fibres in the group
       >>> group.acceptance_angle = 2  # same value for all fibres in the group
       >>> group.radius = 2.e-3
       >>> group.spectral_bins = 512
       >>> group.pixel_samples = [2000, 1000, 2000]  # individual value for each fibre in the group
       >>> group.display_progress = False  # control pipeline parameters through the group observer
       >>> group.observe()  # combined observation
       >>> group.plot_spectra(item=\'MySpectralPipeline\', in_photons=True)  # plot the spectra
       >>> group.plot_total_signal(item=\'MyMonoPipeline\')  # plot the total signals
       >>> plt.show()
    """

    _OBSERVER_TYPE = SpectroscopicFibreOptic
    @property
    def acceptance_angle(self) -> list[float]: ...
    @acceptance_angle.setter
    def acceptance_angle(self, value: float | Sequence[float]) -> None: ...
    @property
    def radius(self) -> list[float]: ...
    @radius.setter
    def radius(self, value: float | Sequence[float]) -> None: ...

class SpectroscopicSightLineGroup(SpectroscopicObserver0DGroup, metaclass=ABCMeta):
    """
    .. deprecated:: 1.4.0
       Use SightLineGroup based on Raysect\'s SightLine observer instead.

    A group of spectroscopic sight-lines under a single scene-graph node.

    A scene-graph object regrouping a series of \'SpectroscopicSightLine\'
    observers as a scene-graph parent. Allows combined observation and display
    control simultaneously.

    :ivar list sight_lines: A list of lines of sight (SpectroscopicSightLine instances)
                            in this group.

    .. code-block:: pycon

       >>> from math import cos, sin, pi
       >>> from matplotlib import pyplot as plt
       >>> from raysect.optical import World
       >>> from raysect.optical.observer import SpectralRadiancePipeline0D, RadiancePipeline0D
       >>> from raysect.core.math import Point3D, Vector3D
       >>> from cherab.tools.observers import SpectroscopicSightLine, SightLineGroup
       >>>
       >>> world = World()
       ...
       >>> group = SightLineGroup(parent=world)
       >>> group.add_sight_line(SpectroscopicSightLine(Point3D(3., 0, 0), Vector3D(-cos(pi/10), 0, sin(pi/10)), name="SightLine 1"))
       >>> group.add_sight_line(SpectroscopicSightLine(Point3D(3., 0, 0), Vector3D(-1, 0, 0), name="SightLine 2"))
       >>> group.add_sight_line(SpectroscopicSightLine(Point3D(3., 0, 0), Vector3D(-cos(pi/10), 0, -sin(pi/10)), name="SightLine 3"))
       >>> group.connect_pipelines([(SpectralRadiancePipeline0D, \'MySpectralPipeline\', None),
                                    (RadiancePipeline0D, \'MyMonoPipeline\', None)])  # add pipelines to all sight lines in the group
       >>> group.spectral_bins = 512  # same value for all sight lines in the group
       >>> group.pixel_samples = [2000, 1000, 2000]  # individual value for each sight line in the group
       >>> group.display_progress = False  # control pipeline parameters through the group observer
       >>> group.observe()  # combined observation
       >>> group.plot_spectra(item=\'MySpectralPipeline\', in_photons=True)  # plot the spectra
       >>> group.plot_total_signal(item=\'MyMonoPipeline\')  # plot the total signals
       >>> plt.show()
    """

    _OBSERVER_TYPE = SpectroscopicSightLine
    @property
    def sensitivity(self) -> list[float]: ...
    @property  # type: ignore[override]
    def names(self) -> list[float]: ...  # pyrefly: ignore [bad-override]
    @names.setter  # type: ignore[override]
    def names(self, value: float | Sequence[float]) -> None: ...
