from typing import Literal

from raysect.core.math import Point3D, Vector3D
from raysect.optical import Spectrum

from ...atomic import AtomicData, Line, ZeemanStructure
from ...atomic.elements import Element, Isotope
from ...math.integrators import Integrator1D
from ...plasma import Plasma
from ...species import Species
from .base import LineShapeModel

_Polarisation = Literal["pi", "sigma", "no"]

beryllium: Element
boron: Element
carbon: Element
deuterium: Isotope
helium: Element
helium3: Isotope
hydrogen: Element
neon: Element
nitrogen: Element
oxygen: Element
tritium: Isotope

class ZeemanLineShapeModel(LineShapeModel):
    r"""
    A base class for building Zeeman line shapes.

    :param Line line: The emission line object for this line shape.
    :param float wavelength: The rest wavelength for this emission line.
    :param Species target_species: The target plasma species that is emitting.
    :param Plasma plasma: The emitting plasma object.
    :param AtomicData atomic_data: The atomic data provider.
    :param str polarisation: Leaves only :math:`\pi`-/:math:`\sigma`-polarised components:
                             "pi" - leave only :math:`\pi`-polarised components,
                             "sigma" - leave only :math:`\sigma`-polarised components,
                             "no" - leave all components (default).
    :param Integrator1D integrator: Integrator1D instance to integrate the line shape
                                    over the spectral bin. Default is None.
    """
    def __init__(
        self,
        line: Line,
        wavelength: float,
        target_species: Species,
        plasma: Plasma,
        atomic_data: AtomicData,
        polarisation: _Polarisation = "no",
        integrator: Integrator1D | None = None,
    ) -> None: ...
    @property
    def polarisation(self) -> _Polarisation: ...
    @polarisation.setter
    def polarisation(self, value: _Polarisation) -> None: ...

class ZeemanTriplet(ZeemanLineShapeModel):
    r"""
    Simple Doppler-Zeeman triplet (Paschen-Back effect).

    :param Line line: The emission line object for this line shape.
    :param float wavelength: The rest wavelength for this emission line.
    :param Species target_species: The target plasma species that is emitting.
    :param Plasma plasma: The emitting plasma object.
    :param AtomicData atomic_data: The atomic data provider.
    :param str polarisation: Leaves only :math:`\pi`-/:math:`\sigma`-polarised components:
                             "pi" - leave central component,
                             "sigma" - leave side components,
                             "no" - all components (default).
    """

    def __init__(
        self,
        line: Line,
        wavelength: float,
        target_species: Species,
        plasma: Plasma,
        atomic_data: AtomicData,
        polarisation: _Polarisation = "no",
    ) -> None: ...
    def add_line(self, radiance: float, point: Point3D, direction: Vector3D, spectrum: Spectrum) -> Spectrum: ...

class ParametrisedZeemanTriplet(ZeemanLineShapeModel):
    r"""Parametrised Doppler-Zeeman triplet.

    It takes into account additional broadening due to
    the line's fine structure without resolving the individual components of the fine
    structure. The model is described with three parameters: :math:`\alpha`,
    :math:`\beta` and :math:`\gamma`.

    The distance between :math:`\sigma^+` and :math:`\sigma^-` peaks:
    :math:`\Delta \lambda_{\sigma} = \alpha B`,
    where `B` is the magnetic field strength.
    The ratio between Zeeman and thermal broadening line widths:
    :math:`\frac{W_\mathrm{Zeeman}}{W_\mathrm{Doppler}} = \beta T^{\gamma}`,
    where `T` is the species temperature in eV.

    For details see A. Blom and C. Jupén, Parametrisation of the Zeeman effect
    for hydrogen-like spectra in high-temperature plasmas,
    Plasma Phys. Control. Fusion 44 (2002) `1229-1241
    <https://doi.org/10.1088/0741-3335/44/7/312>`_.

    :param Line line: The emission line object for this line shape.
    :param float wavelength: The rest wavelength for this emission line.
    :param Species target_species: The target plasma species that is emitting.
    :param Plasma plasma: The emitting plasma object.
    :param AtomicData atomic_data: The atomic data provider.
    :param tuple line_parameters: Parameters of the model in the form (alpha, beta, gamma).
                                  Default is None (will use `atomic_data.zeeman_triplet_parameters`).
    :param str polarisation: Leaves only :math:`\pi`-/:math:`\sigma`-polarised components:
                             "pi" - leave central component,
                             "sigma" - leave side components,
                             "no" - all components (default).
    """

    def __init__(
        self,
        line: Line,
        wavelength: float,
        target_species: Species,
        plasma: Plasma,
        atomic_data: AtomicData,
        line_parameters: tuple[float, ...] | None = None,
        polarisation: _Polarisation = "no",
    ) -> None: ...
    def add_line(self, radiance: float, point: Point3D, direction: Vector3D, spectrum: Spectrum) -> Spectrum: ...

class ZeemanMultiplet(ZeemanLineShapeModel):
    r"""
    Doppler-Zeeman Multiplet.

    The lineshape radiance is calculated from a base PEC rate that is unresolved. This
    radiance is then divided over a number of components as specified in the ``zeeman_structure``
    argument. The ``zeeman_structure`` specifies wavelengths and ratios of
    :math:`\pi`-/:math:`\sigma`-polarised components as functions of the magnetic field strength.
    These functions can be obtained using the output of the ADAS603 routines.

    :param Line line: The emission line object for the base rate radiance calculation.
    :param float wavelength: The rest wavelength of the base emission line.
    :param Species target_species: The target plasma species that is emitting.
    :param Plasma plasma: The emitting plasma object.
    :param AtomicData atomic_data: The atomic data provider.
    :param zeeman_structure: A ``ZeemanStructure`` object that provides wavelengths and ratios
                             of :math:`\pi`-/:math:`\sigma^{+}`-/:math:`\sigma^{-}`-polarised
                             components for any given magnetic field strength.
                             Default is None (will use atomic_data.zeeman_structure).
    :param str polarisation: Leaves only :math:`\pi`-/:math:`\sigma`-polarised components:
                             "pi" - leave only :math:`\pi`-polarised components,
                             "sigma" - leave only :math:`\sigma`-polarised components,
                             "no" - leave all components (default).
    """

    def __init__(
        self,
        line: Line,
        wavelength: float,
        target_species: Species,
        plasma: Plasma,
        atomic_data: AtomicData,
        zeeman_structure: ZeemanStructure | None = None,
        polarisation: _Polarisation = "no",
    ) -> None: ...
    def add_line(self, radiance: float, point: Point3D, direction: Vector3D, spectrum: Spectrum) -> Spectrum: ...
