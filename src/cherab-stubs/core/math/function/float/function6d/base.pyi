from collections.abc import Callable
from typing import TypeAlias, overload

from raysect.core.math.function.float.base import FloatFunction

_Function6DCallable: TypeAlias = Callable[[float, float, float, float, float, float], float]

class Function6D(FloatFunction):
    """
    Cython optimised class for representing an arbitrary 6D function returning a float.

    Using __call__() in cython is slow. This class provides an overloadable
    cython evaluate() method which has much less overhead than a python
    function call.

    For use in cython code only, this class cannot be extended via python.

    To create a new function object, inherit this class and implement the
    evaluate() method. The new function object can then be used with any code
    that accepts a function object.
    """

    def __call__(self, x: float, y: float, z: float, u: float, v: float, w: float) -> float:
        """Evaluate the function f(x, y, z, u, v, w)

        :param float x: function parameter x
        :param float y: function parameter y
        :param float z: function parameter z
        :param float u: function parameter u
        :param float v: function parameter v
        :param float w: function parameter w
        :rtype: float
        """
    @overload
    def __add__(self, other: Function6D | _Function6DCallable, /) -> AddFunction6D: ...
    @overload
    def __add__(self, other: float, /) -> AddScalar6D: ...
    @overload
    def __radd__(self, other: Function6D | _Function6DCallable, /) -> AddFunction6D: ...
    @overload
    def __radd__(self, other: float, /) -> AddScalar6D: ...
    @overload
    def __sub__(self, other: Function6D | _Function6DCallable, /) -> SubtractFunction6D: ...
    @overload
    def __sub__(self, other: float, /) -> SubtractScalar6D: ...
    @overload
    def __rsub__(self, other: Function6D | _Function6DCallable, /) -> SubtractFunction6D: ...
    @overload
    def __rsub__(self, other: float, /) -> SubtractScalar6D: ...
    @overload
    def __mul__(self, other: Function6D | _Function6DCallable, /) -> MultiplyFunction6D: ...
    @overload
    def __mul__(self, other: float, /) -> MultiplyScalar6D: ...
    @overload
    def __rmul__(self, other: Function6D | _Function6DCallable, /) -> MultiplyFunction6D: ...
    @overload
    def __rmul__(self, other: float, /) -> MultiplyScalar6D: ...
    @overload
    def __truediv__(self, other: Function6D | _Function6DCallable, /) -> DivideFunction6D: ...
    @overload
    def __truediv__(self, other: float, /) -> MultiplyScalar6D: ...
    @overload
    def __rtruediv__(self, other: Function6D | _Function6DCallable, /) -> DivideFunction6D: ...
    @overload
    def __rtruediv__(self, other: float, /) -> DivideScalar6D: ...
    @overload
    def __mod__(self, other: Function6D | _Function6DCallable, /) -> ModuloFunction6D: ...
    @overload
    def __mod__(self, other: float, /) -> ModuloFunctionScalar6D: ...
    @overload
    def __rmod__(self, other: Function6D | _Function6DCallable, /) -> ModuloFunction6D: ...
    @overload
    def __rmod__(self, other: float, /) -> ModuloScalarFunction6D: ...
    def __neg__(self) -> MultiplyScalar6D: ...
    @overload
    def __pow__(self, other: Function6D | _Function6DCallable, modulo: None = None, /) -> PowFunction6D: ...
    @overload
    def __pow__(self, other: float, modulo: None = None, /) -> PowFunctionScalar6D: ...
    @overload
    def __pow__(
        self,
        other: Function6D | _Function6DCallable | float,
        modulo: Function6D | _Function6DCallable | float,
        /,
    ) -> ModuloFunction6D | ModuloFunctionScalar6D: ...
    @overload
    def __rpow__(self, other: Function6D | _Function6DCallable, modulo: None = None, /) -> PowFunction6D: ...
    @overload
    def __rpow__(self, other: float, modulo: None = None, /) -> PowScalarFunction6D: ...
    def __abs__(self) -> AbsFunction6D: ...
    @overload
    def __eq__(self, other: Function6D | _Function6DCallable, /) -> EqualsFunction6D: ...  # pyrefly: ignore [bad-override]
    @overload
    def __eq__(self, other: float, /) -> EqualsScalar6D: ...
    @overload
    def __ne__(self, other: Function6D | _Function6DCallable, /) -> NotEqualsFunction6D: ...  # pyrefly: ignore [bad-override]
    @overload
    def __ne__(self, other: float, /) -> NotEqualsScalar6D: ...
    @overload
    def __lt__(self, other: Function6D | _Function6DCallable, /) -> LessThanFunction6D: ...
    @overload
    def __lt__(self, other: float, /) -> GreaterThanScalar6D: ...
    @overload
    def __le__(self, other: Function6D | _Function6DCallable, /) -> LessEqualsFunction6D: ...
    @overload
    def __le__(self, other: float, /) -> GreaterEqualsScalar6D: ...
    @overload
    def __gt__(self, other: Function6D | _Function6DCallable, /) -> GreaterThanFunction6D: ...
    @overload
    def __gt__(self, other: float, /) -> LessThanScalar6D: ...
    @overload
    def __ge__(self, other: Function6D | _Function6DCallable, /) -> GreaterEqualsFunction6D: ...
    @overload
    def __ge__(self, other: float, /) -> LessEqualsScalar6D: ...

