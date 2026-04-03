from collections.abc import Callable

from raysect.core.math.function.float import Function2D

def auto_caching2d_optimiser(
    function2d: float | Function2D | Callable[[float, float], float],
    space_area: tuple[float, float, float, float],
    threshold: float,
) -> tuple[float, float]:
    """
    Find the biggest resolution of the caching of function2d allowing a mean
    relative error less than a threshold.
    Also plot a graph with the resolutions tested and their errors.
    :param function2d: the 2D function to cache
    :param space_area: area where the function has to be cached: (minx, maxx, miny, maxy)
    :param threshold: maximum mean relative error wanted
    :return: a tuple of resolutions (resolutionx, resolutiony)
    """

def mapping_caching2d_resolution(
    function2d: float | Function2D | Callable[[float, float], float],
    space_area: tuple[float, float, float, float],
) -> None:
    """
    Plot a map of the mean relative error when caching function2d with different resolutions.
    :param function2d: 2D function to be cached
    :param space_area: area where the function has to be cached: (minx, maxx, miny, maxy)
    """
