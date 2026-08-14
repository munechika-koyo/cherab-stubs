from raysect.optical.observer import Pipeline0D

class SpectroscopicInstrument:
    """
    Base class for spectroscopic instruments (spectrometers, polychromators, etc.).
    This is an abstract class.

    :param str name: Instrument name.

    :ivar list pipeline_classes: The list of pipeline classes used with this instrument.
    :ivar list pipeline_kwargs: The list of dicts with keywords passed to init methods of
                                pipeline classes used with this instrument.
    :ivar float min_wavelength: Lower wavelength bound for spectral range.
    :ivar float max_wavelength: Upper wavelength bound for spectral range.
    :ivar int spectral_bins: The number of spectral samples over the wavelength range.
    """

    _pipeline_classes: tuple[type[Pipeline0D], ...]
    _name: str
    _pipeline_kwargs: tuple[dict[str, object], ...]
    def __init__(self, name: str = "") -> None: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def pipeline_classes(self) -> tuple[type[Pipeline0D], ...]: ...
    @property
    def pipeline_kwargs(self) -> tuple[dict[str, object], ...]: ...
    def create_pipelines(self) -> list[Pipeline0D]:
        """Returns a list of new pipelines created according to `pipeline_classes`
        and keyword arguments."""
    @property
    def min_wavelength(self) -> float: ...
    @property
    def max_wavelength(self) -> float: ...
    @property
    def spectral_bins(self) -> int: ...
    _min_wavelength: float
    _max_wavelength: float
    _spectral_bins: int
    def _clear_spectral_settings(self) -> None: ...
    def _update_spectral_settings(self) -> None: ...
    def _update_pipeline_classes(self) -> None: ...
    def _update_pipeline_kwargs(self) -> None: ...
