from typing import Literal

from raysect.core.math.function.float import Function1D

class ZeemanStructure:
    """
    Provides wavelengths and ratios of
    :math:`\\pi`-/:math:`\\sigma`-polarised Zeeman components for any given value of
    magnetic field strength.

    :param list pi_components: A list of 2-tuples of Function1D objects that provide the
                               wavelengths and ratios of individual :math:`\\pi`-polarised
                               Zeeman components for a given magnetic field strength:
                               [(wvl_func1, ratio_func1), (wvl_func2, ratio_func2), ...]
    :param list sigma_plus_components: A list of 2-tuples of Function1D objects that provide the
                                       wavelengths and ratios of individual
                                       :math:`\\sigma^{+}`-polarised Zeeman components for
                                       a given magnetic field strength:
                                       [(wvl_func1, ratio_func1), (wvl_func2, ratio_func2), ...]
    :param list sigma_minus_components: A list of 2-tuples of Function1D objects that provide the
                                        wavelengths and ratios of individual
                                        :math:`\\sigma^{-}`-polarised
                                        Zeeman components for a given magnetic field strength:
                                        [(wvl_func1, ratio_func1), (wvl_func2, ratio_func2), ...]
    """
    def __init__(
        self,
        pi_components: list[tuple[Function1D, Function1D]],
        sigma_plus_components: list[tuple[Function1D, Function1D]],
        sigma_minus_components: list[tuple[Function1D, Function1D]],
    ) -> None: ...
    def __call__(self, b: float, polarisation: Literal["pi", "sigma_plus", "sigma_minus"]): ...
