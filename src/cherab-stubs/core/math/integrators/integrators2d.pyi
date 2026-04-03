from collections.abc import Callable

from raysect.core.math.function.float import Function2D

class Integrator2D:
    """
    Compute a definite integral of a two-dimensional function.

    :ivar Function2D integrand: A 2D function to integrate.
    """

    def __call__(self, x_lower: float, x_upper: float, y_lower: Function2D, y_upper: Function2D) -> float:
        """
        Integrates a two-dimensional function over a finite interval.

        :param float x_lower: Lower limit of integration in the x dimension.
        :param float x_upper: Upper limit of integration in the x dimension.
        :param Function2D y_lower: Lower limit of integration in the y dimension.
        :param Function2D y_upper: Upper limit of integration in the y dimension.

        :returns: Definite integral of a two-dimensional function.
        """

    @property
    def integrand(self) -> Function2D:
        """
        A 2D function to integrate.

        :rtype: Function2D
        """

    @integrand.setter
    def integrand(self, func: float | Function2D | Callable[[float, float], float]) -> None: ...