class AddFunction6D(Function6D):
    """
    A Function6D class that implements the addition of the results of two Function6D objects: f1() + f2()

    This class is not intended to be used directly, but rather returned as the result of an __add__() call on a
    Function6D object.

    :param function1: A Function6D object.
    :param function2: A Function6D object.
    """

    def __init__(self, function1: Function6D | _Function6DCallable | float, function2: Function6D | _Function6DCallable | float) -> None: ...

class SubtractFunction6D(Function6D):
    """
    A Function6D class that implements the subtraction of the results of two Function6D objects: f1() - f2()

    This class is not intended to be used directly, but rather returned as the result of a __sub__() call on a
    Function6D object.

    :param function1: A Function6D object.
    :param function2: A Function6D object.
    """

    def __init__(self, function1: Function6D | _Function6DCallable | float, function2: Function6D | _Function6DCallable | float) -> None: ...

class MultiplyFunction6D(Function6D):
    """
    A Function6D class that implements the multiplication of the results of two Function6D objects: f1() * f2()

    This class is not intended to be used directly, but rather returned as the result of a __mul__() call on a
    Function6D object.

    :param function1: A Function6D object.
    :param function2: A Function6D object.
    """

    def __init__(self, function1: Function6D | _Function6DCallable | float, function2: Function6D | _Function6DCallable | float) -> None: ...

class DivideFunction6D(Function6D):
    """
    A Function6D class that implements the division of the results of two Function6D objects: f1() / f2()

    This class is not intended to be used directly, but rather returned as the result of a __truediv__() call on a
    Function6D object.

    :param function1: A Function6D object.
    :param function2: A Function6D object.
    """

    def __init__(self, function1: Function6D | _Function6DCallable | float, function2: Function6D | _Function6DCallable | float) -> None: ...

class ModuloFunction6D(Function6D):
    """
    A Function6D class that implements the modulo of the results of two Function6D objects: f1() % f2()

    This class is not intended to be used directly, but rather returned as the result of a __mod__() call on a
    Function6D object.

    :param object function1: A Function6D object or Python callable.
    :param object function2: A Function6D object or Python callable.
    """
    def __init__(self, function1: Function6D | _Function6DCallable | float, function2: Function6D | _Function6DCallable | float) -> None: ...

class PowFunction6D(Function6D):
    """
    A Function6D class that implements the pow() operator on two Function6D objects.

    This class is not intended to be used directly, but rather returned as the result of a __pow__() call on a
    Function6D object.

    :param object function1: A Function6D object or Python callable.
    :param object function2: A Function6D object or Python callable.
    """
    def __init__(self, function1: Function6D | _Function6DCallable | float, function2: Function6D | _Function6DCallable | float) -> None: ...

class AbsFunction6D(Function6D):
    """
    A Function6D class that implements the absolute value of the result of a Function6D object: abs(f()).

    This class is not intended to be used directly, but rather returned as the
    result of an __abs__() call on a Function6D object.

    :param object function: A Function6D object or Python callable.
    """
    def __init__(self, function: Function6D | _Function6DCallable | float) -> None: ...

