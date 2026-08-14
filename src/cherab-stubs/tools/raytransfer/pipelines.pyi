import numpy as np
from numpy.typing import NDArray
from raysect.optical import Spectrum
from raysect.optical.observer.base import Pipeline0D, Pipeline1D, Pipeline2D, PixelProcessor, SpectralSlice

class RayTransferPipelineBase:
    name: str
    _matrix: NDArray[np.float64]
    _samples: int
    _bins: int
    _kind: str
    def __init__(self, name: str | None = None, kind: str = "power") -> None: ...
    @property
    def kind(self) -> str:
        """
        The kind of the pipeline. Can be 'power' or 'radiance'.
        In the case of 'power', the resulting matrix is multiplied by the sensitivity
        of the detector, and the units of the matrix are [m^3 sr], which gives the units
        of power [W] for the product of the ray transfer matrix and the emission profile.
        In case of 'radiance', the sensitivity is not taken into account and
        the matrix is calculated in [m], which gives the units of radiance [W m^-2 sr^-1]
        for the product of the ray transfer matrix and the emission profile.
        """
    @kind.setter
    def kind(self, value: str) -> None: ...
    @property
    def matrix(self) -> NDArray[np.float64]: ...

class RayTransferPipeline0D(Pipeline0D, RayTransferPipelineBase):
    """
    Simple 0D pipeline for ray transfer matrix (geometry matrix) calculation.

    :param str name: The name of the pipeline. Default is 'RayTransferPipeline0D'.
    :param str kind: The kind of the pipeline. Can be 'power' (default) or 'radiance'.
        In the case of 'power', the resulting matrix is multiplied by the sensitivity
        of the detector, and the units of the matrix are [m^3 sr], which gives the units
        of power [W] for the product of the ray transfer matrix and the emission profile.
        In case of 'radiance', the sensitivity is not taken into account and
        the matrix is calculated in [m], which gives the units of radiance [W m^-2 sr^-1]
        for the product of the ray transfer matrix and the emission profile.
        Note that if the sensitivity of the detector is 1 (e.g. `PinholeCamera`, `VectorCamera`),
        the 'power' and 'radiance' give the same results.

    :ivar np.ndarray matrix: Ray transfer matrix, a 1D array of size :math:`N_{bin}`.

    .. code-block:: pycon

       >>> from cherab.tools.raytransfer import RayTransferPipeline0D
       >>> pipeline = RayTransferPipeline0D(kind='radiance')
    """
    def __init__(self, name: str = "RayTransferPipeline0D", kind: str = "power") -> None: ...
    _samples: int
    _bins: int
    _matrix: NDArray[np.float64]
    def initialise(self, min_wavelength: float, max_wavelength: float, spectral_bins: int, spectral_slices: list[SpectralSlice], quiet: bool) -> None: ...
    def pixel_processor(self, slice_id: int) -> PixelProcessor: ...
    def update(  # pyrefly: ignore [bad-override-param-name]
        self, slice_id: int, packed_result: tuple[NDArray[np.float64], int], pixel_samples: int
    ) -> None: ...
    def finalise(self) -> None: ...

