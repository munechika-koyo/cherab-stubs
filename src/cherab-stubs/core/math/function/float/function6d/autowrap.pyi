from .base import Function6D, _Function6DCallable

class PythonFunction6D(Function6D):
    """
    Wraps a python callable object with a Function6D object.

    This class allows a python object to interact with cython code that requires
    a Function6D object. The python object must implement __call__() expecting
    six arguments.

    This class is intended to be used to transparently wrap python objects that
    are passed via constructors or methods into cython optimised code. It is not
    intended that the users should need to directly interact with these wrapping
    objects. Constructors and methods expecting a Function6D object should be
    designed to accept a generic python object and then test that object to
    determine if it is an instance of Function6D. If the object is not a
    Function6D object it should be wrapped using this class for internal use.

    See also: autowrap_function6d()
    """

    function: _Function6DCallable

    def __init__(self, function: _Function6DCallable) -> None: ...
