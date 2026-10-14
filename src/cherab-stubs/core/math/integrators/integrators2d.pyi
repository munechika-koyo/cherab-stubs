from collections.abc import Callable

from raysect.core.math.function.float import Function1D, Function2D

class Integrator2D:
    """
    Compute a definite integral of a two-dimensional function.

    :ivar Function2D integrand: A 2D function to integrate.
    """

    @property
    def integrand(self) -> Function2D:
        """
        A 2D function to integrate.

        :rtype: Function2D
        """

    @integrand.setter
    def integrand(self, func: float | Function2D | Callable[[float, float], float]) -> None: ...
    def __call__(self, x_lower: float, x_upper: float, y_lower: Function1D, y_upper: Function1D):
        """
        Integrates a two-dimensional function over a finite interval.

        :param double x_lower: Lower limit of integration in the x dimension.
        :param double x_upper: Upper limit of integration in the x dimension.
        :param Function1D y_lower: Lower limit of integration in the y dimension.
        :param Function1D y_upper: Upper limit of integration in the y dimension.

        :returns: Definite integral of a two-dimensional function.
        """

class GaussianQuadrature2D(Integrator2D):
    r"""
    Approximates an integral of a two-dimensional function over a finite interval.

    The integral is approximated with fixed-tolerance Gauss-Legendre quadrature.
    The quadrature approximation is calculated as follows:

    .. math::
        \int_{x_{\mathrm{lower}}}^{x_{\mathrm{upper}}} \int_{y_{\mathrm{lower}}(x)}^{y_{\mathrm{upper}}(x)} f(x, y) \, dy \, dx
        \approx \sum_{i=1}^{n_x} \sum_{j=1}^{n_y} w_{i} w_{j} \,
        f\left( B \xi_i + A, \, D(x) \eta_j + C(x) \right) \,
        B \cdot D(x)

    where:
        -  :math:`x_{\mathrm{lower}}`: Lower limit of integration for the x-dimension.
        -  :math:`x_{\mathrm{upper}}`: Upper limit of integration for the x-dimension.
        -  :math:`y_{\mathrm{lower}}(x)`: Lower limit of integration for the y-dimension, a function of :math:`x`.
        -  :math:`y_{\mathrm{upper}}(x)`: Upper limit of integration for the y-dimension, a function of :math:`x`.
        -  :math:`f(x, y)`: The function to be integrated over the specified region.
        -  :math:`\xi`: The transformed variable for the x-dimension, ranging from -1 to 1.
        -  :math:`\eta`: The transformed variable for the y-dimension, ranging from -1 to 1.
        -  :math:`w_i`: The weight corresponding to the :math:`i`-th root of the Legendre polynomial in the x-dimension.
        -  :math:`w_j`: The weight corresponding to the :math:`j`-th root of the Legendre polynomial in the y-dimension.
        -  :math:`\xi_i`: The :math:`i`-th root of the Legendre polynomial in the x-dimension.
        -  :math:`\eta_j`: The :math:`j`-th root of the Legendre polynomial in the y-dimension.
        -  :math:`n_x`: The number of roots (or nodes) in the x-dimension.
        -  :math:`n_y`: The number of roots (or nodes) in the y-dimension.
        -  :math:`A = \frac{x_{\mathrm{upper}} + x_{\mathrm{lower}}}{2}`: Midpoint of the x-interval.
        -  :math:`B = \frac{x_{\mathrm{upper}} - x_{\mathrm{lower}}}{2}`: Half-width of the x-interval.
        -  :math:`D(x) = \frac{y_{\mathrm{upper}}(x) - y_{\mathrm{lower}}(x)}{2}`: Half-width of the y-interval.
        -  :math:`C(x) = \frac{y_{\mathrm{upper}}(x) + y_{\mathrm{lower}}(x)}{2}`: Midpoint of the y-interval.

    The integration is performed by iteratively increasing the order of the Gaussian quadrature in both the x and y dimensions until the relative tolerance is met or the maximum orders are reached.

    :param Function2D integrand: A 2D function to integrate. Default is `Constant2D(0)`.
    :param double relative_tolerance: Iteration stops when relative error between
        last two iterates is less than this value. Default is `1.e-5`.
    :param int x_max_order: Maximum order on Gaussian quadrature in the x dimension the integration stops at. Default is `50`.
    :param int x_min_order: Minimum order on Gaussian quadrature in the x dimension the integration starts from. Default is `1`.
    :param int y_max_order: Maximum order on Gaussian quadrature in the y dimension the integration stops at. Default is `50`.
    :param int y_min_order: Minimum order on Gaussian quadrature in the y dimension the integration starts from. Default is `1`.

    :ivar Function1D integrand: A 1D function to integrate.
    :ivar double relative_tolerance: Iteration stops when relative error between
        last two iterates is less than this value.
    :ivar int x_max_order: Maximum order on Gaussian quadrature in the x dimension the integration stops at.
    :ivar int x_min_order: Minimum order on Gaussian quadrature in the x dimension the integration starts from.
    :ivar int y_max_order: Maximum order on Gaussian quadrature in the y dimension the integration stops at.
    :ivar int y_min_order: Minimum order on Gaussian quadrature in the y dimension the integration starts from.
    """
    def __init__(
        self,
        integrand: float | Function2D | Callable[[float, float], float] = ...,
        relative_tolerance: float = 1.0e-5,
        x_max_order: int = 50,
        x_min_order: int = 1,
        y_max_order: int = 50,
        y_min_order: int = 1,
    ) -> None: ...
    @property
    def x_min_order(self) -> int:
        """
        Minimum order on Gaussian quadrature in the x dimension.

        :rtype: int
        """
    @x_min_order.setter
    def x_min_order(self, value: int) -> None: ...
    @property
    def x_max_order(self) -> int:
        """
        Maximum order on Gaussian quadrature in the x dimension.

        :rtype: int
        """
    @x_max_order.setter
    def x_max_order(self, value: int) -> None: ...
    @property
    def y_min_order(self) -> int:
        """
        Minimum order on Gaussian quadrature in the y dimension.

        :rtype: int
        """
    @y_min_order.setter
    def y_min_order(self, value: int) -> None: ...
    @property
    def y_max_order(self) -> int:
        """
        Maximum order on Gaussian quadrature in the y dimension.

        :rtype: int
        """
    @y_max_order.setter
    def y_max_order(self, value: int) -> None: ...
    @property
    def relative_tolerance(self) -> float:
        """
        Iteration stops when relative error between last two iterates is less than this value.

        :rtype: double
        """
    @relative_tolerance.setter
    def relative_tolerance(self, value: float) -> None: ...
