from .base import Function6D

class Constant6D(Function6D):
    """
    Wraps a scalar constant with a Function6D object.

    This class allows a numeric Python scalar, such as a float or an integer, to
    interact with cython code that requires a Function6D object. The scalar must
    be convertible to double. The value of the scalar constant will be returned
    independent of the arguments the function is called with.

    This class is intended to be used to transparently wrap python objects that
    are passed via constructors or methods into cython optimised code. It is not
    intended that the users should need to directly interact with these wrapping
    objects. Constructors and methods expecting a Function6D object should be
    designed to accept a generic python object and then test that object to
    determine if it is an instance of Function6D. If the object is not a
    Function6D object it should be wrapped using this class for internal use.

    See also: autowrap_function6d()

    :param float value: the constant value to return when called
    """
    def __init__(self, value: float) -> None: ...
