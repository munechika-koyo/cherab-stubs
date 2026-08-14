from abc import ABCMeta
from collections.abc import Mapping, Sequence
from typing import ClassVar

from raysect.core import AffineMatrix3D, Node
from raysect.core.scenegraph._nodebase import _NodeBase
from raysect.core.workflow import RenderEngine
from raysect.optical.observer import Observer0D
from raysect.optical.observer.base import Pipeline0D

class Observer0DGroup(Node, metaclass=ABCMeta):
    """
    A base class for handling groups of nonimaging observers as one Node.

    A scene-graph object regrouping a series of observers as a scene-graph parent.
    Allows combined observation and display control simultaneously.
    Note that for any property except `names` and `pipelines`, the same value can be shared between
    all observers, or each observer can be assigned with individual value.

    :ivar list names: A list of observer names.
    :ivar list/RenderEngine render_engine: Rendering engine used by the observers.
                                           Note that if the engine is shared, changing its
                                           parameters for one observer in a group will affect
                                           all observers.
    :ivar list/int spectral_bins: The number of spectral samples over the wavelength range.
    :ivar list/int spectral_rays: The number of smaller sub-spectrum rays the full spectrum will be divided into.
    :ivar list/float max_wavelength: Upper wavelength bound for sampled spectral range.
    :ivar list/float min_wavelength: Lower wavelength bound for sampled spectral range.
    :ivar list/float ray_extinction_prob: Probability of ray extinction after every material intersection.
    :ivar list/int ray_max_depth: Maximum number of Ray paths before terminating Ray.
    :ivar list/float ray_extinction_min_depth: Minimum number of paths before russian roulette style ray extinction.
    :ivar list/bool ray_importance_sampling: Toggle importance sampling behaviour (default=True).
    :ivar list/float ray_important_path_weight: Relative weight of important path sampling.
    :ivar list/int pixel_samples: The number of samples to take per pixel.
    :ivar list/int samples_per_task: Minimum number of samples to request per task.
    :ivar list pipelines: A list of all pipelines connected to each observer in the group.
    """

    _OBSERVER_TYPE: ClassVar[type[Observer0D]] = Observer0D
    _observers: list[Observer0D]
    def __init__(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
        observers: Sequence[Observer0D] | None = None,
    ) -> None: ...
    def __getitem__(self, item: int) -> Observer0D: ...
    def __len__(self) -> int: ...
    @property
    def observers(self) -> tuple[Observer0D, ...]:
        """
        A list of all observer object assigned to the group.
        The group is set as a parent to any added observer.

        :rtype: tuple
        """
    @observers.setter
    def observers(self, value: Sequence[Observer0D]) -> None: ...
    def add_observer(self, observer: Observer0D) -> None:
        """Adds new observer to the group."""
    @property
    def names(self) -> list[str]:
        """A list of observer names."""
    @names.setter
    def names(self, value: Sequence[str]) -> None: ...
    def observe(self) -> None:
        """Starts the observation."""
    @property
    def render_engine(self) -> RenderEngine | list[RenderEngine]:
        """
        Rendering engine used by the observers.
        :rtype: list
        """
    @render_engine.setter
    def render_engine(self, value: RenderEngine | Sequence[RenderEngine]) -> None: ...
    @property
    def spectral_bins(self) -> int | list[int]: ...
    @spectral_bins.setter
    def spectral_bins(self, value: int | Sequence[int]) -> None: ...
    @property
    def spectral_rays(self) -> int | list[int]: ...
    @spectral_rays.setter
    def spectral_rays(self, value: int | Sequence[int]) -> None: ...
    @property
    def max_wavelength(self) -> float | list[float]: ...
    @max_wavelength.setter
    def max_wavelength(self, value: float | Sequence[float]) -> None: ...
    @property
    def min_wavelength(self) -> float | list[float]: ...
    @min_wavelength.setter
    def min_wavelength(self, value: float | Sequence[float]) -> None: ...
    @property
    def ray_extinction_prob(self) -> float | list[float]: ...
    @ray_extinction_prob.setter
    def ray_extinction_prob(self, value: float | Sequence[float]) -> None: ...
    @property
    def ray_max_depth(self) -> int | list[int]: ...
    @ray_max_depth.setter
    def ray_max_depth(self, value: int | Sequence[int]) -> None: ...
    @property
    def ray_extinction_min_depth(self) -> int | list[int]: ...
    @ray_extinction_min_depth.setter
    def ray_extinction_min_depth(self, value: int | Sequence[int]) -> None: ...
    @property
    def ray_importance_sampling(self) -> bool | list[bool]: ...
    @ray_importance_sampling.setter
    def ray_importance_sampling(self, value: bool | Sequence[bool]) -> None: ...
    @property
    def ray_important_path_weight(self) -> float | list[float]: ...
    @ray_important_path_weight.setter
    def ray_important_path_weight(self, value: float | Sequence[float]) -> None: ...
    @property
    def quiet(self) -> bool | list[bool]: ...
    @quiet.setter
    def quiet(self, value: bool | Sequence[bool]) -> None: ...
    @property
    def pixel_samples(self) -> int | list[int]: ...
    @pixel_samples.setter
    def pixel_samples(self, value: int | Sequence[int]) -> None: ...
    @property
    def samples_per_task(self) -> int | list[int]: ...
    @samples_per_task.setter
    def samples_per_task(self, value: int | Sequence[int]) -> None: ...
    @property
    def pipelines(self) -> list[list[Pipeline0D]]:
        """
        A list of all pipelines connected to each observer in the group

        :param list pipelist: list of lists/tuples of already instantiated pipelines
        :rtype: list
        """
    @pipelines.setter
    def pipelines(self, pipelist: Sequence[Sequence[Pipeline0D]]) -> None: ...
    def connect_pipelines(
        self,
        pipeline_classes: Sequence[type[Pipeline0D]],
        keywords_list: Sequence[Mapping[str, object]] | None = None,
        suppress_display_progress: bool = True,
    ) -> None:
        """
        Creates and connects a new set of given pipelines to each observer in the group.

        Pipeline classes are instantiated using parameters specified in appropriate dict from keywords list.
        If keywords list is provided, it length must match the number of provided pipeline classes.

        :param list pipeline_classes: list of pipeline classes to be connected with observers
        :param list keywords_list: list of dicts with keywords passed to init methods of pipeline classes
                                   its length must match the number of pipeline classes
                                   for default parameters place an empty dict to appropriate place in the list
        :param bool suppress_display_progress: Toggles setting display_progress to False for each compatible pipeline (default=True)

        .. code-block:: pycon

          ...
          >>> pipelines = [SpectralRadiancePipeline0D, RadiancePipeline0D]
          >>> keywords = [{'name': 'MySpectralPipeline'}, {}]
          >>> group.connect_pipelines(pipeline_classes=pipelines, keywords_list=keywords)
        """
