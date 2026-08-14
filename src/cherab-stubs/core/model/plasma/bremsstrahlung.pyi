from numpy.typing import ArrayLike
from raysect.core.math import Point3D, Vector3D
from raysect.core.math.function.float.function1d.base import Function1D
from raysect.optical import Spectrum

from ...atomic import AtomicData, FreeFreeGauntFactor
from ...math.integrators import Integrator1D
from ...plasma import Plasma
from ...plasma.model import PlasmaModel

class BremsFunction(Function1D):
    """
    Calculates bremsstrahlung spectrum.

    :param FreeFreeGauntFactor gaunt_factor: Free-free Gaunt factor as a function of Z, Te and
                                             wavelength.
    :param object species_density: Array-like object with ions' density in m-3.
    :param object species_charge: Array-like object with ions' charge.
    :param double ne: Electron density in m-3.
    :param double te: Electron temperature in eV.
    """

    def __init__(
        self,
        gaunt_factor: FreeFreeGauntFactor,
        species_density: ArrayLike,
        species_charge: ArrayLike,
        ne: float,
        te: float,
    ) -> None: ...

class Bremsstrahlung(PlasmaModel):
    r"""
    Emitter that calculates bremsstrahlung emission from a plasma object.

    The bremmstrahlung formula implemented is equation 5.3.40
    from I. H. Hutchinson, 'Principles of Plasma Diagnostics', second edition,
    Cambridge University Press, 2002, ISBN: 9780511613630,
    https://doi.org/10.1017/CBO9780511613630

    Note that in eq. 5.3.40, the emissivity :math:`j(\nu)` is given in (W/m^3/sr/Hz) with respect
    to frequency, :math:`\nu`. Here, the emissivity :math:`\epsilon_{\mathrm{ff}}(\lambda)`
    is given in (W/m^3/nm/sr) with respect to wavelength, :math:`\lambda = \frac{10^{9} c}{\nu}`,
    and taking into account that :math:`d\nu=-\frac{10^{9} c}{\lambda^2}d\lambda`.

    .. math::
        \epsilon_{\mathrm{ff}}(\lambda) = \left( \frac{e^2}{4 \pi \varepsilon_0} \right)^3
        \frac{32 \pi^2}{3 \sqrt{3} m_\mathrm{e}^2 c^3}
        \sqrt{\frac{2 m_\mathrm{e}^3}{\pi e T_\mathrm{e}}}
        \frac{10^{9} c}{4 \pi \lambda^2}
        n_\mathrm{e} \sum_i \left( n_\mathrm{i} g_\mathrm{ff} (Z_\mathrm{i}, T_\mathrm{e}, \lambda) Z_\mathrm{i}^2 \right)
        \mathrm{e}^{-\frac{10^9 hc}{e T_\mathrm{e} \lambda}},

    where :math:`T_\mathrm{e}` is in eV and :math:`\lambda` is in nm.

    :math:`g_\mathrm{ff} (Z_\mathrm{i}, T_\mathrm{e}, \lambda)` is the free-free Gaunt factor.

    :ivar Plasma plasma: The plasma to which this emission model is attached. Default is None.
    :ivar AtomicData atomic_data: The atomic data provider for this model. Default is None.
    :ivar FreeFreeGauntFactor gaunt_factor: Free-free Gaunt factor as a function of Z, Te and
                                            wavelength. If not provided,
                                            the `atomic_data` is used.
    :ivar Integrator1D integrator: Integrator1D instance to integrate Bremsstrahlung radiation
                                   over the spectral bin. Default is `GaussianQuadrature`.
    """
    def __init__(
        self,
        plasma: Plasma | None = None,
        atomic_data: AtomicData | None = None,
        gaunt_factor: FreeFreeGauntFactor | None = None,
        integrator: Integrator1D | None = None,
    ) -> None: ...
    @property
    def gaunt_factor(self) -> FreeFreeGauntFactor: ...
    @gaunt_factor.setter
    def gaunt_factor(self, value: FreeFreeGauntFactor) -> None: ...
    @property
    def integrator(self) -> Integrator1D: ...
    @integrator.setter
    def integrator(self, value: Integrator1D) -> None: ...
    def emission(self, point: Point3D, direction: Vector3D, spectrum: Spectrum) -> Spectrum: ...
    def _change(self) -> None: ...
