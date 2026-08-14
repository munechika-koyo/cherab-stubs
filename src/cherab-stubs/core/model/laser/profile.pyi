from raysect.core.math import Vector3D
from raysect.primitive import Cylinder

from ...laser.profile import LaserProfile

class UniformEnergyDensity(LaserProfile):
    """
    LaserProfile with a constant volumetric energy density.

    Returns a laser with a cylindrical shape within which the laser volumentric energy density is constant.
    The laser starts at z=0 and extends in the positive z direction.

    .. note:
        The methods get_pointing, get_polarization and get_energy_density are not limited to the inside
        of the laser cylinder.  If called alone for position (x, y, z) outside the laser cylinder,
        they will still return non-zero values.

    In the following example, a laser of length of 2 m (extending from z=0 to z=2 m) with a radius of 3 cm
    and volumetric energy density of 5 J*m^-3 and polarisation in the y direction is created:

    .. code-block:: pycon

       >>> from raysect.core import Vector3D
       >>> from cherab.core.model.laser import UniformEnergyDensity

       >>> energy = 5 # energy density in J
       >>> radius = 3e-2 # laser radius in m
       >>> length = 2 # laser length in m
       >>> polarisation = Vector3D(0, 1, 0) # polarisation direction

           # create the laser profile
       >>> laser_profile = UniformEnergyDensity(energy, radius, length, polarisation)

    :param float energy_density: The volumetric energy density of the laser light.
    :param float laser_length: The length of the laser cylinder.
    :param float laser_radius: The radius of the laser cylinder.
    :param Vector3D polarization: The direction of the laser polarization:

    :ivar float energy_density: The volumetric energy density of the laser light.
    :ivar float laser_radius: The radius of the laser cylinder.
    :ivar float laser_length: The length of the laser cylinder.
    """
    def __init__(
        self,
        energy_density: float = 1,
        laser_length: float = 1,
        laser_radius: float = 0.05,
        polarization: Vector3D = ...,
    ) -> None: ...
    def set_polarization(self, value: Vector3D) -> None: ...
    @property
    def laser_length(self) -> float: ...
    @laser_length.setter
    def laser_length(self, value: float) -> None: ...
    @property
    def laser_radius(self) -> float: ...
    @laser_radius.setter
    def laser_radius(self, value: float) -> None: ...
    @property
    def energy_density(self) -> float: ...
    @energy_density.setter
    def energy_density(self, value: float) -> None: ...
    def generate_geometry(self) -> list[Cylinder]: ...

class ConstantAxisymmetricGaussian(LaserProfile):
    def __init__(self) -> None: ...

