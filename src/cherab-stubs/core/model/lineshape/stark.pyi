from typing import ClassVar, Literal

from numpy import float64, ufunc
from raysect.core.math import Point3D, Vector3D
from raysect.core.math.function.float.function1d.base import Function1D
from raysect.optical import Spectrum

from ...atomic import AtomicData, Line
from ...atomic.elements import Element, Isotope
from ...math.integrators import Integrator1D
from ...plasma import Plasma
from ...species import Species
from .zeeman import ZeemanLineShapeModel

deuterium: Isotope
hydrogen: Element
hyp2f1: ufunc
tritium: Isotope

class StarkFunction(Function1D):
    """
    Normalised Stark function for the StarkBroadenedLine line shape.

    :param float wavelength: central wavelength of the line in nm.
    :param float lambda_1_2: FWHM of the function in nm.
    """

    STARK_NORM_COEFFICIENT: ClassVar[float64] = ...
    def __init__(self, wavelength: float, lambda_1_2: float) -> None: ...

def add_lorentzian_line(radiance: float, wavelength: float, lambda_1_2: float, spectrum: Spectrum, integrator: Integrator1D) -> Spectrum:
    r"""
    Adds a modified Lorentzian line to the given spectrum and returns the new spectrum.

    The modified Lorentzian:
    :math:`L(\lambda-\lambda_0, \Delta\lambda_{1/2}^{(L)})=\frac{C_0\left(\Delta\lambda_{1/2}^{(L)}\right)^{3/2}}{(\lambda-\lambda_0)^{5/2}+\left(\frac{\Delta\lambda_{1/2}^{(L)}}{2}\right)^{5/2}},`

    :math:`C_0=\frac{(1/2)^{3/2}}{4R{_2}F_1(\frac{2}{5},1,\frac{7}{5},-R^{5/2})},`

    where :math:`\Delta\lambda_{1/2}^{(L)}` is the line FWHM, :math:`{_2}F_1` is the hypergeometric function and :math:`R=50`.
    The line shape is truncated at :math:`\lambda<R\Delta\lambda_{1/2}^{(L)}` and :math:`\lambda>R\Delta\lambda_{1/2}^{(L)}`.

    See B. Lomanowski, et al. "Inferring divertor plasma properties from hydrogen Balmer
    and Paschen series spectroscopy in JET-ILW." Nuclear Fusion 55.12 (2015)
    `123028 <https://doi.org/10.1088/0029-5515/55/12/123028>`_ for details.

    :param float radiance: Intensity of the line in radiance.
    :param float wavelength: central wavelength of the line in nm.
    :param float lambda_1_2: FWHM of the line shape in nm.
    :param Spectrum spectrum: the current spectrum to which the Lorentzian line is added.
    :param Integrator1D integrator: Integrator1D instance to integrate the line shape
                                    over the spectral bin.
    :return: the updated Spectrum instance.
    """

