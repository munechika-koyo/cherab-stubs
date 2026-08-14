from raysect.core.math import Point3D, Vector3D
from raysect.optical import Spectrum

from ...laser import LaserProfile, LaserSpectrum
from ...laser.model import LaserModel
from ...plasma import Plasma

class SeldenMatobaThomsonSpectrum(LaserModel):
    r"""Thomson Scattering based on Selden-Matoba.

    The class calculates Thomson scattering of the laser to the spectrum. The model of the scattered spectrum used is based on
    the semi-empirical model by Selden and the Thomson scattering cross-section is taken from Matoba articles. The spectral contribution
    of the scattered laser light :math:`c` is calculated as a sum of contributions of all laser wavelengths

    .. math::

         c(\lambda) =  c r_\mathrm{e}^2 n_\mathrm{e} \cos^2\theta \sum_{\lambda_\mathrm{L}} \frac{E_\mathrm{L}(\lambda_\mathrm{L}) S\left(\frac{\lambda}{\lambda_\mathrm{L}} - 1, \varphi, T_\mathrm{e}\right)}{\lambda_\mathrm{L}},


    where :math:`\lambda` is the spectrum's wavelength, :math:`r_\mathrm{e}` is the classical electron radius, :math:`n_\mathrm{e}` is the electron delsity,
    :math:`\theta` is the angle between the laser polarisation and scattering vectors, :math:`c` is the vacuum speed of light
    :math:`\lambda_\mathrm{L}` is the laser wavelength, :math:`E_\mathrm{L}` is the laser energy density, :math:`\varphi` is the scattering angle and :math:`T_\mathrm{e}` is the electron
    temperature. The scattering function :math:`S` is taken from the Matoba article. The multiplication by the speed of light is added to transfer the Thomson scattering
    cross section into a reaction rate.

    .. seealso::
         The Prunty article provides a thorough introduction into the physics of Thomson scattering. The articles by Selden and Matoba were used to build
         this model.

         :Selden: `Selden, A.C., 1980. Simple analytic form of the relativistic Thomson scattering spectrum. Physics Letters A, 79(5-6), pp.405-406.`
         :Matoba: `Matoba, T., et al., 1979. Analytical approximations in the theory of relativistic Thomson scattering for high temperature fusion plasma.
                  Japanese Journal of Applied Physics, 18(6), p.1127.`
         :Prunty: `Prunty, S.L., 2014. A primer on the theory of Thomson scattering for high-temperature fusion plasmas. Physica Scripta, 89(12), p.128001.`

    """

    def __init__(
        self,
        laser_profile: LaserProfile | None = None,
        laser_spectrum: LaserSpectrum | None = None,
        plasma: Plasma | None = None,
    ) -> None: ...
    def emission(
        self,
        point_plasma: Point3D,
        observation_plasma: Vector3D,
        point_laser: Point3D,
        observation_laser: Vector3D,
        spectrum: Spectrum,
    ) -> Spectrum: ...
    def calculate_spectrum(
        self,
        ne: float,
        te: float,
        laser_energy_density: float,
        laser_wavelength: float,
        observation_angle: float,
        angle_polarization: float,
        spectrum: Spectrum,
    ) -> Spectrum:
        """
        Calculates scattered spectrum for the given parameters.

        The method returns the Thomson scattered spectrum given the plasma parameters, without the need of specifying
        plasma or laser.

        :param float ne: Plasma electron density in m**-3
        :param float te: Plasma electron temperature in eV
        :param float laser_energy_density: Energy density of the laser light in J * m**-3
        :param float laser_wavelength: The laser light wavelength in nm
        :param float observation_angle: The angle of observation is the angle between the observation direction and the direction
                                        of the Poynting vector.
        :param float angle_polarization: The angle between the observation direction and the polarisation direction of the laser light.

        :return: Spectrum
        """
