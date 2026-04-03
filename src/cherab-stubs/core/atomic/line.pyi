from .elements import Element

class Line:
    """
    A class fully specifies an observed spectroscopic emission line.

    Note that wavelengths are not arguments to this class. This is because in
    principle the transition has already been fully specified with the other three
    arguments. The wavelength is looked up in the wavelength database of the
    atomic data provider.

    :param Element element: The atomic element/isotope to which this emission line belongs.
    :param int charge: The charge state of the element/isotope that emits this line.
    :param tuple transition: A two element tuple that defines the upper and lower electron
      configuration states of the transition. For hydrogen-like ions it may be enough to
      specify the n-levels with integers (e.g. (3,2)). For all other ions the full spectroscopic
      configuration string should be specified for both states. It is up to the atomic data
      provider package to define the exact notation.

    .. code-block:: pycon

        >>> from cherab.core.atomic import Line, deuterium, carbon
        >>>
        >>> # Specifying the d-alpha and d-gamma balmer lines
        >>> d_alpha = Line(deuterium, 0, (3, 2))
        >>> d_beta = Line(deuterium, 0, (4, 2))
        >>>
        >>> # Specifying a CIII line at 465nm
        >>> ciii_465 = Line(carbon, 2, ('2s1 3p1 3P4.0', '2s1 3s1 3S1.0'))
    """

    element: Element
    charge: int
    transition: tuple[int, int] | tuple[str, str]

    def __init__(
        self,
        element: Element,
        charge: int,
        transition: tuple[int, int] | tuple[str, str],
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __richcmp__(self, other: Line) -> bool: ...