class RayTransferPipeline1D(Pipeline1D, RayTransferPipelineBase):
    """
    Simple 1D pipeline for ray transfer matrix (geometry matrix) calculation.

    :param str name: The name of the pipeline. Default is 'RayTransferPipeline0D'.
    :param str kind: The kind of the pipeline. Can be 'power' (default) or 'radiance'.
        In the case of 'power', the resulting matrix is multiplied by the sensitivity
        of the detector, and the units of the matrix are [m^3 sr], which gives the units
        of power [W] for the product of the ray transfer matrix and the emission profile.
        In case of 'radiance', the sensitivity is not taken into account and
        the matrix is calculated in [m], which gives the units of radiance [W m^-2 sr^-1]
        for the product of the ray transfer matrix and the emission profile.
        Note that if the sensitivity of the detector is 1 (e.g. `PinholeCamera`, `VectorCamera`),
        the 'power' and 'radiance' give the same results.

    :ivar np.ndarray matrix: Ray transfer matrix, a 2D array of shape :math:`(N_{pixel}, N_{bin})`.

    .. code-block:: pycon

       >>> from cherab.tools.raytransfer import RayTransferPipeline1D
       >>> pipeline = RayTransferPipeline1D(kind='radiance')
    """

    _pixels: int
    def __init__(self, name: str = "RayTransferPipeline1D", kind: str = "power") -> None: ...
    _samples: int
    _bins: int
    _matrix: NDArray[np.float64]
    def initialise(self, pixels: int, pixel_samples: int, min_wavelength: float, max_wavelength: float, spectral_bins: int, spectral_slices: list[SpectralSlice], quiet: bool) -> None: ...
    def pixel_processor(self, pixel: int, slice_id: int) -> PixelProcessor: ...
    def update(self, pixel: int, slice_id: int, packed_result: tuple[NDArray[np.float64], int]) -> None: ...
    def finalise(self) -> None: ...

class RayTransferPipeline2D(Pipeline2D, RayTransferPipelineBase):
    """
    Simple 2D pipeline for ray transfer matrix (geometry matrix) calculation.

    :param str name: The name of the pipeline. Default is 'RayTransferPipeline0D'.
    :param str kind: The kind of the pipeline. Can be 'power' (default) or 'radiance'.
        In the case of 'power', the resulting matrix is multiplied by the sensitivity
        of the detector, and the units of the matrix are [m^3 sr], which gives the units
        of power [W] for the product of the ray transfer matrix and the emission profile.
        In case of 'radiance', the sensitivity is not taken into account and
        the matrix is calculated in [m], which gives the units of radiance [W m^-2 sr^-1]
        for the product of the ray transfer matrix and the emission profile.
        Note that if the sensitivity of the detector is 1 (e.g. `PinholeCamera`, `VectorCamera`),
        the 'power' and 'radiance' give the same results.

    :ivar np.ndarray matrix: Ray transfer matrix, a 3D array of shape :math:`(N_x, N_y, N_{bin})`.

    .. code-block:: pycon

       >>> from cherab.tools.raytransfer import RayTransferPipeline2D
       >>> pipeline = RayTransferPipeline2D(kind='radiance')
    """

    _pixels: tuple[int, int]
    def __init__(self, name: str = "RayTransferPipeline2D", kind: str = "power") -> None: ...
    _samples: int
    _bins: int
    _matrix: NDArray[np.float64]
    def initialise(self, pixels: tuple[int, int], pixel_samples: int, min_wavelength: float, max_wavelength: float, spectral_bins: int, spectral_slices: list[SpectralSlice], quiet: bool) -> None: ...
    def pixel_processor(self, x: int, y: int, slice_id: int) -> PixelProcessor: ...
    def update(self, x: int, y: int, slice_id: int, packed_result: tuple[NDArray[np.float64], int]) -> None: ...
    def finalise(self) -> None: ...

class RayTransferPixelProcessorBase(PixelProcessor):
    """
    Base class for PixelProcessor that stores ray transfer matrix for each pixel.
    """

    _matrix: NDArray[np.float64]
    def __init__(self, bins: int) -> None: ...
    def pack_results(self) -> tuple[NDArray[np.float64], int]: ...

class RadianceRayTransferPixelProcessor(RayTransferPixelProcessorBase):
    """
    PixelProcessor that stores ray transfer matrix in the units of [m] for each pixel.
    """
    def add_sample(self, spectrum: Spectrum, sensitivity: float) -> None: ...

class PowerRayTransferPixelProcessor(RayTransferPixelProcessorBase):
    """
    PixelProcessor that stores ray transfer matrix in the units of [m^3 sr] for each pixel.
    """
    def add_sample(self, spectrum: Spectrum, sensitivity: float) -> None: ...
