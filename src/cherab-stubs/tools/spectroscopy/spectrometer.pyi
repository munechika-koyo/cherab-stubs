import numpy as np
from numpy.typing import ArrayLike, NDArray
from raysect.optical import Spectrum

from .instrument import SpectroscopicInstrument as SpectroscopicInstrument

class Spectrometer(SpectroscopicInstrument):
    """
    Spectrometer that can accommodate multiple spectra.

    Spectrometer is initialized with a sequence of calibration arrays (one array per accommodated
    spectrum) containing the wavelengths of the pixel borders. Namely, the values
    :math:`w_{k}^{i}` and :math:`w_{k}^{i+1}` define the spectral range of the pixel :math:`p_i`
    of the `k`-th spectrum. After the spectrum is ray-traced, it can be recalibrated with
    `spectrometer.calibrate(spectrum)`.

    Note that Raysect cannot raytrace the spectra with non-constant spectral resolution.
    Thus, the actual number of spectral bins of raytraced spectrum is defined with
    `min_bins_per_pixel` attribute.

    :param tuple wavelength_to_pixel: Wavelength-to-pixel calibration arrays.
    :param int min_bins_per_pixel: Minimal number of spectral bins
                                   per pixel. Default is 1.
    :param str name: Spectrometer name.

    :ivar tuple wavelengths: Central wavelengths of the pixels.

    .. code-block:: pycon

       >>> from raysect.optical import World, Spectrum
       >>> from raysect.optical.observer import FibreOptic
       >>> from cherab.tools.spectroscopy import Spectrometer
       >>> from matplotlib import pyplot as plt
       >>>
       >>> wavelength_to_pixel = ([400., 400.5, 401.5, 402., 404.],
       >>>                        [600., 600.5, 601.5, 602., 604., 607.])
       >>> spectrometer = Spectrometer(wavelength_to_pixel, min_bins_per_pixel=5,
       >>>                             name=\'MySpectrometer\')
       >>>
       >>> world = World()
       >>> fibreoptic = FibreOptic(name="MyFibreOptic", parent=world)
       >>> fibreoptic.min_wavelength = spectrometer.min_wavelength
       >>> fibreoptic.max_wavelength = spectrometer.max_wavelength
       >>> fibreoptic.spectral_bins = spectrometer.spectral_bins
       >>> fibreoptic.pipelines = spectrometer.create_pipelines()
       >>> ...
       >>> fibreoptic.observe()
       >>> spectrum = Spectrum(fibreoptic.min_wavelength, fibreoptic.max_wavelength, fibreoptic.spectral_bins)
       >>> spectrum.samples[:] = fibreoptic.pipelines[0].mean
       >>> calibrated_spectra = spectrometer.calibrate(spectrum)
       >>> wavelengths = spectrometer.wavelengths
       >>>
       >>> plt.plot(wavelengths[0], calibrated_spectra[0])
       >>> plt.show()
    """

    _wavelength_to_pixel: tuple[NDArray[np.float64], ...]
    _wavelengths: tuple[NDArray[np.float64], ...]
    _min_bins_per_pixel: int
    def __init__(self, wavelength_to_pixel: tuple[ArrayLike, ...], min_bins_per_pixel: int = 1, name: str = "") -> None: ...
    @property
    def wavelength_to_pixel(self) -> tuple[NDArray[np.float64], ...]: ...
    @wavelength_to_pixel.setter
    def wavelength_to_pixel(self, value: tuple[ArrayLike, ...]) -> None: ...
    @property
    def wavelengths(self) -> tuple[NDArray[np.float64], ...]: ...
    @property
    def min_bins_per_pixel(self) -> int: ...
    @min_bins_per_pixel.setter
    def min_bins_per_pixel(self, value: int) -> None: ...
    def _update_pipeline_classes(self) -> None: ...
    def _update_pipeline_kwargs(self) -> None: ...
    def _update_spectral_settings(self) -> None: ...
    def calibrate(self, spectrum: Spectrum) -> tuple[NDArray[np.float64], ...]:
        """
        Calibrates the spectrum according to the `wavelength_to_pixel` arrays
        by averaging it over the pixel widths.

        :param Spectrum spectrum: Spectrum to calibrate.

        :returns: A tuple of calibrated spectra as ndarrays.
        """

