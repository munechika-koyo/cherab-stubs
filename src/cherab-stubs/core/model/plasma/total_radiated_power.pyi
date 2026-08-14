from raysect.core.math import Point3D, Vector3D
from raysect.optical import Spectrum

from ...atomic import AtomicData, Element
from ...atomic.elements import Isotope
from ...plasma import Plasma
from ...plasma.model import PlasmaModel

deuterium: Isotope
hydrogen: Element
tritium: Isotope

class TotalRadiatedPower(PlasmaModel):
    r"""
    Emitter that calculates total power radiated by a given ion, which includes:

    - line power due to electron impact excitation,
    - continuum and line power due to recombination and Bremsstrahlung,
    - line power due to charge exchange with thermal neutral hydrogen and its isotopes.

    The emission calculated by this model is spectrally unresolved,
    which means that the total radiated power will be spread of the entire
    observable spectral range.

    .. math::
        \epsilon_{\mathrm{total}} = \frac{1}{4 \pi \Delta\lambda} \left(
        n_{Z_\mathrm{i}} n_\mathrm{e} C_{\mathrm{excit}}(n_\mathrm{e}, T_\mathrm{e}) +
        n_{Z_\mathrm{i} + 1} n_\mathrm{e} C_{\mathrm{recomb}}(n_\mathrm{e}, T_\mathrm{e}) +
        n_{Z_\mathrm{i} + 1} n_\mathrm{hyd} C_{\mathrm{cx}}(n_\mathrm{e}, T_\mathrm{e}) \right)

    where :math:`n_{Z_\mathrm{i}}` is the target species density;
    :math:`n_{Z_\mathrm{i} + 1}` is the recombining species density;
    :math:`n_{\mathrm{hyd}}` is the total density of all hydrogen isotopes;
    :math:`C_{\mathrm{excit}}, C_{\mathrm{recomb}}, C_{\mathrm{cx}}` are the radiated power
    coefficients in :math:`W m^3` due to electron impact excitation, recombination
    + Bremsstrahlung and charge exchange with thermal neutral hydrogen, respectively;
    :math:`\Delta\lambda` is the observable spectral range.

    :param Element element: The atomic element/isotope.
    :param int charge: The charge state of the element/isotope.
    :param Plasma plasma: The plasma to which this emission model is attached. Default is None.
    :param AtomicData atomic_data: The atomic data provider for this model. Default is None.
    """

    def __init__(self, element: Element, charge: int, plasma: Plasma | None = None, atomic_data: AtomicData | None = None) -> None: ...
    def emission(self, point: Point3D, direction: Vector3D, spectrum: Spectrum) -> Spectrum: ...
    def _change(self) -> None: ...