class ConstantBivariateGaussian(LaserProfile):
    """
    LaserProfile with a Gaussian-shaped volumetric energy density distribution in the xy plane
    and constant pulse intensity.

    Returns a laser with a cylindrical shape and the propagation of the laser light in the positive z direction.

    The model imitates a laser beam with a uniform power output within a single pulse. This results
    in the distribution of the energy density along the propagation direction of the laser (z-axis) to be also
    uniform. The integral value of laser energy Exy in an x-y plane is given by

    .. math::
         E_{xy} = \\frac{E_p}{(c * \\tau)},

    where Ep is the energy of the laser pulse, tau is the temporal pulse length and c is the speed of light in vacuum.
    In an x-y plane, the volumetric energy density follows a bivariate Gaussian with a zero correlation:

    .. math::
         E(x, y) = \\frac{E_{xy}}{2 \\pi \\sigma_x \\sigma_y} exp\\left(-\\frac{x^2 + y^2}{2 \\sigma_x \\sigma_y}\\right).

    The sigma_x and sigma_y are standard deviations in x and y directions, respectively.

    .. note::
        The height of the cylinder, forming the laser beam, is given by the laser_length and is independent from the
        temporal length of the laser pulse given by pulse_length. This gives the possibility to independently control
        the size of the laser primitive and the value of the volumetric energy density.

        The methods get_pointing, get_polarization and get_energy_density are not limited to the inside
        of the laser cylinder.  If called for position (x, y, z) outside the laser cylinder, they can still
        return non-zero values.


    The following example shows how to create a laser with sigma_x= 1 cm and sigma_y=2 cm, which makes the laser
    profile in x-y plane to be elliptical. The pulse energy is 5 J and the laser temporal pulse length is 10 ns:

    .. code-block:: pycon

       >>> from raysect.core import Vector3D
       >>> from cherab.core.model.laser import ConstantBivariateGaussian

       >>> radius = 3e-2 # laser radius in m
       >>> length = 2 # laser length in m
       >>> polarisation = Vector3D(0, 1, 0) # polarisation direction
       >>> pulse_energy = 5 # energy in a laser pulse in J
       >>> pulse_length = 1e-8 # pulse length in s
       >>> width_x = 1e-2 # standard deviation in x direction in m
       >>> width_y = 2e-2 # standard deviation in y direction in m

           # create the laser profile
       >>> laser_profile = ConstantBivariateGaussian(pulse_energy, pulse_length, radius, length, width_x, width_y, polarisation)

    :param float pulse_energy: The energy of the laser in Joules delivered in a single laser pulse.
    :param float pulse_length: The temporal length of the laser pulse in seconds.
    :param float laser_length: The length of the laser cylinder.
    :param float laser_radius: The radius of the laser cylinder.
    :param float stddev_x: The standard deviation of the bivariate Gaussian distribution of the volumetric energy
      density distribution of the laser light in the x axis in meters.
    :param float stddev_y: The standard deviation of the bivariate Gaussian distribution of the volumetric energy
      density distribution of the laser light in the y axis in meters.
    :param Vector3D polarization: The direction of the laser polarization:

    :ivar float pulse_energy: The energy of the laser in Joules delivered in a single laser pulse.
    :ivar float pulse_length: The temporal length of the laser pulse in seconds.
    :ivar float laser_radius: The radius of the laser cylinder.
    :ivar float laser_length: The length of the laser cylinder.
    :ivar float stddev_x: The standard deviation of the bivariate Gaussian distribution of the volumetric energy
      density distribution of the laser light in the x axis in meters.
    :ivar float stddev_y: The standard deviation of the bivariate Gaussian distribution of the volumetric energy
      density distribution of the laser light in the y axis in meters.
    """
    def __init__(
        self,
        pulse_energy: float = 1,
        pulse_length: float = 1,
        laser_radius: float = 0.05,
        laser_length: float = 1,
        stddev_x: float = 0.01,
        stddev_y: float = 0.01,
        polarization: Vector3D = ...,
    ) -> None: ...
    def set_polarization(self, value: Vector3D) -> None: ...
    @property
    def laser_length(self) -> float: ...
    @laser_length.setter
    def laser_length(self, value: float) -> None: ...
    @property
    def laser_radius(self) -> float: ...
    @laser_radius.setter
    def laser_radius(self, value: float) -> None: ...
    @property
    def pulse_energy(self) -> float: ...
    @pulse_energy.setter
    def pulse_energy(self, value: float) -> None: ...
    @property
    def pulse_length(self) -> float: ...
    @pulse_length.setter
    def pulse_length(self, value: float) -> None: ...
    @property
    def stddev_x(self) -> float: ...
    @stddev_x.setter
    def stddev_x(self, value: float) -> None: ...
    @property
    def stddev_y(self) -> float: ...
    @stddev_y.setter
    def stddev_y(self, value: float) -> None: ...
    def _function_changed(self) -> None:
        """
        Energy density should be returned in units [J/m ** 3]. Energy shape in xy
        plane is defined by normal distribution (integral over xy plane for
        constant z is 1). The units of such distribution are [m ** -2].
        In the z axis direction (direction of laser propagation),
        the laser_energy is spread along the z axis using the velocity
        of light SPEED_OF_LIGHT and the temporal duration of the pulse:
        length = SPEED_OF_LIGHT * pulse_length. Combining the normal distribution with the normalisation
         pulse_energy / length gives the units [J / m ** 3].
        """
    def generate_geometry(self) -> list[Cylinder]: ...

