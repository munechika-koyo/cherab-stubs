from raysect.core.math.function.float.function3d.base import Function3D

class ConstantAxisymmetricGaussian3D(Function3D):
    r"""
    A function with a 2D Gaussian in the x-y plane and equal standard deviations in x and y directions.

    .. math::

        F(x, y, z) = \frac{1}{2 * \pi \sigma^2} \exp\left(-\frac{x^2 + y^2}{2 * \sigma^2}\right)

    The function value has a Gaussian shape in the x-y plane with the standard deviations in
    x and y direction being equal. The integral over an x-y plane is equal to 1
    and the mean values in x and y directions are equal to 0.

    :param float stddev: The standard deviation in both the x and y directions.
    """
    def __init__(self, stddev: float) -> None: ...
    @property
    def stddev(self) -> float: ...
    @stddev.setter
    def stddev(self, value: float) -> None: ...

class ConstantBivariateGaussian3D(Function3D):
    r"""
    A function with a 2D Gaussian in the x-y plane.

    .. math::

        F(x, y, z) = \frac{1}{2 * \pi \sigma_x \sigma_y} \exp\left(-\frac{x^2 + y^2}{2 * \sigma_x \sigma_y}\right)

    The function value has a Gaussian shape in the x-y plane. The integral over an x-y plane is equal to 1
    and the mean values in x and y directions are equal to 0.
    The correlation between the standard deviations in x and y directions is equal to 0.

    :param float stddev_x: The standard deviation in the x directions.
    :param float stddev_y: The standard deviation in the y directions.
    """
    def __init__(self, stddev_x: float, stddev_y: float) -> None: ...
    def _init_params(self) -> None: ...
    @property
    def stddev_x(self) -> float: ...
    @stddev_x.setter
    def stddev_x(self, value: float) -> None: ...
    @property
    def stddev_y(self) -> float: ...
    @stddev_y.setter
    def stddev_y(self, value: float) -> None: ...
    def _cache_constants(self) -> None: ...

class TrivariateGaussian3D(Function3D):
    r"""
    A function with a 3D Gaussian shape.

    .. math::

        F(x, y, z) = \frac{1}{\sqrt{2 \pi^3} \sigma_x \sigma_y \sigma_z} \exp\left(-\frac{x^2}{2 \sigma_x^2} -\frac{y^2}{2 \sigma_y^2} - \frac{(z - \mu_z)^2}{2 \sigma_z^2}\right)

    The integral over the whole 3D space is equal to 1.The correlation between the standard deviations in x and y directions is equal to 0. The mean value in the
    x and y directions are equal to 0.

    :param float mean_z: Mean value in the z direction.
    :param float stddev_x: The standard deviation in the x directions.
    :param float stddev_y: The standard deviation in the y directions.
    :param float stddev_z: The standard deviation in the z directions.
    """
    def __init__(self, mean_z: float, stddev_x: float, stddev_y: float, stddev_z: float) -> None: ...
    def _init_params(self) -> None: ...
    @property
    def stddev_x(self) -> float: ...
    @stddev_x.setter
    def stddev_x(self, value: float) -> None: ...
    @property
    def stddev_y(self) -> float: ...
    @stddev_y.setter
    def stddev_y(self, value: float) -> None: ...
    @property
    def stddev_z(self) -> float: ...
    @stddev_z.setter
    def stddev_z(self, value: float) -> None: ...
    @property
    def mean_z(self) -> float: ...
    @mean_z.setter
    def mean_z(self, value: float) -> None: ...
    def _cache_constants(self) -> None: ...

class GaussianBeamModel(Function3D):
    r"""
    A Gaussian beam function (https://en.wikipedia.org/wiki/Gaussian_beam)

    .. math::

        F(x, y, z) = \frac{1}{2 \pi \sigma^2_z} \exp\left( -\frac{x^2 + y^2}{2 \sigma_z(z)^2 }\right)

    where the standard deviation in the z direction

    .. math::

        \sigma_z(z) = \sigma_0 \sqrt{1 + \left(\frac{z - z_0}{z_R}\right)^2}

    is a function of position and the

    .. math::

        z_R = \frac{\pi \omega_0^2 n}{\lambda_l}

    is the Rayleigh range.
    """
    def __init__(self, wavelength: float, waist_z: float, stddev_waist: float) -> None: ...
    @property
    def wavelength(self) -> float: ...
    @wavelength.setter
    def wavelength(self, value: float) -> None: ...
    @property
    def waist_z(self) -> float: ...
    @waist_z.setter
    def waist_z(self, value: float) -> None: ...
    @property
    def stddev_waist(self) -> float: ...
    @stddev_waist.setter
    def stddev_waist(self, value: float) -> None: ...
    def _cache_constants(self) -> None: ...
