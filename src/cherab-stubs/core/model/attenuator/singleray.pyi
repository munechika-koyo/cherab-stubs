from ...atomic import AtomicData
from ...beam import Beam, BeamAttenuator
from ...math import Function1D
from ...plasma import Plasma

class SingleRayAttenuator(BeamAttenuator):
    r"""
    Calculates beam attenuation in the single-ray approximation.
    Attenuation is calculated along the beam axis and extrapolated across the beam.

    :param double step: Distance between sample points along the beam axis in meters
        for beam stopping calculation. Defaults to 0.01.
    :param bint clamp_to_zero: Omptimises beam density calculation.
        If True, the beam density outside the clamping range is zero. Defaults to False.
    :param double clamp_sigma: The clamping range as a factor of beam :math:`\sigma(z)`.
        Defaults to 5.
    :param Beam beam: The beam instance to which this attenuator is attached. Defaults to None.
    :param Plasma plasma: The plasma instance with which this beam interacts. Defaults to None.
    :param AtomicData atomic_data: The atomic data provider class for this attenuator.
        Defaults to None.
    """

    _density: Function1D | None
    _stopping_data: list[tuple[object, object]] | None
    _step: float
    _clamp_sigma_sqr: float
    _tanxdiv: float
    _tanydiv: float
    _source_density: float
    clamp_to_zero: bool
    def __init__(
        self,
        step: float = 0.01,
        clamp_to_zero: bool = False,
        clamp_sigma: float = 5.0,
        beam: Beam | None = None,
        plasma: Plasma | None = None,
        atomic_data: AtomicData | None = None,
    ) -> None: ...
    @property
    def step(self) -> float: ...
    @step.setter
    def step(self, value: float) -> None: ...
    @property
    def clamp_sigma(self) -> float: ...
    @clamp_sigma.setter
    def clamp_sigma(self, value: float) -> None: ...
    def density(self, x: float, y: float, z: float) -> float:
        r"""
        Returns the beam density at the specified point in beam coordinate space.
        The beam density is calculated as follows:

        .. math::
            n(x, y, z) = \frac{R}{2\pi v_0 \sigma_x\sigma_y} \exp\left(-\frac{1}{2}\left(\frac{x^2}{\sigma_x^2}+\frac{y^2}{\sigma_y^2}\right)\right)\exp\left(-\int_{0}^{z}\frac{S(z')}{v_0}dz'\right),

            \sigma_x = \sqrt{\sigma^2 + (ztg(\alpha_x))^2},\quad\sigma_y = \sqrt{\sigma^2 + (ztg(\alpha_y))^2},

        where :math:`R=\frac{P}{E}` is the particle rate of the beam defined as the power
        of the beam divided by the kinetic energy of the single particle, :math:`v_0=\sqrt{2E/m}`
        is the particle speed, :math:`\sigma` is the Gaussian beam deviation at origin,
        :math:`\alpha_x` and :math:`\alpha_y` are the beam divergence angles in the :math:`x` and :math:`y`
        dimensions respectively, :math:`S(z)` is the composite beam attenuation coefficient due to
        collisional-radiative interaction with the plasma species:

        .. math::
            S(z) = \sum_{i=1}^{N}Z_i n_i S_i(E_\mathrm{int}, n_{i,e}^{(\mathrm{eq})}, T_i),

            n_{i,e}^{(\mathrm{eq})} = \frac{1}{Z_i}\sum_{j=1}^{N}Z_j^2 n_j.

        Here :math:`Z_i` is the charge of the i-th type of plasma ions,
        :math:`n_i` is density of the i-th type of plasma ions, :math:`N` is the number of type of plasma
        ions, :math:`E_\mathrm{int}` is the kinetic energy of the beam atoms in the frame of reference where
        ions of the i-th type are at rest, :math:`T_{i}` is the temperature of ions of the i-th type.

        The values of partial beam attenuation coefficients, :math:`S_i`, are provided by the atomic data source.

        :param x: x coordinate in meters.
        :param y: y coordinate in meters.
        :param z: z coordinate in meters.
        :return: Density in m^-3.
        """
    def calculate_attenuation(self) -> None:
        """
        Trigger beam attenuation calculation
        """
    def _change(self) -> None: ...