class TrivariateGaussian(LaserProfile):
    """
    LaserProfile with a trivariate Gaussian-shaped volumetric energy density.

    Returns a laser with a cylindrical shape and the propagation of the laser light in the positive z direction.
    This model imitates a laser beam with a Gaussian distribution of power output within a single pulse frozen in time:

    .. math::
         E(x, y, z) = \\frac{E_p}{\\sqrt{2 \\pi^3} \\sigma_x \\sigma_y \\sigma_z} exp\\left(-\\frac{x^2}{2 \\sigma_x^2} -\\frac{y^2}{2 \\sigma_y^2} -\\frac{(z - \\mu_z)^2}{2 \\sigma_z^2}\\right).


    The sigma_x and sigma_y are standard deviations in x and y directions, respectively, and E_p is the energy delivered by laser in a
    single laser pulse. The mu_z is the mean of the distribution in the z direction and controls th position of the laser pulse along the z direction.
    The standard deviation in z direction sigma_z is calculated from the pulse length tau_p, which is the
    standard deviation of the Gaussian distributed output power of the laser within a single pulse:

    .. math::
         \\sigma_z = \\tau_p c.

    The c stands for the speed of light in vacuum.

    .. note::
        The height of the cylinder, forming the laser beam, is given by the laser_length and is independent from the
        temporal length of the laser pulse given by pulse_length. This gives the possibility to independently control
        the size of the laser primitive and the value of the volumetric energy density.

        The methods get_pointing, get_polarization and get_energy_density are not limited to the inside
        of the laser cylinder.  If called alone for position (x, y, z) outside the laser cylinder, they can still
        return non-zero values.


    The following example shows how to create a laser with sigma_x = 1 cm and sigma_y = 2 cm, which makes the laser
    profile in an x-y plane to be elliptical. The pulse energy is 5 J and the laser temporal pulse length is 10 ns.
    The position of the laser pulse maximum mean_z is set to 0.5:

    .. code-block:: pycon

       >>> from raysect.core import Vector3D
       >>> from cherab.core.model.laser import ConstantBivariateGaussian

       >>> radius = 3e-2 # laser radius in m
       >>> length = 2 # laser length in m
       >>> polarisation = Vector3D(0, 1, 0) # polarisation direction
       >>> pulse_energy = 5 # energy in a laser pulse in J
       >>> pulse_length = 1e-8 # pulse length in s
       >>> pulse_z = 0.5 # position of the pulse mean
       >>> width_x = 1e-2 # standard deviation in x direction in m
       >>> width_y = 2e-2 # standard deviation in y direction in m

           # create the laser profile
       >>> laser_profile = ConstantBivariateGaussian(pulse_energy, pulse_length, pulse_z, radius, length, width_x, width_y, polarisation)


    :param float pulse_energy: The energy of the laser in Joules delivered in a single laser pulse.
    :param float pulse_length: The standard deviation of the laser pulse length in the temporal domain.
    :param float mean_z: Position of the mean value of the laser pulse in the z direction. Can be used to control the
      position of the laser pulse along the laser propagation.
    :param float laser_length: The length of the laser cylinder.
    :param float laser_radius: The radius of the laser cylinder.
    :param float stddev_x: The standard deviation of the bivariate Gaussian distribution of the volumetric energy
      density distribution of the laser light in the x axis in meters.
    :param float stddev_y: The standard deviation of the bivariate Gaussian distribution of the volumetric energy
      density distribution of the laser light in the y axis in meters.
    :param Vector3D polarization: The direction of the laser polarization.

    :ivar float pulse_energy: The energy of the laser in Joules delivered in a single laser pulse.
    :ivar float pulse_length: The standard deviation of the laser pulse length in the temporal domain.
    :ivar float mean_z: Position of the mean value of the laser pulse in the z direction.
     Can be used to control the position of the laser pulse along the laser propagation.
    :ivar float laser_radius: The radius of the laser cylinder.
    :ivar float laser_length: The length of the laser cylinder.
    :ivar float stddev_x: The standard deviation of the bivariate Gaussian distribution of the volumetric energy
      density distribution of the laser light in the x axis in meters.
    :ivar float stddev_y: The standard deviation of the bivariate Gaussian distribution of the volumetric energy
      density distribution of the laser light in the y axis in meters.
    """
    def __init__(
        self,
        pulse_energy: float = 1,
        pulse_length: float = 1,
        mean_z: float = 0,
        laser_length: float = 1,
        laser_radius: float = 0.05,
        stddev_x: float = 0.01,
        stddev_y: float = 0.01,
        polarization: Vector3D = ...,
    ) -> None: ...
    def set_polarization(self, value: Vector3D) -> None: ...
    @property
    def laser_length(self) -> float: ...
    @laser_length.setter
    def laser_length(self, value: float) -> None: ...
    @property
    def laser_radius(self) -> float: ...
    @laser_radius.setter
    def laser_radius(self, value: float) -> None: ...
    @property
    def pulse_energy(self) -> float: ...
    @pulse_energy.setter
    def pulse_energy(self, value: float) -> None: ...
    @property
    def pulse_length(self) -> float: ...
    @pulse_length.setter
    def pulse_length(self, value: float) -> None: ...
    @property
    def stddev_x(self) -> float: ...
    @stddev_x.setter
    def stddev_x(self, value: float) -> None: ...
    @property
    def stddev_y(self) -> float: ...
    @stddev_y.setter
    def stddev_y(self, value: float) -> None: ...
    @property
    def mean_z(self) -> float: ...
    @mean_z.setter
    def mean_z(self, value: float) -> None: ...
    def _function_changed(self) -> None:
        """
        Energy density should be returned in units [J/m ** 3]. The integral value of the _distribution
        is 1, thus multiplying _distribution by _pulse_energy gives correct values.
        """
    def generate_geometry(self) -> list[Cylinder]: ...

