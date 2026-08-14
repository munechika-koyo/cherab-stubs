from os import PathLike

from ...tools.equilibrium import EFITEquilibrium

def load_equilibrium(file_path: str | PathLike[str] | None = None) -> EFITEquilibrium:
    """
    Load Generomak EFITEquilibrium.

    :param str file_path: Path to the json equilibrium file (optional)
    :return: EFITEquilibrium
    """
