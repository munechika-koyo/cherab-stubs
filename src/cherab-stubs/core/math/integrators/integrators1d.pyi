from collections.abc import Callable

from raysect.core.math.function.float import Constant1D, Function1D

ZERO_1D = Constant1D(0)

class Integrator1D:
    """
    Compute a definite integral of a one-dimensional function.

    :ivar Function1D integrand: A 1D function to integrate.
    """

    def __call__(self, a: float, b: float) -> float:
        """
        Integrates a one-dimensional function over a finite interval.

        :param float a: Lower limit of integration.
        :param float b: Upper limit of integration.

        :returns: Definite integral of a one-dimensional function.
        """

    @property
    def integrand(self) -> Function1D:
        """
        A 1D function to integrate.

        :rtype: Function1D
        """

    @integrand.setter
    def integrand(self, func: float | Function1D | Callable[[float], float]) -> None: ...

class GaussianQuadrature(Integrator1D):
    """
    Compute an integral of a one-dimensional function over a finite interval
    using fixed-tolerance Gaussian quadrature.
    (see Scipy `quadrature <https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quadrature.html>`).

    :param object integrand: A 1D function to integrate. Default is Constant1D(0).
    :param float relative_tolerance: Iteration stops when relative error between
        last two iterates is less than this value. Default is 1.e-5.
    :param int max_order: Maximum order on Gaussian quadrature. Default is 50.
    :param int min_order: Minimum order on Gaussian quadrature. Default is 1.

    :ivar Function1D integrand: A 1D function to integrate.
    :ivar float relative_tolerance: Iteration stops when relative error between
        last two iterates is less than this value.
    :ivar int max_order: Maximum order on Gaussian quadrature.
    :ivar int min_order: Minimum order on Gaussian quadrature.
    """

    def __init__(
        self,
        integrand: float | Function1D | Callable[[float], float] = ZERO_1D,
        relative_tolerance: float = 1.0e-5,
        max_order: int = 50,
        min_order: int = 1,
    ) -> None: ...
    @property
    def min_order(self) -> int:
        """
        Minimum order on Gaussian quadrature.

        :rtype: int
        """

    @min_order.setter
    def min_order(self, order: int) -> None: ...
    @property
    def max_order(self) -> int:
        """
        Maximum order on Gaussian quadrature.

        :rtype: int
        """

    @max_order.setter
    def max_order(self, order: int) -> None: ...
    @property
    def relative_tolerance(self) -> float:
        """
        Iteration stops when relative error between last two iterates is less than this value.

        :rtype: float
        """

    @relative_tolerance.setter
    def relative_tolerance(self, tolerance: float) -> None: ...
