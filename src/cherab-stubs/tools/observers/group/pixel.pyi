from abc import ABCMeta
from collections.abc import Sequence

from raysect.optical.observer import Pixel

from .base import Observer0DGroup as Observer0DGroup

class PixelGroup(Observer0DGroup, metaclass=ABCMeta):
    """
    A group of pixels under a single scene-graph node.

    A scene-graph object regrouping a series of 'Pixel'
    observers as a scene-graph parent. Allows combined observation and display
    control simultaneously.

    :ivar list x_width: Width of pixel along local x axis
    :ivar list y_width: Width of pixel along local y axis
    """

    _OBSERVER_TYPE = Pixel
    @property
    def x_width(self) -> list[float]: ...
    @x_width.setter
    def x_width(self, value: float | Sequence[float]) -> None: ...
    @property
    def y_width(self) -> list[float]: ...
    @y_width.setter
    def y_width(self, value: float | Sequence[float]) -> None: ...
