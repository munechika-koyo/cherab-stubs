from raysect.core.math import Point3D, Vector3D
from raysect.optical import Spectrum

from ..atomic import AtomicData
from ..plasma import Plasma
from ..utility.notify import Notifier
from .node import Beam

class BeamModel:
    def __init__(self) -> None: ...
    @property
    def plasma(self) -> Plasma | None: ...
    @plasma.setter
    def plasma(self, value: Plasma | None) -> None: ...
    @property
    def beam(self) -> Beam | None: ...
    @beam.setter
    def beam(self, value: Beam | None) -> None: ...
    @property
    def atomic_data(self) -> AtomicData | None: ...
    @atomic_data.setter
    def atomic_data(self, value: AtomicData | None) -> None: ...
    def emission(
        self,
        beam_point: Point3D,
        plasma_point: Point3D,
        beam_direction: Vector3D,
        observation_direction: Vector3D,
        spectrum: Spectrum,
    ) -> Spectrum:
        """
        Calculate the emission for a point on the beam in a specified direction.

        Models implementing this method must add their spectral response to the
        supplied spectrum object. The spectrum units are spectral radiance per
        meter (W/m^3/str/nm).

        :param beam_point: Point in beam space.
        :param plasma_point: Point in plasma space.
        :param beam_direction: Beam axis direction in plasma space.
        :param observation_direction: Observation direction in plasma space.
        :param spectrum: Spectrum to which emission should be added.
        :return: Updated Spectrum object.
        """
    def _change(self) -> None:
        """
        Called if the plasma, beam or the atomic data source properties change.

        If the model caches calculation data that would be invalidated if its
        source data changes then this method may be overridden to clear the
        cache.
        """

class BeamAttenuator:
    notifier: Notifier
    def __init__(self) -> None: ...
    @property
    def plasma(self) -> Plasma | None: ...
    @plasma.setter
    def plasma(self, value: Plasma | None) -> None: ...
    @property
    def beam(self) -> Beam | None: ...
    @beam.setter
    def beam(self, value: Beam | None) -> None: ...
    @property
    def atomic_data(self) -> AtomicData | None: ...
    @atomic_data.setter
    def atomic_data(self, value: AtomicData | None) -> None: ...
    def density(self, x: float, y: float, z: float) -> float:
        """
        Returns the beam density at the specified point.

        The point is specified in beam space.

        :param x: x coordinate in meters.
        :param y: y coordinate in meters.
        :param z: z coordinate in meters.
        :return: Density in m^-3.
        """
    def _change(self) -> None:
        """
        Called if the plasma, beam or the atomic data source properties change.

        If the model caches calculation data that would be invalidated if its
        source data changes then this method may be overridden to clear the
        cache.
        """
