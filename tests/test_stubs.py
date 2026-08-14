"""Regression tests for representative Cherab user code."""

from collections.abc import Sequence

import pytest
from mypy import api


def _mypy(source: str, extra_args: Sequence[str] = ()) -> tuple[str, int]:
    stdout, stderr, status = api.run(
        [
            "--no-error-summary",
            "--show-error-codes",
            "--strict",
            *extra_args,
            "-c",
            source,
        ]
    )
    assert not stderr
    return stdout, status


@pytest.mark.parametrize(
    "source",
    [
        """
import sys
if sys.version_info >= (3, 11):
    from typing import assert_type
else:
    from typing_extensions import assert_type
from raysect.core import Point3D, Vector3D, World
from raysect.primitive import Sphere
from cherab.core import Maxwellian, Plasma, Species, hydrogen
from cherab.openadas import OpenADAS

world = World()
distribution = Maxwellian(1e19, 100.0, Vector3D(0, 0, 0), 1.67e-27)
species = Species(hydrogen, 1, distribution)
plasma = Plasma(parent=world)
plasma.atomic_data = OpenADAS()
plasma.geometry = Sphere(1.0)
plasma.b_field = Vector3D(0, 0, 2)
plasma.electron_distribution = distribution
plasma.composition = [species]
assert_type(plasma.ion_density(0, 0, 0), float)
assert_type(plasma.composition.get(hydrogen, 1), Species)
assert_type(Point3D(0, 0, 0).vector_to(Point3D(1, 0, 0)), Vector3D)
""",
        """
import sys
if sys.version_info >= (3, 11):
    from typing import assert_type
else:
    from typing_extensions import assert_type
from raysect.core import Primitive, Vector3D, World
from cherab.core import Beam, Line, carbon, deuterium, hydrogen
from cherab.core.beam.node import ModelManager as BeamModelManager
from cherab.core.laser import Laser
from cherab.core.laser.node import ModelManager as LaserModelManager
from cherab.core.model import BeamCXLine, ExcitationLine, GaussianLine
from cherab.openadas import OpenADAS

world = World()
beam = Beam(parent=world)
beam.atomic_data = OpenADAS()
beam.element = deuterium
beam.energy = 60_000.0
beam.power = 10_000.0
beam.models = [BeamCXLine(Line(carbon, 5, (8, 7)))]
assert_type(beam.models, BeamModelManager)
assert_type(beam.density(0, 0, 1), float)
assert_type(beam.direction(0, 0, 1), Vector3D)
assert_type(hydrogen.name, str)
assert_type(hydrogen.atomic_number, int)

laser = Laser(parent=world)
laser.models = []
assert_type(laser.models, LaserModelManager)
assert_type(laser.get_geometry(), list[Primitive])
model = ExcitationLine(Line(carbon, 1, (3, 2)), lineshape=GaussianLine)
assert_type(model, ExcitationLine)
""",
        """
import sys
if sys.version_info >= (3, 11):
    from typing import assert_type
else:
    from typing_extensions import assert_type
import numpy as np
from numpy.typing import NDArray
from raysect.core.math.function.float import Constant3D
from raysect.optical import Spectrum
from cherab.openadas import OpenADAS
from cherab.core import hydrogen
from cherab.tools.emitters import RadiationFunction
from cherab.tools.inversions import ToroidalVoxelGrid
from cherab.tools.raytransfer import CartesianRayTransferEmitter, RayTransferBox

emitter_from_callable = RadiationFunction(lambda x, y, z: x + y + z)
emitter_from_function = RadiationFunction(Constant3D(1.0))
adas = OpenADAS(permit_extrapolation=True)
assert_type(adas.wavelength(hydrogen, 0, (3, 2)), float)
assert_type(adas.ionisation_rate(hydrogen, 0).evaluate(1e19, 10.0), float)
grid = ToroidalVoxelGrid([[(1.0, -0.1), (1.1, -0.1), (1.1, 0.1), (1.0, 0.1)]])
assert_type(grid.emissivities_from_function(lambda x, y, z: 1.0), NDArray[np.float64])
rt_emitter = CartesianRayTransferEmitter((2, 2, 2), (0.1, 0.1, 0.1))
assert_type(rt_emitter.bins, int)
rt_box = RayTransferBox(1.0, 1.0, 1.0, 10, 10, 10)
assert_type(rt_box.bins, int)
""",
    ],
)
def test_representative_public_api(source: str) -> None:
    stdout, status = _mypy(source)
    assert status == 0, stdout


def test_python_subclass_extension_hooks() -> None:
    stdout, status = _mypy(
        """
import sys
if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override
from raysect.core import Point3D, Vector3D
from raysect.optical import Spectrum
from cherab.core import AtomicData, Plasma
from cherab.core.beam import BeamAttenuator, BeamModel
from cherab.core.plasma import PlasmaModel

class CustomPlasmaModel(PlasmaModel):
    @override
    def emission(self, point: Point3D, direction: Vector3D, spectrum: Spectrum) -> Spectrum:
        return spectrum

    @override
    def _change(self) -> None:
        pass

class CustomBeamAttenuator(BeamAttenuator):
    @override
    def density(self, x: float, y: float, z: float) -> float:
        return 0.0

    @override
    def _change(self) -> None:
        pass

class CustomBeamModel(BeamModel):
    @override
    def emission(
        self,
        beam_point: Point3D,
        plasma_point: Point3D,
        beam_direction: Vector3D,
        observation_direction: Vector3D,
        spectrum: Spectrum,
    ) -> Spectrum:
        return spectrum
"""
    )
    assert status == 0, stdout


def test_invalid_calls_are_rejected() -> None:
    stdout, status = _mypy(
        """
from cherab.core import Beam, Plasma, hydrogen
from cherab.openadas import OpenADAS

beam = Beam()
beam.power = "high"
plasma = Plasma()
plasma.ion_density(0, 0)
OpenADAS().ionisation_rate(hydrogen, "neutral")
"""
    )
    assert status != 0
    assert "Incompatible types in assignment" in stdout
    assert "Missing positional argument" in stdout
    assert "incompatible type" in stdout