class CzernyTurnerSpectrometer(Spectrometer):
    """
    Czerny-Turner spectrometer.

    The Czerny-Turner spectrometer is initialized with the parameters of the diffraction scheme
    and a sequence of accommodated spectra, each of which is determined by the lower wavelength
    bound and the number of pixels.

    This spectrometer automatically fills the wavelength-to-pixel calibration arrays
    according to the parameters of the diffraction scheme.

    :param int diffraction_order: Diffraction order.
    :param float grating: Diffraction grating in nm-1.
    :param float focal_length: Focal length in nm.
    :param float pixel_spacing: Pixel to pixel spacing on CCD in nm.
    :param float diffraction_angle: Angle between incident and diffracted light in degrees.
    :param tuple accommodated_spectra: A sequence of (`min_wavelength`, `pixels`) pairs, specifying
                                       the lower wavelength bound and the number of pixels
                                       of accommodated spectra.
    :param int min_bins_per_pixel: Minimal number of spectral bins
                                   per pixel. Default is 1.
    :param str name: Spectrometer name.

    :ivar tuple wavelength_to_pixel: Wavelength-to-pixel calibration arrays.

    .. code-block:: pycon

       >>> from raysect.optical import World
       >>> from raysect.optical.observer import FibreOptic
       >>> from cherab.tools.spectroscopy import CzernyTurnerSpectrometer
       >>>
       >>> world = World()
       >>> hires_spectrometer = CzernyTurnerSpectrometer(1, 2.e-3, 1.e9, 2.e4, 10.,
       >>>                                               ((600., 512), (700., 128)),
       >>>                                               name=\'MySpectrometer\')
       >>> fibreoptic = FibreOptic(name="MyFibreOptic", parent=world)
       >>> fibreoptic.min_wavelength = hires_spectrometer.min_wavelength
       >>> fibreoptic.max_wavelength = hires_spectrometer.max_wavelength
       >>> fibreoptic.spectral_bins = hires_spectrometer.spectral_bins
       >>> fibreoptic.pipelines = hires_spectrometer.create_pipelines()
    """

    _accommodated_spectra: tuple[tuple[float, int], ...]
    _diffraction_order: int
    _grating: float
    _focal_length: float
    _pixel_spacing: float
    _diffraction_angle: float
    def __init__(
        self,
        diffraction_order: int,
        grating: float,
        focal_length: float,
        pixel_spacing: float,
        diffraction_angle: float,
        accommodated_spectra: tuple[tuple[float, int], ...],
        min_bins_per_pixel: int = 1,
        name: str = "",
    ) -> None: ...
    @property
    def diffraction_order(self) -> int: ...
    @diffraction_order.setter
    def diffraction_order(self, value: int) -> None: ...
    @property
    def grating(self) -> float: ...
    @grating.setter
    def grating(self, value: float) -> None: ...
    @property
    def focal_length(self) -> float: ...
    @focal_length.setter
    def focal_length(self, value: float) -> None: ...
    @property
    def pixel_spacing(self) -> float: ...
    @pixel_spacing.setter
    def pixel_spacing(self, value: float) -> None: ...
    @property
    def diffraction_angle(self) -> float: ...
    @diffraction_angle.setter
    def diffraction_angle(self, value: float) -> None: ...
    @property
    def accommodated_spectra(self) -> tuple[tuple[float, int], ...]: ...
    @accommodated_spectra.setter
    def accommodated_spectra(self, value: tuple[tuple[float, int], ...]) -> None: ...
    def _update_wavelength_to_pixel(self) -> None: ...
    @property  # type: ignore[misc]  # Runtime intentionally narrows this to read-only.
    def wavelength_to_pixel(  # pyrefly: ignore [bad-override]
        self,
    ) -> tuple[NDArray[np.float64], ...]: ...
    def resolution(self, wavelength: float) -> float:
        """
        Calculates spectral resolution in nm for a given wavelength.

        :param wavelength: Wavelength in nm.

        :returns: Resolution in nm.
        """
