from collections.abc import Sequence

from numpy.typing import ArrayLike
from raysect.optical import InterpolatedSF

from .instrument import SpectroscopicInstrument as SpectroscopicInstrument

class PolychromatorFilter(InterpolatedSF):
    """
    Defines a polychromator filter as a Raysect\'s InterpolatedSF.

    :param object wavelengths: 1D array of wavelengths in nanometers.
    :param object samples: 1D array of spectral samples.
    :param bool normalise: True/false toggle for whether to normalise the
                           spectral function so its integral equals 1.
    :param str name: Filter name (e.g. "H-alpha filter"). Default is \'\'.

    :ivar float min_wavelength: Lower wavelength bound of the filter\'s spectral range in nm.
    :ivar float max_wavelength: Upper wavelength bound of the filter\'s spectral range in nm.
    """

    _min_wavelength: float
    _max_wavelength: float
    _window: float
    _central_wavelength: float
    _name: str
    def __init__(self, wavelengths: ArrayLike, samples: ArrayLike, normalise: bool = False, name: str = "") -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def min_wavelength(self) -> float: ...
    @property
    def max_wavelength(self) -> float: ...
    @property
    def window(self) -> float: ...
    @property
    def central_wavelength(self) -> float: ...

class TrapezoidalFilter(PolychromatorFilter):
    """
    Symmetrical trapezoidal polychromator filter.

    :param float wavelength: Central wavelength of the filter in nm.
    :param float window: Size of the filtering window in nm. Default is 3.
    :param float flat_top: Size of the flat top part of the filter in nm.
                           Default is None (equal to window).
    :param str name: Filter name (e.g. "H-alpha filter"). Default is \'\'.
    """

    _flat_top: float
    def __init__(self, central_wavelength: float, window: float = 3.0, flat_top: float | None = None, name: str = "") -> None: ...
    @property
    def flat_top(self) -> float: ...

class Polychromator(SpectroscopicInstrument):
    """
    A polychromator assembly with a set of different filters.

    :param list filters: List of the `PolychromatorFilter` instances.
    :param int min_bins_per_window: Minimal number of spectral bins
                                    per filtering window. Default is 10.
    :param str name: Polychromator name.

    .. code-block:: pycon

       >>> from raysect.optical import World
       >>> from raysect.optical.observer import FibreOptic
       >>> from cherab.tools.spectroscopy import Polychromator, TrapezoidalFilter
       >>>
       >>> world = World()
       >>> h_alpha_filter = TrapezoidalFilter(656.1, name=\'H-alpha filter\')
       >>> ciii_465nm_filter = TrapezoidalFilter(464.8, name=\'CIII 465 nm filter\')
       >>> polychromator = Polychromator([h_alpha_filter, ciii_465nm_filter], name=\'MyPolychromator\')
       >>> fibreoptic = FibreOptic(name="MyFibreOptic", parent=world)
       >>> fibreoptic.min_wavelength = polychromator.min_wavelength
       >>> fibreoptic.max_wavelength = polychromator.max_wavelength
       >>> fibreoptic.spectral_bins = polychromator.spectral_bins
       >>> fibreoptic.pipelines = polychromator.create_pipelines()
    """

    _min_bins_per_window: int
    _filters: tuple[PolychromatorFilter, ...]
    def __init__(self, filters: Sequence[PolychromatorFilter], min_bins_per_window: int = 10, name: str = "") -> None: ...
    @property
    def min_bins_per_window(self) -> int: ...
    @min_bins_per_window.setter
    def min_bins_per_window(self, value: int) -> None: ...
    @property
    def filters(self) -> tuple[PolychromatorFilter, ...]: ...
    @filters.setter
    def filters(self, value: Sequence[PolychromatorFilter]) -> None: ...
    def _update_pipeline_classes(self) -> None: ...
    def _update_pipeline_kwargs(self) -> None: ...
    def _update_spectral_settings(self) -> None: ...
