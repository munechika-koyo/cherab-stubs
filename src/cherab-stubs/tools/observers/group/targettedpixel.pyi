from collections.abc import Sequence

from .targetedpixel import TargetedPixelGroup as _TargetedPixelGroup

class TargettedPixelGroup(_TargetedPixelGroup):
    """
    A group of targeted pixel under a single scene-graph node.

    .. deprecated::
        `TargettedPixelGroup` is deprecated and will be removed in version 2.0.
        Use `TargetedPixelGroup` instead.

    A scene-graph object regrouping a series of `TargetedPixel`
    observers as a scene-graph parent. Allows combined observation and display
    control simultaneously.

    :ivar list x_width: Width of pixel along local x axis
    :ivar list y_width: Width of pixel along local y axis
    :ivar list targets: Targets for preferential sampling
    :ivar list targetted_path_prob: Probability of ray being casted at the target
    """

    @property
    def targetted_path_prob(self) -> list[float]: ...
    @targetted_path_prob.setter
    def targetted_path_prob(self, value: Sequence[float]) -> None: ...
