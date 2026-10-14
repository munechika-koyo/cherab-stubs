from collections.abc import Sequence

import numpy as np
from numpy.typing import NDArray
from raysect.core import Primitive
from raysect.optical.observer import TargetedPixel

from .base import Observer0DGroup

class TargetedPixelGroup(Observer0DGroup):
    """
    A group of targeted pixels under a single scene-graph node.

    A scene-graph object regrouping a series of 'TargetedPixel'
    observers as a scene-graph parent. Allows combined observation and display
    control simultaneously.

    :ivar list x_width: Width of pixel along local x axis
    :ivar list y_width: Width of pixel along local y axis
    :ivar list targets: Targets for preferential sampling
    :ivar list targeted_path_prob: Probability of ray being casted at the target
    """

    _OBSERVER_TYPE = TargetedPixel

    @property
    def x_width(self) -> list[float]: ...
    @x_width.setter
    def x_width(self, value: Sequence[float] | NDArray[np.float64] | float) -> None: ...
    @property
    def y_width(self) -> list[float]: ...
    @y_width.setter
    def y_width(self, value: Sequence[float] | NDArray[np.float64] | float) -> None: ...
    @property
    def targets(self) -> list[list[Primitive]]:
        """
        List of target lists used by pixels for preferential sampling

        :param list value: List of primitives to be set to each pixel or
                           list of lists containing targets specific for each pixel
                           in this case the number of lists must match number of pixels

        :rtype: list
        """

    @targets.setter
    def targets(self, value: Sequence[Primitive] | Sequence[Sequence[Primitive]]) -> None: ...
    @property
    def targeted_path_prob(self) -> list[float]: ...
    @targeted_path_prob.setter
    def targeted_path_prob(self, value: Sequence[float] | float) -> None: ...
