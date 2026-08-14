from collections.abc import Mapping, Sequence

from raysect.core.math import Point3D, Vector3D
from raysect.optical import Spectrum

from ...atomic import AtomicData, Line
from ...beam import Beam
from ...beam.model import BeamModel
from ...plasma import Plasma
from ..lineshape import LineShapeModel

class BeamCXLine(BeamModel):
    """
    Calculates emission produced by charge-exchange of plasma ions
    with beam species.

    :param Line line: The emission line object.
    :param Beam beam: The beam object.
    :param Plasma plasma: The emitting plasma object.
    :param AtomicData atomic_data: The atomic data provider.
    :param object lineshape: The spectral line shape class. Must be a subclass of `LineShapeModel`.
                             Defaults to `GaussianLine`.
    :param object lineshape_args: The arguments of spectral line shape class. Defaults is None.
    :param object lineshape_kwargs: The keyword arguments of spectral line shape class.
                                    Defaults is None.

    :ivar Line line: The emission line object.

    .. code-block:: pycon

        >>> from cherab.core.model import BeamCXLine
        >>> from cherab.core.atomic import carbon
        >>> from cherab.core.model import ParametrisedZeemanTriplet
        >>>
        >>> cVI_8_7 = Line(carbon, 5, (8, 7))  # emission line
        >>> # define plasma, beam and atomic data, plasma mast contain C6+ ions.
        >>> ...
        >>> # here we override default line shape class, GaussianLine,
        >>> # with ParametrisedZeemanTriplet to take into account Zeeman splitting.
        >>> beam_cx_line = BeamCXLine(cVI_8_7, lineshape=ParametrisedZeemanTriplet)
        >>> beam.models = [beam_cx_line]
    """
    def __init__(
        self,
        line: Line,
        beam: Beam | None = None,
        plasma: Plasma | None = None,
        atomic_data: AtomicData | None = None,
        lineshape: type[LineShapeModel] | None = None,
        lineshape_args: Sequence[object] | None = None,
        lineshape_kwargs: Mapping[str, object] | None = None,
    ) -> None: ...
    @property
    def line(self) -> Line: ...
    @line.setter
    def line(self, value: Line) -> None: ...
    def emission(
        self,
        beam_point: Point3D,
        plasma_point: Point3D,
        beam_direction: Vector3D,
        observation_direction: Vector3D,
        spectrum: Spectrum,
    ) -> Spectrum: ...
    def _change(self) -> None: ...