class EqualsFunction6D(Function6D):
    """
    A Function6D class that tests the equality of the results of two Function6D objects: f1() == f2()

    This class is not intended to be used directly, but rather returned as the result of an __eq__() call on a
    Function6D object.

    :param object function1: A Function6D object or Python callable.
    :param object function2: A Function6D object or Python callable.
    """
    def __init__(self, function1: Function6D | _Function6DCallable | float, function2: Function6D | _Function6DCallable | float) -> None: ...

class NotEqualsFunction6D(Function6D):
    """
    A Function6D class that tests the inequality of the results of two Function6D objects: f1() != f2()

    This class is not intended to be used directly, but rather returned as the result of an __ne__() call on a
    Function6D object.

    :param object function1: A Function6D object or Python callable.
    :param object function2: A Function6D object or Python callable.
    """
    def __init__(self, function1: Function6D | _Function6DCallable | float, function2: Function6D | _Function6DCallable | float) -> None: ...

class LessThanFunction6D(Function6D):
    """
    A Function6D class that implements < of the results of two Function6D objects: f1() < f2()

    This class is not intended to be used directly, but rather returned as the result of an __lt__() call on a
    Function6D object.

    :param object function1: A Function6D object or Python callable.
    :param object function2: A Function6D object or Python callable.
    """
    def __init__(self, function1: Function6D | _Function6DCallable | float, function2: Function6D | _Function6DCallable | float) -> None: ...

class GreaterThanFunction6D(Function6D):
    """
    A Function6D class that implements > of the results of two Function6D objects: f1() > f2()

    This class is not intended to be used directly, but rather returned as the result of a __gt__() call on a
    Function6D object.

    :param object function1: A Function6D object or Python callable.
    :param object function2: A Function6D object or Python callable.
    """
    def __init__(self, function1: Function6D | _Function6DCallable | float, function2: Function6D | _Function6DCallable | float) -> None: ...

class LessEqualsFunction6D(Function6D):
    """
    A Function6D class that implements <= of the results of two Function6D objects: f1() <= f2()

    This class is not intended to be used directly, but rather returned as the result of an __le__() call on a
    Function6D object.

    :param object function1: A Function6D object or Python callable.
    :param object function2: A Function6D object or Python callable.
    """
    def __init__(self, function1: Function6D | _Function6DCallable | float, function2: Function6D | _Function6DCallable | float) -> None: ...

class GreaterEqualsFunction6D(Function6D):
    """
    A Function6D class that implements >= of the results of two Function6D objects: f1() >= f2()

    This class is not intended to be used directly, but rather returned as the result of an __ge__() call on a
    Function6D object.

    :param object function1: A Function6D object or Python callable.
    :param object function2: A Function6D object or Python callable.
    """
    def __init__(self, function1: Function6D | _Function6DCallable | float, function2: Function6D | _Function6DCallable | float) -> None: ...

class AddScalar6D(Function6D):
    """
    A Function6D class that implements the addition of scalar and the result of a Function6D object: K + f()

    This class is not intended to be used directly, but rather returned as the result of an __add__() call on a
    Function6D object.

    :param value: A double value.
    :param function: A Function6D object or Python callable.
    """

    def __init__(self, value: float, function: Function6D | _Function6DCallable) -> None: ...

class SubtractScalar6D(Function6D):
    """
    A Function6D class that implements the subtraction of scalar and the result of a Function6D object: K - f()

    This class is not intended to be used directly, but rather returned as the result of an __sub__() call on a
    Function6D object.

    :param value: A double value.
    :param function: A Function6D object or Python callable.
    """

    def __init__(self, value: float, function: Function6D | _Function6DCallable) -> None: ...

class MultiplyScalar6D(Function6D):
    """
    A Function6D class that implements the multiplication of scalar and the result of a Function6D object: K * f()

    This class is not intended to be used directly, but rather returned as the result of an __mul__() call on a
    Function6D object.

    :param value: A double value.
    :param function: A Function6D object or Python callable.
    """

    def __init__(self, value: float, function: Function6D | _Function6DCallable) -> None: ...

class DivideScalar6D(Function6D):
    """
    A Function6D class that implements the subtraction of scalar and the result of a Function6D object: K / f()

    This class is not intended to be used directly, but rather returned as the result of an __div__() call on a
    Function6D object.

    :param value: A double value.
    :param function: A Function6D object or Python callable.
    """

    def __init__(self, value: float, function: Function6D | _Function6DCallable) -> None: ...

