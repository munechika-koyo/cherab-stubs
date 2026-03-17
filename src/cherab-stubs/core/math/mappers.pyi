# cython: language_level=3

# Copyright 2016-2018 Euratom
# Copyright 2016-2018 United Kingdom Atomic Energy Authority
# Copyright 2016-2018 Centro de Investigaciones Energéticas, Medioambientales y Tecnológicas
#
# Licensed under the EUPL, Version 1.1 or – as soon they will be approved by the
# European Commission - subsequent versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at:
#
# https://joinup.ec.europa.eu/software/page/eupl5
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the Licence is distributed on an "AS IS" basis, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.
#
# See the Licence for the specific language governing permissions and limitations
# under the Licence.

from raysect.core.math.function.float import Function1D, Function2D, Function3D
from raysect.core.math.function.vector3d import Function2D as VectorFunction2D
from raysect.core.math.function.vector3d import Function3D as VectorFunction3D

class IsoMapper2D(Function2D):
    """
    Applies a 1D function to modify the value of a 2D scalar field.

    For a given 2D scalar field f(x,y) and 1D function g(x) this object
    returns g(f(x,y)).

    :param Function2D function2d: the 2D scalar field
    :param Function1D function1d: the 1D function

    .. code-block:: pycon

       >>> from raysect.core.math.function.float import Interpolator1DArray
       >>> from cherab.core.math import IsoMapper2D
       >>> from cherab.tools.equilibrium import example_equilibrium
       >>>
       >>> equilibrium = example_equilibrium()
       >>>
       >>> # extract the 2D psi function
       >>> psi_n = equilibrium.psi_normalised
       >>> # make a 1D psi profile
       >>> profile = Interpolator1DArray(
       ...     [0, 0.5, 0.9, 1.0], [2500, 2000, 1000, 0], "cubic", "none", 0
       ... )
       >>> # perform the flux function mapping
       >>> f = IsoMapper2D(psi_n, profile)
       >>>
       >>> f(2, 0)
       2499.97177
       >>> f(2.2, 0.5)
       1990.03783
    """

    function1d: Function1D
    function2d: Function2D

    def __init__(self, function2d: Function2D, function1d: Function1D): ...

class IsoMapper3D(Function3D):
    """
    Applies a 1D function to modify the value of a 3D scalar field.

    For a given 3D scalar field f(x,y,z) and 1D function g(x) this object
    returns g(f(x,y,z)).

    :param Function3D function3d: the 3D scalar field
    :param Function1D function1d: the 1D function

    .. code-block:: pycon

       >>> from raysect.core.math.function.float import Interpolator1DArray
       >>> from cherab.core.math import IsoMapper2D, AxisymmetricMapper
       >>> from cherab.tools.equilibrium import example_equilibrium
       >>>
       >>> equilibrium = example_equilibrium()
       >>>
       >>> # extract the 3D psi function
       >>> psi_n = equilibrium.psi_normalised
       >>> psi_n_3d = AxisymmetricMapper(psi_n)
       >>> # make a 1D psi profile
       >>> profile = Interpolator1DArray(
       ...     [0, 0.5, 0.9, 1.0], [2500, 2000, 1000, 0], "cubic", "none", 0
       ... )
       >>> # perform the flux function mapping
       >>> f = IsoMapper3D(psi_n_3d, profile)
       >>>
       >>> f(2, 0, 0)
       2499.97177
       >>> f(0, 2, 0)
       2499.97177
    """

    function1d: Function1D
    function3d: Function3D

    def __init__(self, function3d: Function3D, function1d: Function1D): ...

class Swizzle2D(Function2D):
    """
    Inverts the argument order of the specified function.

    :param Function2D function2d: The 2D function you want to inverse the arguments.

    .. code-block:: pycon

       >>> from cherab.core.math import Swizzle2D
       >>>
       >>> def f1(r, z):
       >>>     return r**2 + z
       >>>
       >>> f2 = Swizzle2D(f1)
       >>>
       >>> f2(3, 0)
       3.0
    """

    function2d: Function2D

    def __init__(self, function2d: Function2D): ...

class Swizzle3D(Function3D):
    """
    Rearranges the order of a 3D functions arguments.

    For instance, a 90 degree rotation of function coordinates can be performed
    by swapping arguments: xyz -> xzy

    Shape is a tuple of 3 integers from 0,1,2 imposing the order of
    arguments. 0, 1 and 2 correspond respectively to x, y and z where (
    x,y,z) are the initial arguments.
    For instance:
    shape = (0,2,1) transforms f(x,y,z) in f(x,z,y)
    shape = (1,0,1) transforms f(x,y,z) in f(y,x,y)

    :param Function3D function3d: the 3D function you want to reorder the arguments.
    :param tuple shape: a tuple of integers imposing the order of the arguments.

    .. code-block:: pycon

       >>> from cherab.core.math import Swizzle3D
       >>>
       >>> def f1(x, y, z):
       >>>     return x**3 + y**2 + z
       >>>
       >>> f2 = Swizzle3D(f1, (0, 2, 1))
       >>>
       >>> f2(3, 2, 1)
       30.0
    """

    function3d: Function3D
    shape: tuple

    def __init__(self, function3d: Function3D, shape: tuple): ...

class AxisymmetricMapper(Function3D):
    """
    Performs an 360 degree rotation of a 2D function (defined on the xz plane) around the z-axis.

    Due to the nature of this mapping, only the positive region of the x range
    of the supplied function is mapped.

    :param Function2D function2d: The function to be mapped.

    .. code-block:: pycon

       >>> from numpy import sqrt
       >>> from cherab.core.math import AxisymmetricMapper
       >>>
       >>> def f1(r, z):
       >>>     return r
       >>>
       >>> f2 = AxisymmetricMapper(f1)
       >>>
       >>> f2(1, 0, 0)
       1.0
       >>> f2(1 / sqrt(2), 1 / sqrt(2), 0)
       0.99999999
    """

    function2d: Function2D

    def __init__(self, function2d: Function2D): ...

class VectorAxisymmetricMapper(VectorFunction3D):
    """
    Performs an 360 degree rotation of a 2D vector function (defined on the xz plane) around the z-axis.

    Due to the nature of this mapping, only the positive region of the x range
    of the supplied function is mapped.

    :param VectorFunction2D vectorfunction2d: The vector function to be mapped.

    .. code-block:: pycon

       >>> from cherab.core.math import VectorAxisymmetricMapper
       >>>
       >>> def my_func(r, z):
       >>>     v = Vector3D(1, 0, 0)
       >>>     v.length = r
       >>>     return v
       >>>
       >>> f = VectorAxisymmetricMapper(my_func)
       >>>
       >>> f(1, 0, 0)
       Vector3D(1.0, 0.0, 0.0)
       >>> f(1 / sqrt(2), 1 / sqrt(2), 0)
       Vector3D(0.70710678, 0.70710678, 0.0)
    """

    function2d: VectorFunction2D

    def __init__(self, vectorfunction2d: VectorFunction2D): ...
