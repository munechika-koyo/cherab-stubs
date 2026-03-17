from raysect.core.math import Point3D, Vector3D
from raysect.optical.spectrum import Spectrum

from ..atomic import AtomicData
from .node import Plasma

class PlasmaModel:
    """
    A plasma emission model.

    When attached to a plasma, a plasma emission model samples the plasma properties
    and atomic data it needs to calculate its emission. The emission is calculated
    for a particular point and viewing orientation in plasma space.

    A new emission model is implemented by inheriting from this class and specifying
    the emission() function.

    If it is necessary to cache data to speed up the emission
    calculation and there is a risk the cached data may be made stale by changes to the
    plasma, the _change() method must be implemented to reset the cache. The _change()
    function is automatically called when changes occur on the Plasma object.

    The plasma and atomic data provider attributes will be automatically populated
    when the PlasmaModel is attached to the Plasma object. In general these should
    not be set by the user directly.

    :ivar Plasma plasma: The plasma to which this emission model is attached.
    :ivar AtomicData atomic_data: The atomic data provider for this model.
    """

    _plasma: Plasma | None
    _atomic_data: AtomicData | None

    def __init__(
        self, plasma: Plasma | None = None, atomic_data: AtomicData | None = None
    ) -> None: ...
    @property
    def plasma(self) -> Plasma: ...
    @plasma.setter
    def plasma(self, value: Plasma) -> None: ...
    @property
    def atomic_data(self) -> AtomicData: ...
    @atomic_data.setter
    def atomic_data(self, value: AtomicData) -> None: ...
    def emission(self, point: Point3D, direction: Vector3D, spectrum: Spectrum) -> Spectrum:
        """
        Calculate the emission for a point in the plasma in a specified direction.

        Models implementing this method must add their spectral response to the
        supplied spectrum object. The spectrum units are spectral radiance per
        meter (W/m^3/str/nm).

        If a model has a directional response, the model should pass through
        its own reference axis e.g. Thomsen scattering laser direction.

        :param point: Point in plasma space.
        :param direction: Direction in plasma space.
        :param spectrum: Spectrum to which emission should be added.
        :return: Updated Spectrum object.
        """

    def _change(self) -> None:
        """
        Call if the plasma properties or the atomic data source changes.

        If the model caches calculation data that would be invalidated if its
        source data changes then this method may be overridden to clear the
        cache.

        This method is triggered if the plasma notifies the model of a change
        or the atomic data source is changed.
        """
