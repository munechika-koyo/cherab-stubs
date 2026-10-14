from .base import Function6D, _Function6DCallable

class Blend6D(Function6D):
    """
    Performs a linear interpolation between two scalar functions, modulated by a 3rd scalar function.

    The value of the scalar mask function is used to interpolated between the
    values returned by the two functions. Mathematically the value returned by
    this function is as follows:

    .. math::
        v = (1 - f_m(x, y, z, u, v, w)) f_1(x, y, z, u, v, w) + f_m(x, y, z, u, v, w) f_2(x, y, z, u, v, w)

    The value of the mask function is clamped to the range [0, 1] if the sampled
    value exceeds the required range.
    """

    def __init__(
        self,
        f1: Function6D | _Function6DCallable | float,
        f2: Function6D | _Function6DCallable | float,
        mask: Function6D | _Function6DCallable | float,
    ):
        """
        :param float.Function6D f1: First scalar function.
        :param float.Function6D f2: Second scalar function.
        :param float.Function6D mask: Scalar function returning a value in the range [0, 1].
        """