class ModuloScalarFunction6D(Function6D):
    """
    A Function6D class that implements the modulo of scalar and the result of a Function6D object: K % f()

    This class is not intended to be used directly, but rather returned as the result of a __mod__() call on a
    Function6D object.

    :param float value: A double value.
    :param object function: A Function6D object or Python callable.
    """
    def __init__(self, value: float, function: Function6D | _Function6DCallable) -> None: ...

class ModuloFunctionScalar6D(Function6D):
    """
    A Function6D class that implements the modulo of the result of a Function6D object and a scalar: f() % K

    This class is not intended to be used directly, but rather returned as the result of a __mod__() call on a
    Function6D object.

    :param object function: A Function6D object or Python callable.
    :param float value: A double value.
    """
    def __init__(self, function: Function6D | _Function6DCallable, value: float) -> None: ...

class PowScalarFunction6D(Function6D):
    """
    A Function6D class that implements the pow of scalar and the result of a Function6D object: K ** f()

    This class is not intended to be used directly, but rather returned as the result of an __pow__() call on a
    Function6D object.

    :param float value: A double value.
    :param object function: A Function6D object or Python callable.
    """
    def __init__(self, value: float, function: Function6D | _Function6DCallable) -> None: ...

class PowFunctionScalar6D(Function6D):
    """
    A Function6D class that implements the pow of the result of a Function6D object and a scalar: f() ** K

    This class is not intended to be used directly, but rather returned as the result of an __pow__() call on a
    Function6D object.

    :param object function: A Function6D object or Python callable.
    :param float value: A double value.
    """
    def __init__(self, function: Function6D | _Function6DCallable, value: float) -> None: ...

class EqualsScalar6D(Function6D):
    """
    A Function6D class that tests the equality of a scalar and the result of a Function6D object: K == f2()

    This class is not intended to be used directly, but rather returned as the result of an __eq__() call on a
    Function6D object.

    :param value: A double value.
    :param object function: A Function6D object or Python callable.
    """
    def __init__(self, value: float, function: Function6D | _Function6DCallable) -> None: ...

class NotEqualsScalar6D(Function6D):
    """
    A Function6D class that tests the inequality of a scalar and the result of a Function6D object: K != f2()

    This class is not intended to be used directly, but rather returned as the result of an __ne__() call on a
    Function6D object.

    :param value: A double value.
    :param object function: A Function6D object or Python callable.
    """
    def __init__(self, value: float, function: Function6D | _Function6DCallable) -> None: ...

class LessThanScalar6D(Function6D):
    """
    A Function6D class that implements < of a scalar and the result of a Function6D object: K < f2()

    This class is not intended to be used directly, but rather returned as the result of an __lt__() call on a
    Function6D object.

    :param value: A double value.
    :param object function: A Function6D object or Python callable.
    """
    def __init__(self, value: float, function: Function6D | _Function6DCallable) -> None: ...

class GreaterThanScalar6D(Function6D):
    """
    A Function6D class that implements > of a scalar and the result of a Function6D object: K > f2()

    This class is not intended to be used directly, but rather returned as the result of a __gt__() call on a
    Function6D object.

    :param value: A double value.
    :param object function: A Function6D object or Python callable.
    """
    def __init__(self, value: float, function: Function6D | _Function6DCallable) -> None: ...

class LessEqualsScalar6D(Function6D):
    """
    A Function6D class that implements <= of a scalar and the result of a Function6D object: K <= f2()

    This class is not intended to be used directly, but rather returned as the result of an __le__() call on a
    Function6D object.

    :param value: A double value.
    :param object function: A Function6D object or Python callable.
    """
    def __init__(self, value: float, function: Function6D | _Function6DCallable) -> None: ...

class GreaterEqualsScalar6D(Function6D):
    """
    A Function6D class that implements >= of a scalar and the result of a Function6D object: K >= f2()

    This class is not intended to be used directly, but rather returned as the result of an __ge__() call on a
    Function6D object.

    :param value: A double value.
    :param object function: A Function6D object or Python callable.
    """
    def __init__(self, value: float, function: Function6D | _Function6DCallable) -> None: ...
