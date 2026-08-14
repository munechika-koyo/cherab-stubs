from typing import TextIO

import numpy as np
from numpy.typing import NDArray

from ...core.utility.conversion import PerCm3ToPerM3 as PerCm3ToPerM3

def parse_adas2x_rate(file: TextIO, normalisation: float = 1) -> dict[str, object]:
    """
    Read and parse data from the supplied adf21/22 file stream.

    :param file: A file stream.
    :param normalisation: Normalisation factor applied to rate coefficients. Equals to 1E-6
                          (cm3 to m3) for beam emission and beam stopping rates and 1 for beam
                          population coefficient.
    :return: A dictionary.
    """

def readvalues(file: TextIO, nb_values: int, values_per_line: int, type: type[object] = ...) -> NDArray[np.object_]:
    """
    Read and return a given number of values in a file, taking into account
    end of lines. The reading begins at the current read line of the file (which
    must be open to use this function). The read lines of the file are assumed
    to be shaped as following:
    a first useless character, then a given number of 10 characters values, and
    any other characters after (not read).

    :param file: file in which values have to be read
    :param nb_values: number of values to be read
    :param values_per_line: number of values per line on the file
    :param type: python type of the values to be returned
    :return: a numpy 1D array with the read values in the reading order.
    """
