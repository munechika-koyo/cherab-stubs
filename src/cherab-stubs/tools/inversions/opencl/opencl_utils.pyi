_has_pyopencl: bool

def get_flops(device: object, verbose: bool = False) -> float:
    """
    Returns the theoretical peak performance of specified OpenCL-compatible GPU or ACCELERATOR.
    Currently supports only Nvidia, AMD, Intel or Mali GPUs.

    :param pyopencl.Device device: OpenCL device.
    :param bool verbose: Verbose output, defaults to `verbose=False`.

    :return: Theoretical peak performance in GFLOPs.
    """

def get_best_gpu(platforms: list[object] | None = None, device_type: int | None = None, verbose: bool = False) -> object | None:
    """
    Finds the fastest (in terms of theoretical peak performance) GPU and/or accelerator
    available in specified OpenCL platforms

    :param list platforms: List of pyopencl.Platform instances. Default value: `platforms=None`
                           (all available OpenCL platforms).
    :param pyopencl.device_type device_type: OpenCL device type (GPU, ACCELERATOR, or both).
                                             Default value: `device_type=None` (GPU or accelerator).
                                             If device_type is ALL or DEFAULT, all non-GPU/ACCELERATOR
                                             devices will be skipped.
    :param bool verbose: Verbose output, defaults to `verbose=False`.

    :return: The pyopencl.Device instance corresponding to the fastest GPU or accelerator available
             in the specified OpenCL platforms.
    """

def get_first_device(platforms: list[object] | None = None, device_type: int | None = None, verbose: bool = False) -> object | None:
    """
    Returns the first OpenCL device of specified type available in specified OpenCL platforms

    :param list platforms: List of pyopencl.Platform instances. Default value: `platforms=None` (all available OpenCL platforms).
    :param pyopencl.device_type device_type: OpenCL device type (GPU, ACCELERATOR, CPU, ALL, etc.).
        Default value: `device_type=None` (GPU or accelerator).
    :param bool verbose: Verbose output, defaults to `verbose=False`.

    :return: The pyopencl.Device instance corresponding to the first device available in the specified OpenCL platforms.
    """

def device_select(platform_id: int | None = None, device_id: int | None = None, device_type: int | None = None, verbose: bool = False) -> object:
    """
    OpenCL device selector. Returns the most powerful OpenCL device available
    if device_type is GPU or ACCELERATOR or the first OpenCL device available
    if device_type is CPU, ALL or CUSTOM.

    :param int platform_id: OpenCL platform ID, defaults to `platform_id=None`.
    :param int device_id: OpenCL device ID (in the selected OpenCL platform),
                          defaults to `device_id=None`.
    :param pyopencl.device_type device_type: OpenCL device type (GPU, ACCELERATOR, etc.).
                                             Default value: `device_type=None` (GPU | ACCELERATOR).
    :param bool verbose: Verbose output, defaults to `verbose=False`.

    :return: The pyopencl.Device instance corresponding to the selected OpenCL device.
    """
