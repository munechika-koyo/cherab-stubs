import numpy as np
from numpy.typing import ArrayLike, NDArray

class FreeFreeGauntFactor:
    """
    The base class for temperature-averaged free-free Gaunt factors.
    """
    def __call__(self, z: float, temperature: float, wavelength: float) -> float:
        """
        Return the temperature-averaged free-free Gaunt factor for the supplied parameters.

        :param double z: Species charge or effective plasma charge.
        :param double temperature: Electron temperature in eV.
        :param double wavelength: Spectral wavelength.

        :return: free-free Gaunt factor
        """

class InterpolatedFreeFreeGauntFactor(FreeFreeGauntFactor):
    """
    The temperature-averaged free-free Gaunt factors interpolated in the space of parameters:
    :math:`u = h{\\nu}/kT` and :math:`{\\gamma}^{2} = Z^{2}Ry/kT`.
    See T.R. Carson, 1988, Astron. & Astrophys., 189,
    `319 <https://ui.adsabs.harvard.edu/#abs/1988A&A...189..319C/abstract>`_ for details.

    The cubic interpolation in a semi-log space is used.

    The Born approximation is used outside the interpolation range.

    :param object u: A 1D array-like object of real values.
    :param object gamma2: A 1D array-like object of real values.
    :param object gaunt_factor: 2D array-like object of real values
                                storing the Gaunt factor values at u, gamma2.

    :ivar tuple u_range: The interpolation range of `u` parameter.
    :ivar tuple gamma2_range: The interpolation range of :math:`\\\\gamma^2` parameter.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    u_range: tuple[float, float]
    gamma2_range: tuple[float, float]
    raw_data: dict[str, NDArray[np.float64]]

    def __init__(self, u: ArrayLike, gamma2: ArrayLike, gaunt_factor: ArrayLike) -> None: ...

class MaxwellianFreeFreeGauntFactor(InterpolatedFreeFreeGauntFactor):
    """
    The Maxwellian-averaged free-free Gaunt factor interpolated over the data from Table A.1 in
    M.A. de Avillez and D. Breitschwerdt, "Temperature-averaged and total free-free Gaunt factors
    for κ and Maxwellian distributions of electrons", 2015, Astron. & Astrophys. 580,
    `A124 <https://www.aanda.org/articles/aa/full_html/2015/08/aa26104-15/aa26104-15.html>`_.

    The Born approximation is used outside the interpolation range.
    """
    def __init__(self) -> None: ...