class StarkBroadenedLine(ZeemanLineShapeModel):
    r"""
    Parametrised Stark-Doppler-Zeeman line shape for Balmer and Paschen series based on
    B. Lomanowski, et al. "Inferring divertor plasma properties from hydrogen Balmer
    and Paschen series spectroscopy in JET-ILW." Nuclear Fusion 55.12 (2015)
    `123028 <https://doi.org/10.1088/0029-5515/55/12/123028>`_.

    The following approximations are used:

      * The Zeeman and Stark effects are considered independently.
      * Zeeman splitting is taken in the form of a simple triplet with a :math:`\pi`-component
        centred at :math:`\lambda`, :math:`\sigma^{+}`-component at :math:`\frac{hc}{hc/\lambda -\mu B}`
        and :math:`\sigma^{-}`-component at :math:`\frac{hc}{hc/\lambda +\mu B}`.
      * The model of Stark broadening is obtained by fitting the Model Microfield Method (MMM).
      * The convolution of Stark-Zeeman and Doppler profiles is replaced with the weighted sum
        to speed-up calculations (so-called pseudo-Voigt profile).

    The Stark-broadened line shape is modelled as modified Lorentzian:
    :math:`L(\lambda-\lambda_0, \Delta\lambda_{1/2}^{(L)})=\frac{C_0(\Delta\lambda_{1/2}^{(L)})^{3/2}}{(\lambda-\lambda_0)^{5/2}+(\frac{\Delta\lambda_{1/2}^{(L)}}{2})^{5/2}},`

    :math:`C_0=\frac{(1/2)^{3/2}}{4R{_2}F_1(\frac{2}{5},1,\frac{7}{5},-R^{5/2})},`

    where :math:`\Delta\lambda_{1/2}^{(L)}=c_{ij}\frac{n_e^{a_{ij}}}{T_e^{b_{ij}}}` is the line FWHM,
    :math:`{_2}F_1` is the hypergeometric function and :math:`R=50`.
    The line shape is truncated at :math:`\lambda<R\Delta\lambda_{1/2}^{(L)}` and :math:`\lambda>R\Delta\lambda_{1/2}^{(L)}`.
    The :math:`a_{ij}`, :math:`b_{ij}` and :math:`c_{ij}` are the fitting coefficients.

    Each Zeeman component is modelled as a weighted sum of Stark (Lorentzian), :math:`L(\lambda-\lambda_0, \Delta\lambda_{1/2}^{(L)})`,
    and Doppler (Gauss), :math:`G(\lambda'-\lambda_0, \Delta\lambda_{1/2}^{(G)})` profiles:

      :math:`\eta L(\lambda-\lambda_0, \Delta\lambda_{1/2}^{(V)}) + (1-\eta)G(\lambda-\lambda_0, \Delta\lambda_{1/2}^{(V)})`,

      with :math:`\Delta\lambda_{1/2}^{(V)}\equiv \Delta\lambda_{1/2}^{(V)}(\Delta\lambda_{1/2}^{(G)}, \Delta\lambda_{1/2}^{(L)})`
      and :math:`\eta\equiv \eta(\Delta\lambda_{1/2}^{(G)}, \Delta\lambda_{1/2}^{(L)})`.

    Both :math:`\Delta\lambda_{1/2}^{(V)}` and :math:`\eta` are obtained by fitting the convolution:

      :math:`\int_{-\infty}^{\infty}G(\lambda'-\lambda_0, \Delta\lambda_{1/2}^{(G)})L(\lambda-\lambda'-\lambda_0, \Delta\lambda_{1/2}^{(L)})d\lambda'`.

    The :math:`\Delta\lambda_{1/2}^{(V)}` function is fitted as:
    :math:`\Delta\lambda_{1/2}^{(V)}=\sum_{n=0}^{6}a_n(\frac{\Delta\lambda_{1/2}^{(L)}}{\Delta\lambda_{1/2}^{(G)}})^n`
    for :math:`\frac{\Delta\lambda_{1/2}^{(L)}}{\Delta\lambda_{1/2}^{(G)}} \le 1` and
    :math:`\Delta\lambda_{1/2}^{(V)}=\sum_{n=0}^{6}b_n(\frac{\Delta\lambda_{1/2}^{(G)}}{\Delta\lambda_{1/2}^{(L)}})^n`
    for :math:`\frac{\Delta\lambda_{1/2}^{(L)}}{\Delta\lambda_{1/2}^{(G)}} > 1` with

    `a` = [1., 0.15882, 1.04388, -1.38281, 0.46251, 0.82325, -0.58026] and

    `b` = [1., 0, 0.57575, 0.37902, -0.42519, -0.31525, 0.31718].

    While the :math:`\eta` function is fitted as:
    :math:`\eta=exp(\sum_{n=0}^{5}c_n(ln(\frac{\Delta\lambda_{1/2}^{(L)}}{\Delta\lambda_{1/2}^{(V)}}))^n`
    for :math:`0.01<\frac{\Delta\lambda_{1/2}^{(L)}}{\Delta\lambda_{1/2}^{(V)}}<0.999` with

    `c` = [5.14820e-04, 1.38821e+00, -9.60424e-02, -3.83995e-02, -7.40042e-03, -5.47626e-04].

    :param Line line: The emission line object for this line shape.
    :param float wavelength: The rest wavelength for this emission line.
    :param Species target_species: The target plasma species that is emitting.
    :param Plasma plasma: The emitting plasma object.
    :param AtomicData atomic_data: The atomic data provider.
    :param tuple stark_model_coefficients: Stark model coefficients in the form (c_ij, a_ij, b_ij).
                                           Default is None (will use
                                           `atomic_data.stark_model_coefficients`).
    :param Integrator1D integrator: Integrator1D instance to integrate the line shape
        over the spectral bin. Default is `GaussianQuadrature()`.
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
        stark_model_coefficients: tuple[float, ...] | None = None,
        integrator: Integrator1D = ...,
        polarisation: Literal["pi", "sigma", "no"] = "no",
    ) -> None: ...
    def add_line(self, radiance: float, point: Point3D, direction: Vector3D, spectrum: Spectrum) -> Spectrum: ...
