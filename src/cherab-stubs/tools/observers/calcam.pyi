from os import PathLike

import numpy as np
from numpy.typing import NDArray

def load_calcam_calibration(cal_file_path: str | PathLike[str], reduction_factor: int = 1) -> tuple[tuple[int, int], NDArray[np.object_], NDArray[np.object_]]:
    """
    Extract camera calibration information from a calcam netCDF file.

    :param cal_file_path: path to calcam calibration netCDF file.
    :param reduction_factor: number of pixels to skip when reading the netCDF file.
    :return: tuple of (pixels_shape, pixel_origins, pixel_directions).
    """
