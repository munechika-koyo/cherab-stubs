from collections.abc import Sequence

from raysect.core.math import AffineMatrix3D, Point3D, Vector3D
from raysect.optical import SpectralFunction
from raysect.optical.observer import Pipeline0D

class _SpectroscopicObserver0DBase:
    """
    .. deprecated:: 1.4.0
       Use Raysect's observer classes instead.

    A base class for spectroscopic 0D observers.

    The observer allows to control some of the pipeline properties
    without accessing the pipelines. It has a built-in plotting method.

    Multiple spectroscopic 0D observers can be combined into a group.

    :ivar Point3D origin: The origin point of the sight line.
    :ivar Vector3D direction: The observation direction of the sight line.
    :ivar bool display_progress: Toggles the display of live render progress.
    :ivar bool accumulate: Toggles whether to accumulate samples with subsequent
                           calls to observe().

    """

    transform: AffineMatrix3D
    @property
    def origin(self) -> Point3D: ...
    @origin.setter
    def origin(self, value: Point3D) -> None: ...
    @property
    def direction(self) -> Vector3D: ...
    @direction.setter
    def direction(self, value: Vector3D) -> None: ...
    @property
    def display_progress(self) -> bool: ...
    @display_progress.setter
    def display_progress(self, value: bool) -> None: ...
    @property
    def accumulate(self) -> bool: ...
    @accumulate.setter
    def accumulate(self, value: bool) -> None: ...
    def get_pipeline(self, item: int | str = 0) -> Pipeline0D:
        """
        Gets a pipeline by its name or index.

        :param str/int item: The name of the pipeline or its index in the list.

        :rtype: Pipeline0D
        """
    pipelines: list[Pipeline0D]
    def connect_pipelines(self, properties: Sequence[tuple[type[Pipeline0D], str | None, SpectralFunction | None]] = ...) -> None:
        """
        Connects pipelines of given kinds and names to this sight line.
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
    def plot_spectrum(self, item: int | str = 0, in_photons: bool = False, ax: object | None = None, extras: bool = True) -> object:
        """
        Plot the observed spectrum for a given spectral pipeline.

        :param str/int item: The index or name of the pipeline. Default: 0.
        :param bool in_photons: If True, plots the spectrum in photon/s/nm instead of W/nm.
                                Default is False.
        :param Axes ax: Existing matplotlib axes.
        :param bool extras: If True, set title and axis labels.

        :rtype: matplotlib.pyplot.axes
        """
