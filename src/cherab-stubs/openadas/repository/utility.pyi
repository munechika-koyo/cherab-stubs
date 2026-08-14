from ...core.atomic import Element

DEFAULT_REPOSITORY_PATH: str

def encode_transition(transition: tuple[int | str, int | str]) -> str:
    """
    Generate a key string from a transition.

    Both integer and string transition descriptions are handled.
    """

def valid_charge(element: Element, charge: int) -> bool:
    """
    Returns true if the element can be ionised to the specified charge state level.

    :param charge: Integer charge state.
    :return: True/False.
    """