class GaussianBeamAxisymmetric(LaserProfile):
    """
    LaserProfile with volumetric energy density following the Gaussian beam model.

    Returns a laser with a cylindrical shape and the propagation of the laser light in the positive z direction. This model implements
    the axisymmetrical Gaussian beam model. It imitates a focused axis symmetrical laser beam with a uniform power output in a laser pulse.
    The volumetric energy density is given by

    .. math::
         E(x, y, z) = \\frac{E_{xy}}{2 \\pi \\sigma^2(z)} exp\\left( -\\frac{x^2 + y^2}{2 \\sigma^2(z) }\\right) \\\\\n
    where the sigma is the standard deviation of the Gaussian shape in the xy plane and is given by

    .. math::
         sigma(z) = \\sigma_0 \\sqrt{1 + \\left(\\frac{z - z_0}{z_R}\\right)^2}.

    The z_0 is the position of the beam focus and z_R is the Rayleigh length

    .. math::
         z_R = \\frac{\\pi \\omega_0^2 n}{\\lambda_l}

    where the omega_0 is the standard deviation in the xy plane in the focal point (beam waist) and lambda_l is the central wavelength of
    the laser. The E_xy stand for the laser energy in an xy plane and is calculated as:

    .. math::
         E_{xy} = \\frac{E_p}{(c * \\tau)},

    where the E_p is the energy in a single laser pulse and tau is the temporal pulse length.

    .. note::
        For more information about the Gaussian beam model see https://en.wikipedia.org/wiki/Gaussian_beam

        The methods get_pointing, get_polarization and get_energy_density are not limited to the inside
        of the laser cylinder.  If called alone for position (x, y, z) outside the laser cylinder, they can still
        return non-zero values.

    The following example shows how to create a laser with pulse energy 5J, pulse length 10 ns and with the laser cylinder primitive
    being 2m long with 5 cm in diameter. The the standard deviation of the beam in the focal point (waist) is 5mm and the position of the
    waist is z=50 cm. The laser wavelength is 1060 nm.

    .. code-block:: pycon

       >>> from raysect.core import Vector3D
       >>> from cherab.core.model.laser import GaussianBeamAxisymmetric

       >>> radius = 5e-2 # laser radius in m
       >>> length = 2 # laser length in m
       >>> polarisation = Vector3D(0, 1, 0) # polarisation direction
       >>> pulse_energy = 5 # energy in a laser pulse in J
       >>> pulse_length = 1e-8 # pulse length in s
       >>> waist_width = 5e-3 # standard deviation in the waist
       >>> waist_z = 0.5 # position of the pulse mean
       >>> width_x = 1e-2 # standard deviation in x direction in m
       >>> width_y = 2e-2 # standard deviation in y direction in m
       >>> laser_wlen = 1060 # laser wavelength in nm

           # create the laser profile
       >>> laser_profile = GaussianBeamAxisymmetric(pulse_energy, pulse_length, length, radius, waist_z, waist_width, laser_wlen)

    :param float pulse_energy: The energy of the laser in Joules delivered in a single laser pulse.
    :param float pulse_length: The temporal length of the laser pulse in seconds.
    :param float laser_length: The length of the laser cylinder in meters.
    :param float laser_radius: The radius of the laser cylinder in meters.
    :param float waist_z: Position of the laser waist along the z axis in m.
    :param float stddev_waist: The standard deviation of the laser width in the focal point (waist) in m.
    :param float laser_wavelength: The central wavelength of the laser light in nanometers.
    :param Vector3D polarization: The direction of the laser polarization.

    :ivar float pulse_energy: The energy of the laser in Joules delivered in a single laser pulse.
    :ivar float pulse_length: The temporal length of the laser pulse in seconds.
    :ivar float laser_length: The length of the laser cylinder in meters.
    :ivar float laser_radius: The radius of the laser cylinder in meters.
    :ivar float waist_z: Position of the laser waist along the z axis in m.
    :ivar float stddev_waist: The standard deviation of the laser width in the focal point (waist) in m.
    :ivar float laser_wavelength: The central wavelength of the laser light in nanometers.
    :ivar Vector3D polarization: The direction of the laser polarization.
    """
    def __init__(
        self,
        pulse_energy: float = 1,
        pulse_length: float = 1,
        laser_length: float = 1,
        laser_radius: float = 0.05,
        waist_z: float = 0,
        stddev_waist: float = 0.01,
        laser_wavelength: float = 1000,
        polarization: Vector3D = ...,
    ) -> None: ...
    def set_polarization(self, value: Vector3D) -> None: ...
    @property
    def laser_length(self) -> float: ...
    @laser_length.setter
    def laser_length(self, value: float) -> None: ...
    @property
    def laser_radius(self) -> float: ...
    @laser_radius.setter
    def laser_radius(self, value: float) -> None: ...
    @property
    def pulse_energy(self) -> float: ...
    @pulse_energy.setter
    def pulse_energy(self, value: float) -> None: ...
    @property
    def pulse_length(self) -> float: ...
    @pulse_length.setter
    def pulse_length(self, value: float) -> None: ...
    @property
    def waist_z(self) -> float: ...
    @waist_z.setter
    def waist_z(self, value: float) -> None: ...
    @property
    def stddev_waist(self) -> float: ...
    @stddev_waist.setter
    def stddev_waist(self, value: float) -> None: ...
    @property
    def laser_wavelength(self) -> float: ...
    @laser_wavelength.setter
    def laser_wavelength(self, value: float) -> None: ...
    def _function_changed(self) -> None:
        """
        Energy density should be returned in units [J/m ** 3]. Energy shape in xy
        plane is defined by normal distribution (integral over xy plane for
        constant z is 1). The units of such distribution are [m ** -2].
        In the z axis direction (direction of laser propagation),
        the laser_energy is spread along the z axis using the velocity
        of light SPEED_OF_LIGHT and the temporal duration of the pulse:
        length = SPEED_OF_LIGHT * pulse_length. Combining the normal distribution with the normalisation
         pulse_energy / length gives the units [J / m ** 3].
        """
    def generate_geometry(self) -> list[Cylinder]: ...

def generate_segmented_cylinder(radius: float, length: float) -> list[Cylinder]: ...
